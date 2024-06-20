import datetime
from pydantic import BaseModel


class CreateHolidayDto(BaseModel):
    name: str
    date: datetime