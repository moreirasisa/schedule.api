import datetime
import uuid
from pydantic import BaseModel, Field


class HolidayModel(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias='_id')
    name: str
    date: datetime