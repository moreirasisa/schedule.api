import os
import uuid
from dotenv import load_dotenv
import pytest
import pytest_asyncio
from motor.motor_asyncio import AsyncIOMotorClient

from models.users import UpdateUserModel, UserModel
from repositories.user_repository import UserRepository


load_dotenv()

@pytest_asyncio.fixture
async def db():
    db_uri = os.getenv('MONGODB_CONNECTION_URI')
    if not db_uri: raise ValueError("Connection string could not be found")
    client = AsyncIOMotorClient(db_uri)
    db = client['test_database']
    yield db
    await client.drop_database('test_database')
    client.close()
    
@pytest_asyncio.fixture
async def user_mock():
    return UserModel(
        _id = str(uuid.uuid4()),
        name = 'User Test',
        email = 'usertest@example.com',
        password = 'password123'
    )
    
@pytest.mark.asyncio
async def test_create_user(db, user_mock):
    result = await UserRepository.create(db, user_mock)
    assert '_id' in result
    db_user = await db['users'].find_one({'_id': result['_id']})
    assert db_user is not None
    
@pytest.mark.asyncio
async def test_list_all_users(db, user_mock):
    user_mock = await UserRepository.create(db, user_mock)
    result = await UserRepository.list_all(db)
    user_list = [user async for user in result]
    assert len(user_list) == 1
    
@pytest.mark.asyncio
async def test_list_user_by_id(db, user_mock):
    await UserRepository.create(db, user_mock)
    result = await UserRepository.list_by_id(db, user_mock.id)
    result_data = await result
    assert result_data is not None
    
@pytest.mark.asyncio
async def test_update_user(db, user_mock):
    await UserRepository.create(db, user_mock)
    update_data = UpdateUserModel(name='Updated User', email='updated@example.com', password="updatedPassword")
    updated_user = await UserRepository.update(db, update_data, user_mock.id)
    assert updated_user is not None
    assert updated_user['_id'] == user_mock.id
    assert updated_user['name'] == 'Updated User'
    assert updated_user['email'] == 'updated@example.com'
    assert updated_user['password'] == 'updatedPassword'

@pytest.mark.asyncio
async def test_delete_user(db, user_mock):
    await UserRepository.create(db, user_mock)
    deleted = await UserRepository.delete(db, user_mock.id)
    assert deleted is True
    deleted_user = await db['users'].find_one({"_id": user_mock.id})
    assert deleted_user is None