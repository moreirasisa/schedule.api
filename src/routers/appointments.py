from typing import List
from fastapi import APIRouter, Request

from models.dtos.appointment_dto import CreateAppointmentDto, UpdateAppointmentDto
from models.view_models.appointment_view_model import AppointmentViewModel
from services.appointment_service import AppointmentService


router = APIRouter()

@router.post("", response_model=AppointmentViewModel)
async def post(appointment: CreateAppointmentDto, request: Request):
    return await AppointmentService.create(request.app.database, appointment)

@router.get("", response_model=List[AppointmentViewModel])
async def get(request: Request):
    return await AppointmentService.list_all(request.app.database)

@router.get("/{id}")
async def get(id: str, request: Request):
    return await AppointmentService.list_by_id(request.app.database, id)

@router.put("/{id}", response_model=AppointmentViewModel)
async def put(id: str, appointment: UpdateAppointmentDto, request: Request):
    return await AppointmentService.update(request.app.database, appointment, id)

@router.delete("/{id}")
async def delete(id: str, request: Request):
    return await AppointmentService.delete(request.app.database, id)