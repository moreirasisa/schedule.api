from datetime import datetime
import os
import uuid
from dotenv import load_dotenv
import pytest
import pytest_asyncio
from motor.motor_asyncio import AsyncIOMotorClient

from models.appointment import AppointmentModel, UpdateAppointmentModel
from repositories.appointment_repository import AppointmentRepository


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
async def appointment_mock():
    return AppointmentModel(
        _id = str(uuid.uuid4()),
        name = 'Appointment Test',
        date = '2024-06-25T16:47:00.187+00:00',
        startTime = '2024-06-25T16:47:00.187+00:00',
        endTime = '2024-06-25T17:47:00.187+00:00',
        typeId = '3fa85f64-5717-4562-b3fc-2c963f66afa6',
        userId = '3fa85f64-5717-4562-b3fc-2c963f66afa6',
        address = 'Address Test'
    )

@pytest.mark.asyncio
async def test_create_appointment(db, appointment_mock):
    result = await AppointmentRepository.create(db, appointment_mock)
    assert '_id' in result
    db_appointment = await db['appointments'].find_one({'_id': result['_id']})
    assert db_appointment is not None
    
@pytest.mark.asyncio
async def test_list_all_appointments(db, appointment_mock):
    appointment_mock = await AppointmentRepository.create(db, appointment_mock)
    result = await AppointmentRepository.list_all(db)
    appointment_list = [appointment async for appointment in result]
    assert len(appointment_list) == 1
    
@pytest.mark.asyncio
async def test_list_by_appointment_id(db, appointment_mock):
    await AppointmentRepository.create(db, appointment_mock)
    result = await AppointmentRepository.list_by_id(db, appointment_mock.id)
    result_data = await result
    assert result_data is not None
    
@pytest.mark.asyncio
async def test_update_appointment(db, appointment_mock):
    await AppointmentRepository.create(db, appointment_mock)
    update_data = UpdateAppointmentModel(name='Updated Name', date=datetime.fromisoformat('2024-06-26T16:47:00.187+00:00'), address='Updated Address')
    updated_appointment = await AppointmentRepository.update(db, update_data, appointment_mock.id)
    assert updated_appointment is not None
    
@pytest.mark.asyncio
async def test_delete_appointment(db, appointment_mock):
    await AppointmentRepository.create(db, appointment_mock)
    deleted = await AppointmentRepository.delete(db, appointment_mock.id)
    assert deleted is True
    deleted_appointment = await db['appointments'].find_one({'_id': appointment_mock.id})
    assert deleted_appointment is None