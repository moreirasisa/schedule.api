from models.appointment_type import AppointmentTypeModel


class AppointmentTypeRepository:
    @staticmethod
    async def create(db, type: AppointmentTypeModel):
        type_dictionary = type.model_dump(by_alias=True)
        type_dictionary["_id"] = str(type_dictionary["_id"])
        result = await db['appointment-types'].insert_one(type_dictionary)
        type_dictionary['_id'] = str(result.inserted_id)
        return type_dictionary
    
    @staticmethod
    async def list_all(db):
        return db['appointment-types'].find()
    
    @staticmethod
    async def list_by_id(db, id: str):
        return db['appointment-types'].find_one(id)
    
    @staticmethod
    async def exists(db, id: str):
        return db['appointment-types'].find_one({"_id": id})