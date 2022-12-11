from .bioimage_processing_service import bioimage_processing_service
from .models import *


@bioimage_processing_service.task()
def task_isolate_rgb(image: int) -> str:
    return "image"
