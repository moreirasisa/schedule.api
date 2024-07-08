from datetime import datetime, time
from typing import Optional
import uuid
from pydantic import BaseModel, Field


class AppointmentModel(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias='_id')
    name: str
    date: datetime
    startTime: str
    endTime: str
    typeId: str
    address: str
    
class UpdateAppointmentModel(BaseModel):
    name: Optional[str] = None
    date: Optional[datetime] = None
    startTime: Optional[str] = None
    endTime: Optional[str] = None
    typeId: Optional[str] = None
    address: Optional[str] = None