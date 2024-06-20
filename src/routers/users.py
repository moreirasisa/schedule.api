from typing import List
from fastapi import APIRouter, Request

from models.dtos.users_dto import CreateUserDto, UpdateUserDto
from models.view_models.user_view_model import UserViewModel
from services.user_service import UserService


router = APIRouter()

@router.post("", response_model=UserViewModel)
async def post(user: CreateUserDto, request: Request):
    return await UserService.create(request.app.database, user)

@router.get("", response_model=List[UserViewModel])
async def get(request: Request):
    return await UserService.list_all(request.app.database)

@router.get("/{id}")
async def get(id: str, request: Request):
    return await UserService.list_by_id(request.app.database, id)

@router.put("/{id}", response_model=UserViewModel)
async def put(id: str, user: UpdateUserDto, request: Request):
    return await UserService.update(request.app.database, user, id)

@router.delete("/{id}")
async def delete(id: str, request: Request):
    return await UserService.delete(request.app.database, id)