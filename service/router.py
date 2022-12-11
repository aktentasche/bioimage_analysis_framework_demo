from __future__ import annotations

from io import BytesIO
from typing import Callable

from fastapi import APIRouter, File, UploadFile
from fastapi.responses import StreamingResponse
from skimage.io import imread, imsave  # type: ignore

from service.models import *
from service.proxy import BioImageProcessingProxy

router = APIRouter()


@router.post(
    "/detect_ridges",
    response_class=StreamingResponse,
)
async def detect_ridges(file: UploadFile = File(...)) -> StreamingResponse:
    proxy = BioImageProcessingProxy()
    return await _process_image(proxy.detect_ridges, file)


@router.post(
    "/isolate_rgb",
    response_class=StreamingResponse,
)
async def isolate_rgb(file: UploadFile = File(...)) -> StreamingResponse:
    proxy = BioImageProcessingProxy()
    return await _process_image(proxy.isolate_rgb, file)


@router.post(
    "/recognize_faces",
    response_class=StreamingResponse,
)
async def recognize_faces(file: UploadFile = File(...)) -> StreamingResponse:
    proxy = BioImageProcessingProxy()
    return await _process_image(proxy.recognize_faces, file)


async def _process_image(
    process_function: Callable[[NpImage], ImageBaseResponse],
    file: UploadFile = File(...),
) -> StreamingResponse:

    request_image_data_binary = await file.read()
    image: NpImage = imread(request_image_data_binary, plugin="imageio")  # type: ignore

    # send image to proxy
    response = process_function(image)  # type: ignore

    # store processed image in buffer to stream back to browser
    buffer = BytesIO()
    imsave(buffer, response.processed_image, format="JPEG", quality=95)
    buffer.seek(0)

    return StreamingResponse(buffer, media_type="image/jpeg")
