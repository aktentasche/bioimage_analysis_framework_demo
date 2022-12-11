from loguru import logger
from skimage import color, util
from skimage.filters import sato

from .bioimage_processing_service import bioimage_processing_service
from .models import *


@bioimage_processing_service.task()
def task_isolate_rgb(json_image: JsonImage) -> str:
    raise NotImplementedError()
