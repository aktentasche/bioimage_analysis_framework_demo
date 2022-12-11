from .bioimage_processing_service import bioimage_processing_service
from .models import *


@bioimage_processing_service.task()
def task_store_image(image: int) -> str:
    return "image"


@bioimage_processing_service.task()
def task_retrieve_image(image: int) -> str:
    return "image"


@bioimage_processing_service.task()
def task_retrieve_images(image: int) -> str:
    return "image"
