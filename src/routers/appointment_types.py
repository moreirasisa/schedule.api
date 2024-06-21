from typing import List
from fastapi import APIRouter, Request

from models.dtos.appointment_type_dto import CreateAppointmentTypeDto
from models.view_models.appointment_type_view_model import AppointmentTypeViewModel
from services.appointment_type_service import AppointmentTypeService


router = APIRouter()

@router.post("", response_model=AppointmentTypeViewModel)
async def post(type: CreateAppointmentTypeDto, request: Request):
    return await AppointmentTypeService.create(request.app.database, type)

@router.get("", response_model=List[AppointmentTypeViewModel])
async def get(request: Request):
    return await AppointmentTypeService.list_all(request.app.database)

@router.get("/{id}")
async def get(id: str, request: Request):
    return await AppointmentTypeService.list_by_id(request.app.database, id)