from loguru import logger
from skimage import color, util
from skimage.filters import sato

from .bioimage_processing_service import bioimage_processing_service
from .models import *


@bioimage_processing_service.task()
def task_detect_ridges(json_image: JsonImage) -> str:
    # convert to JSON and grayscale first
    logger.info("Converting to grayscale")
    np_image = convert_jsonimg_to_npimg(json_image)
    grayscale_image: NpImage = color.rgb2gray(np_image)  # type: ignore
    logger.info("Apply Sato ridge detection")
    processed_image: NpImage = sato(grayscale_image, black_ridges=True)
    logger.info("Done!")
    return DetectRidgesResponse(
        processed_image_json=convert_npimg_to_jsonimg(processed_image),
        grayscale_image_json=convert_npimg_to_jsonimg(grayscale_image),
        processed_image_inverted_json=convert_npimg_to_jsonimg(
            util.invert(processed_image)  # type: ignore
        ),
    ).json()
