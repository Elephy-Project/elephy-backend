from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from typing import Optional


class Record(BaseModel):
    id: Optional[UUID]
    datetime: Optional[datetime]
    informant: str
    elephant_name: str
    location: str


class CameraRecord(BaseModel):
    id: Optional[UUID]
    datetime: Optional[datetime]
    camera_id: str
    elephant_name: str
    location: str
    # picture?
