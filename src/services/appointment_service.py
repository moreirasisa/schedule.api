from typing import List
from exceptions.appointment_type_exceptions import AppointmentNotFoundException
from models.appointment import AppointmentModel, UpdateAppointmentModel
from models.dtos.appointment_dto import CreateAppointmentDto, UpdateAppointmentDto
from models.view_models.appointment_view_model import AppointmentViewModel
from repositories.appointment_repository import AppointmentRepository
from repositories.appointment_type_repository import AppointmentTypeRepository


class AppointmentService:
    @staticmethod
    async def create(db, appointment_dto: CreateAppointmentDto) -> AppointmentViewModel:
        if not await AppointmentTypeRepository.exists(db, appointment_dto.typeId):
            raise AppointmentNotFoundException()
        
        appointment_model = AppointmentModel(
            name = appointment_dto.name,
            date = appointment_dto.date,
            startTime = appointment_dto.startTime,
            endTime = appointment_dto.endTime,
            typeId = appointment_dto.typeId,
            userId = appointment_dto.userId,
            address = appointment_dto.address
        )
        created_appointment = await AppointmentRepository.create(db, appointment_model)
        return AppointmentViewModel(**created_appointment)
    
    @staticmethod
    async def list_all(db) -> List[AppointmentViewModel]:
        appointments_index  = await AppointmentRepository.list_all(db)
        appointments = []
        for appointment in appointments_index:
            appointment_view_model = AppointmentViewModel(**appointment)
            appointments.append(appointment_view_model)
        return appointments
    
    @staticmethod
    async def list_by_id(db, id: str) -> AppointmentViewModel:
        return await AppointmentRepository.list_by_id(db, id)
    
    @staticmethod
    async def update(db, appointment_dto: UpdateAppointmentDto, id: str) -> AppointmentViewModel:
        update_appointment_model = UpdateAppointmentModel(
            name = appointment_dto.name,
            date = appointment_dto.date,
            startTime = appointment_dto.startTime,
            endTime = appointment_dto.endTime,
            typeId = appointment_dto.typeId,
            address = appointment_dto.address
        )
        updated_appointment = await AppointmentRepository.update(db, update_appointment_model, id)
        return AppointmentViewModel(**updated_appointment)
    
    @staticmethod
    async def delete(db, id: str) -> bool:
        deleted_appointment = await AppointmentRepository.delete(db, id)
        return deleted_appointment