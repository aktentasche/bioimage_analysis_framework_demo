import json_numpy
import numpy as np
from pydantic import BaseModel, Field

NpImage = np.ndarray[int, np.dtype[np.generic]]
JsonImage = str


def convert_npimg_to_jsonimg(np_image: NpImage) -> JsonImage:
    return json_numpy.dumps(np_image)  # type: ignore


def convert_jsonimg_to_npimg(json_image: JsonImage) -> NpImage:
    return json_numpy.loads(json_image)  # type: ignore


class ImageBaseResponse(BaseModel):
    processed_image_json: JsonImage
    grayscale_image_json: JsonImage

    @property
    def processed_image(self) -> NpImage:
        return convert_jsonimg_to_npimg(self.processed_image_json)

    @property
    def grayscale_image(self) -> NpImage:
        return convert_jsonimg_to_npimg(self.grayscale_image_json)


class DetectRidgesResponse(ImageBaseResponse):
    processed_image_inverted_json: JsonImage

    @property
    def processed_image_inverted(self) -> NpImage:
        return convert_jsonimg_to_npimg(self.processed_image_inverted_json)


class IsolateRgbResponse(ImageBaseResponse):
    ...


class RecognizeFacesResponse(ImageBaseResponse):
    ...
