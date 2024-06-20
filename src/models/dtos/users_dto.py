from pydantic import BaseModel


class CreateUserDto(BaseModel):
    name: str
    email: str
    password: str
    
class UpdateUserDto(BaseModel):
    name: str
    email: str
    password: str