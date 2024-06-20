import uuid
from pydantic import BaseModel, Field


class UserModel(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias='_id')
    name: str
    email: str
    password: str
    
class UpdateUserModel(BaseModel):
    name: str
    email: str
    password: str