from datetime import datetime, time
from typing import Optional
from pydantic import BaseModel


class CreateAppointmentDto(BaseModel):
    name: str
    date: datetime
    startTime: str
    endTime: str
    typeId: str
    address: str

class UpdateAppointmentDto(BaseModel):
    name: Optional[str] = None
    date: Optional[datetime] = None
    startTime: Optional[str] = None
    endTime: Optional[str] = None
    typeId: Optional[str] = None
    address: Optional[str] = None