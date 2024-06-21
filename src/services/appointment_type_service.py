from typing import List
from models.appointment_type import AppointmentTypeModel
from models.dtos.appointment_type_dto import CreateAppointmentTypeDto
from models.view_models.appointment_type_view_model import AppointmentTypeViewModel
from repositories.appointment_type_repository import AppointmentTypeRepository


class AppointmentTypeService:
    @staticmethod
    async def create(db, type_dto: CreateAppointmentTypeDto) -> AppointmentTypeViewModel:
        type_model = AppointmentTypeModel(
            name = type_dto.name
        )
        created_type = await AppointmentTypeRepository.create(db, type_model)
        return AppointmentTypeViewModel(**created_type)
    
    @staticmethod
    async def list_all(db) -> List[AppointmentTypeViewModel]:
        types_index = await AppointmentTypeRepository.list_all(db)
        types = []
        for type in types_index:
            type_view_model = AppointmentTypeViewModel(**type)
            types.append(type_view_model)
        return types
    
    @staticmethod
    async def list_by_id(db, id: str) -> AppointmentTypeViewModel:
        return await AppointmentTypeRepository.list_by_id(db, id)