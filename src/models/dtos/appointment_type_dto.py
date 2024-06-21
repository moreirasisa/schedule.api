from pydantic import BaseModel


class CreateAppointmentTypeDto(BaseModel):
    name: str