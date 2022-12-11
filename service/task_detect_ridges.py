from .bioimage_processing_service import bioimage_processing_service
from .models import *


@bioimage_processing_service.task()
def task_detect_ridges(image: int) -> str:
    return "image"
