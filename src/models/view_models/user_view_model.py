from pydantic import BaseModel


class UserViewModel(BaseModel):
    name: str
    email: str
    password: str