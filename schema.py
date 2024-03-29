from pydantic import BaseModel
from typing import Optional


class Record(BaseModel):
    informant: str
    location_lat: Optional[float]
    location_long: Optional[float]
    img_link: Optional[str]


class Camera(BaseModel):
    camera_id: str
    location_lat: float
    location_long: float
