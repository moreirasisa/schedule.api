import os
import uuid
from dotenv import load_dotenv
import pytest
import pytest_asyncio
from motor.motor_asyncio import AsyncIOMotorClient

from models.holiday import HolidayModel
from repositories.holiday_repository import HolidayRepository


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
async def holiday_mock():
    return HolidayModel(
        _id = str(uuid.uuid4()),
        name = 'Holiday Test',
        date = '2024-06-25T16:47:00.187+00:00'
    )
    
@pytest.mark.asyncio
async def test_create_holiday(db, holiday_mock):
    result = await HolidayRepository.create(db, holiday_mock)
    assert '_id' in result
    db_holiday = await db['holidays'].find_one({'_id': result['_id']})
    assert db_holiday is not None
    
@pytest.mark.asyncio
async def test_list_all_holidays(db, holiday_mock):
    holiday_mock = await HolidayRepository.create(db, holiday_mock)
    result = await HolidayRepository.list_all(db)
    holiday_list = [holiday async for holiday in result]
    assert len(holiday_list) == 1
    
@pytest.mark.asyncio
async def test_list_holiday_by_id(db, holiday_mock):
    await HolidayRepository.create(db, holiday_mock)
    result = await HolidayRepository.list_by_id(db, holiday_mock.id)
    result_data = await result
    assert result_data is not None