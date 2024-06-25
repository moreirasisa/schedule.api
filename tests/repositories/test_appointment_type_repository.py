import os
import uuid
from dotenv import load_dotenv
import pytest
import pytest_asyncio
from motor.motor_asyncio import AsyncIOMotorClient

from models.appointment_type import AppointmentTypeModel
from repositories.appointment_type_repository import AppointmentTypeRepository


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
async def type_mock():
    return AppointmentTypeModel(
        _id = str(uuid.uuid4()),
        name = 'Type Test'
    )
    
@pytest.mark.asyncio
async def test_create_appointment_type(db, type_mock):
    result = await AppointmentTypeRepository.create(db, type_mock)
    assert '_id' in result
    db_type = await db['appointment-types'].find_one({'_id': result['_id']})
    assert db_type is not None
    
@pytest.mark.asyncio
async def test_list_all_types(db, type_mock):
    type_mock = await AppointmentTypeRepository.create(db, type_mock)
    result = await AppointmentTypeRepository.list_all(db)
    type_list = [type async for type in result]
    assert len(type_list) == 1
    
@pytest.mark.asyncio
async def test_list_type_by_id(db, type_mock):
    await AppointmentTypeRepository.create(db, type_mock)
    result = await AppointmentTypeRepository.list_by_id(db, type_mock.id)
    result_data = await result
    assert result_data is not None
    
@pytest.mark.asyncio
async def test_if_type_exists(db, type_mock):
    await AppointmentTypeRepository.create(db, type_mock)
    result = await AppointmentTypeRepository.exists(db, type_mock.id)
    type_found = await db['appointment-types'].find_one({'_id': type_mock.id})
    assert type_found is not None