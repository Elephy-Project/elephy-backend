from xmlrpc.client import DateTime
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID, uuid4
from typing import Optional


class Record(BaseModel):
    id: Optional[UUID]
    datetime: Optional[datetime]
    informant: str
    elephantname: str
    location: str


class CameraRecord(BaseModel):
    id: Optional[UUID]
    datetime: Optional[datetime]
    cameraid: str
    elephantname: str
    location: str
