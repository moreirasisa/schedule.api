from typing import List
from models.dtos.holiday_dto import CreateHolidayDto
from models.holiday import HolidayModel
from models.view_models.holiday_view_model import HolidayViewModel
from repositories.holiday_repository import HolidayRepository


class HolidayService:
    @staticmethod
    async def create(db, holiday_dto: CreateHolidayDto) -> HolidayViewModel:
        holiday_model = HolidayModel(
            name = holiday_dto.name,
            date = holiday_dto.date
        )
        created_holiday = await HolidayRepository.create(db, holiday_model)
        return HolidayViewModel(**created_holiday)
    
    @staticmethod
    async def list_all(db) -> List[HolidayViewModel]:
        holidays_index = await HolidayRepository.list_all(db)
        holidays = []
        for holiday in holidays_index:
            holiday_view_model = HolidayViewModel(**holiday)
            holidays.append(holiday_view_model)
        return holidays
    
    @staticmethod
    async def list_by_id(db, id: str) -> HolidayViewModel:
        return await HolidayRepository.list_by_id(db, id)