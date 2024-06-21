from datetime import datetime, time
import uuid
from pydantic import BaseModel, Field


class AppointmentModel(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias='_id')
    name: str
    date: datetime
    startTime: time
    endTime: time
    typeId: str
    userId: str
    address: str
    
class UpdateAppointmentModel(BaseModel):
    name: str
    date: datetime
    startTime: time
    endTime: time
    typeId: str
    userId: str
    address: str