from typing import List
from fastapi import APIRouter, Request

from models.dtos.holiday_dto import CreateHolidayDto
from models.view_models.holiday_view_model import HolidayViewModel
from services.holiday_service import HolidayService


router = APIRouter()

@router.post("", response_model=HolidayViewModel)
async def post(holiday: CreateHolidayDto, request: Request):
    return await HolidayService.create(request.app.database, holiday)

@router.get("", response_model=List[HolidayViewModel])
async def get(request: Request):
    return await HolidayService.list_all(request.app.database)