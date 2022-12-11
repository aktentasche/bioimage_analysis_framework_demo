from service.bioimage_processing_service import bioimage_processing_service

argv = [
    "worker",
    "--pool",
    "prefork",
    "--loglevel",
    "DEBUG",
    "--task-events",
    "--hostname",
    f"bioimage_processing_service@%h",
]
bioimage_processing_service.worker_main(argv)
