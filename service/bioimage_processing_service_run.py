from uuid import uuid4

from .bioimage_processing_service import bioimage_processing_service

argv = [
    "worker",
    "--pool",
    "prefork",
    "--loglevel",
    "DEBUG",
    "--task-events",
    "--hostname",
    f"bioimage_processing_service-{uuid4()}@%h",
]
bioimage_processing_service.worker_main(argv)
