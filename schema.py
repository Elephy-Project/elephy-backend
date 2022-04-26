from pydantic import BaseModel
from datetime import datetime
from uuid import UUID, uuid4
from typing import Optional


class Record(BaseModel):
    id: Optional[UUID] = uuid4()
    datetime: datetime
    informant: str
    elephant_name: str
    location: str


class CameraRecord(BaseModel):
    id: Optional[UUID] = uuid4()
    datetime: datetime
    camera_id: int
    elephant_name: str
    location: str
