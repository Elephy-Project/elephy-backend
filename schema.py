from pydantic import BaseModel


class Record(BaseModel):
    informant: str
    location_lat: float
    location_long: float


class Camera(BaseModel):
    camera_id: str
    location_lat: float
    location_long: float
