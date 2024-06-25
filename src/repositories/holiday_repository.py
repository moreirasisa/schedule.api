from models.holiday import HolidayModel


class HolidayRepository:
    @staticmethod
    async def create(db, holiday: HolidayModel):
        holiday_dictionary = holiday.model_dump(by_alias=True)
        holiday_dictionary["_id"] = str(holiday_dictionary["_id"])
        result = await db['holidays'].insert_one(holiday_dictionary)
        holiday_dictionary['_id'] = str(result.inserted_id)
        return holiday_dictionary
    
    @staticmethod
    async def list_all(db):
        return db['holidays'].find()
    
    @staticmethod
    async def list_by_id(db, id: str):
        return db['holidays'].find_one(id)