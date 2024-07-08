from datetime import datetime, time
from pydantic import BaseModel


class AppointmentViewModel(BaseModel):
    name: str
    date: datetime
    startTime: str
    endTime: str
    typeId: str
    address: str