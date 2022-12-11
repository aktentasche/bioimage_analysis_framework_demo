from celery import Celery
from pydantic import AmqpDsn, RedisDsn, parse_obj_as

# from .models import *

# settings
broker_dsn: AmqpDsn = parse_obj_as(AmqpDsn, "amqp://biodude:biodude@localhost")
result_backend_dsn: RedisDsn = parse_obj_as(RedisDsn, "redis://localhost:6379/0")

bioimage_processing_service = Celery(
    "service.bioimage_processing_service",
    broker=broker_dsn,
    backend=result_backend_dsn,
    include=[
        "service.task_detect_ridges",
        "service.task_isolate_rgb",
        "service.task_recognize_faces",
        "service.tasks_storage",
    ],
)
