import os
from unittest.mock import AsyncMock
import pytest
import pytest_asyncio
from motor.motor_asyncio import AsyncIOMotorClient

from models.dtos.users_dto import CreateUserDto
from models.users import UserModel
from models.view_models.user_view_model import UserViewModel
from repositories.user_repository import UserRepository
from services.user_service import UserService

@pytest_asyncio.fixture
async def db_mock():
    db_uri = os.getenv('MONGODB_CONNECTION_URI')
    if not db_uri: raise ValueError("Connection string could not be found")
    client = AsyncIOMotorClient(db_uri)
    db = client['test_database']
    yield db
    await client.drop_database('test_database')
    client.close()

@pytest_asyncio.fixture
async def user_mock():
    return CreateUserDto(
        name = "User Test",
        email = "test@gmail.com",
        password = "passoword123"
    )

@pytest.mark.asyncio
async def test_create_user(db_mock, user_mock):
    created_user_mock = UserModel(
        name=user_mock.name,
        email=user_mock.email,
        password=user_mock.password
    )
    UserRepository.create = AsyncMock(return_value = created_user_mock)
    created_user = await UserService.create(db_mock, user_mock)
    user_view_model_dict = {
        'name': created_user.name,
        'email': created_user.email,
        'password': created_user.password
    }
    created_user_view_model = UserViewModel(**user_view_model_dict)
    assert isinstance(created_user_view_model, UserViewModel)
    UserRepository.create.assert_called_once_with(db_mock, created_user_mock)