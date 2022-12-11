from celery.exceptions import TimeoutError
from kombu import Queue

from .models import *
from .task_detect_ridges import task_detect_ridges
from .task_isolate_rgb import task_isolate_rgb
from .task_recognize_faces import task_recognize_faces

_TIMEOUT_SECONDS = 10


class BioImageProcessingProxy:
    def detect_ridges(
        self,
        # need np image for usage from scriptm json image from web ui
        image: NpImage | JsonImage,
    ) -> DetectRidgesResponse:

        # convert to JsonImage if not already
        if not isinstance(image, JsonImage):
            image = convert_npimg_to_jsonimg(image)

        response_future = task_detect_ridges.apply_async(args=(image,))
        try:
            return DetectRidgesResponse.parse_raw(
                response_future.get(timeout=_TIMEOUT_SECONDS)
            )

        except TimeoutError:
            msg = f"""Could not get result from detect_ridges within 
                    {_TIMEOUT_SECONDS} seconds."""
            raise TimeoutError(msg)

    def isolate_rgb(
        self,
        image: int,
    ) -> IsolateRgbResponse:

        response_future = task_isolate_rgb.apply_async(
            args=(image,),
            queue=Queue(name="isolate_rgb", auto_delete=True, durable=False),
        )
        try:
            return IsolateRgbResponse.parse_raw(
                response_future.get(timeout=_TIMEOUT_SECONDS)
            )
        except TimeoutError:
            msg = f"""Could not get result from isolate_rgb within 
                    {_TIMEOUT_SECONDS} seconds."""
            raise TimeoutError(msg)

    def recognize_faces(
        self,
        image: int,
    ) -> DetectRidgesResponse:

        response_future = task_recognize_faces.apply_async(
            args=(image,),
            queue=Queue(name="recognize_faces", auto_delete=True, durable=False),
        )
        try:
            return DetectRidgesResponse.parse_raw(
                response_future.get(
                    disable_sync_subtasks=False, timeout=_TIMEOUT_SECONDS
                )
            )
        except TimeoutError:
            msg = f"""Could not get result from recognize_faces within 
                    {_TIMEOUT_SECONDS} seconds."""
            raise TimeoutError(msg)
