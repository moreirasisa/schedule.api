from datetime import datetime, time
from pydantic import BaseModel


class CreateAppointmentDto(BaseModel):
    name: str
    date: datetime
    startTime: time
    endTime: time
    typeId: str
    userId: str
    address: str

class UpdateAppointmentDto(BaseModel):
    name: str
    date: datetime
    startTime: time
    endTime: time
    typeId: str
    userId: str
    address: str