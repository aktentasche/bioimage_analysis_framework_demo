from pydantic import BaseModel, Field


class DetectRidgesResponse(BaseModel):
    foo: int = Field(..., description="foo")


class IsolateRgbResponse(BaseModel):
    foo: int = Field(..., description="foo")


class RecognizeFacesResponse(BaseModel):
    foo: int = Field(..., description="foo")
