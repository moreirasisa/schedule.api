from pydantic import BaseModel


class AppointmentTypeViewModel(BaseModel):
    name: str