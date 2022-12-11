import numpy as np
from skimage import color, util
from skimage.filters import sato

from .bioimage_processing_service import bioimage_processing_service
from .models import *


@bioimage_processing_service.task()
def task_detect_ridges(image: NpImage) -> DetectRidgesResponse:
    # convert to grayscale first
    grayscale_image: NpImage = color.rgb2gray(image)  # type: ignore
    processed_image: NpImage = sato(grayscale_image, black_ridges=True)
    return DetectRidgesResponse(
        processed_image_json=convert_npimg_to_jsonimg(processed_image),
        grayscale_image_json=convert_npimg_to_jsonimg(grayscale_image),
        processed_image_inverted_json=convert_npimg_to_jsonimg(
            util.invert(processed_image)  # type: ignore
        ),
    )
