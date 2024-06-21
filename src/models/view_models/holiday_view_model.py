from datetime import datetime
from pydantic import BaseModel


class HolidayViewModel(BaseModel):
    name: str
    date: datetime