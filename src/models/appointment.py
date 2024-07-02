from datetime import datetime
from typing import Optional
import uuid
from pydantic import BaseModel, Field


class AppointmentModel(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias='_id')
    name: str
    date: datetime
    startTime: datetime
    endTime: datetime
    typeId: str
    address: str
    
class UpdateAppointmentModel(BaseModel):
    name: Optional[str] = None
    date: Optional[datetime] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    typeId: Optional[str] = None
    address: Optional[str] = None