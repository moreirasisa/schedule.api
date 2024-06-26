from datetime import datetime, time
from pydantic import BaseModel


class AppointmentViewModel(BaseModel):
    name: str
    date: datetime
    startTime: datetime
    endTime: datetime
    typeId: str
    userId: str
    address: str