from __future__ import annotations

import uuid
from typing import Callable

from fastapi import APIRouter, File, Response, UploadFile
from fastapi.responses import FileResponse
from skimage.io import imread, imsave  # type: ignore
from skimage.util import img_as_ubyte

from service.models import *
from service.proxy import BioImageProcessingProxy

router = APIRouter()


@router.post(
    "/detect_ridges",
    response_class=Response,
    responses={200: {"content": {"image/png": {}}}},
)
async def detect_ridges(file: UploadFile = File(...)) -> Response:
    proxy = BioImageProcessingProxy()
    return await _process_image(proxy.detect_ridges, file)


@router.post(
    "/isolate_rgb",
    response_class=Response,
)
async def isolate_rgb(file: UploadFile = File(...)) -> Response:
    proxy = BioImageProcessingProxy()
    return await _process_image(proxy.isolate_rgb, file)


@router.post(
    "/recognize_faces",
    response_class=Response,
)
async def recognize_faces(file: UploadFile = File(...)) -> Response:
    proxy = BioImageProcessingProxy()
    return await _process_image(proxy.recognize_faces, file)


async def _process_image(
    process_function: Callable[[NpImage], ImageBaseResponse],
    file: UploadFile = File(...),
) -> Response:

    request_image_data_binary = await file.read()
    image: NpImage = imread(request_image_data_binary, plugin="imageio")  # type: ignore

    # send image to proxy
    response = process_function(image)  # type: ignore

    # temp store result. ugly but works for now.
    filename = str(f"{uuid.uuid4()}.png")
    imsave(filename, response.processed_image)

    return FileResponse(filename, media_type="image/png")
