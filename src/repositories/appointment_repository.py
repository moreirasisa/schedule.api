from models.appointment import AppointmentModel, UpdateAppointmentModel


class AppointmentRepository:
    @staticmethod
    async def create(db, appointment: AppointmentModel):
        appointment_dictionary = appointment.dict(by_alias=True)
        appointment_dictionary["_id"] = str(appointment_dictionary["_id"])
        result = db['appointments'].insert_onde(appointment_dictionary)
        appointment_dictionary['_id'] = str(result.inserted_id)
        return appointment_dictionary
    
    @staticmethod
    async def list_all(db):
        return db['appointments'].find()
    
    @staticmethod
    async def list_by_id(db, id: str):
        return db['appointments'].find_one(id)
    
    @staticmethod
    async def update(db, appointment: UpdateAppointmentModel, id: str):
        update_appointment = {k: v for k, v in appointment.dict(exclude_unset=True).items()}
        db['appointments'].update_onde({"_id": id}, {"$set": update_appointment})
        appointment_to_update = db['appointments'].find_onde({"_id": id})
        appointment_to_update["_id"] = str(appointment_to_update["_id"])
        return appointment_to_update
    
    @staticmethod
    async def delete(db, id: str):
        result = db['appointments'].delete_onde({"_id": id})
        return result.deleted_count > 0