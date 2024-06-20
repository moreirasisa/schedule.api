from typing import List
from models.dtos.users_dto import CreateUserDto, UpdateUserDto
from models.users import UpdateUserModel, UserModel
from models.view_models.user_view_model import UserViewModel
from repositories.user_repository import UserRepository


class UserService:
    @staticmethod
    async def create(db, user_dto: CreateUserDto) -> UserViewModel:
        user_model = UserModel(
            name = user_dto.name,
            email = user_dto.email,
            password = user_dto.password
        )
        created_user = await UserRepository.create(db, user_model)
        return UserViewModel(**created_user)
    
    @staticmethod
    async def list_all(db) -> List[UserViewModel]:
        users_index = await UserRepository.list_all(db)
        users = []
        for user in users_index:
            user_view_model = UserViewModel(**user)
            users.append(user_view_model)
        return users
    
    @staticmethod
    async def list_by_id(db, id: str) -> UserViewModel:
        return await UserRepository.list_by_id(db, id)
    
    @staticmethod
    async def update(db, user_dto: UpdateUserDto, id: str) -> UserViewModel:
        update_user_model = UpdateUserModel(
            name = user_dto.name,
            email = user_dto.email,
            password = user_dto.password
        )
        updated_user = await UserRepository.update(db, update_user_model, id)
        return UserViewModel(**updated_user)
    
    @staticmethod
    async def delete(db, id: str) -> bool:
        deleted_user = await UserRepository.delete(db, id)
        return deleted_user