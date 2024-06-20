from models.users import UserModel


class UserRepository:
    @staticmethod
    async def create(db, user: UserModel):
        user_dictionary = user.dict(by_alias=True)
        user_dictionary["_id"] = str(user_dictionary["_id"])
        result = db['users'].insert_one(user_dictionary)
        user_dictionary['_id'] = str(result.inserted_id)
        return user_dictionary
    
    @staticmethod
    async def list_all(db):
        return db['users'].find()
    
    @staticmethod
    async def list_by_id(db, id: str):
        return db['users'].find_onde(id)
    
    @staticmethod
    async def update(db, user: UserModel, id: str):
        update_user = {k: v for k, v in user.dict(exclude_unset=True).items()}
        db['users'].update_one({"_id": id}, {"$set": update_user})
        user_to_update = db['users'].find_one({"_id": id})
        user_to_update["_id"] = str(user_to_update["_id"])
        return user_to_update
    
    @staticmethod
    async def delete(db, id: str):
        result = db['users'].delete_one({"_id": id})
        return result.deleted_count > 0