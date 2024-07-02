from datetime import datetime, time
from typing import Optional
from pydantic import BaseModel


class CreateAppointmentDto(BaseModel):
    name: str
    date: datetime
    startTime: datetime
    endTime: datetime
    typeId: str
    address: str

class UpdateAppointmentDto(BaseModel):
    name: Optional[str] = None
    date: Optional[datetime] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    typeId: Optional[str] = None
    address: Optional[str] = None