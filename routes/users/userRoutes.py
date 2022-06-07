from http import HTTPStatus
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from manageUsers import addUser, listUser , updateUser
from login.oauth2 import current_user
from schemas.requestUserSchema import userPydantic,user
from schemas.responseUserSchema import showUser
from marshmallow import Schema, fields, ValidationError
router = APIRouter(
    tags = ['User']
)

@router.post('/user')
def add_user(data: userPydantic,cur_user: showUser = Depends(current_user)):
    try:
        data1 = dict(data)
        user().load(data1)
    except ValidationError as err:
        return err.messages
    return addUser.add_user(data,cur_user)

@router.get('/user',response_model = List[showUser])
def list_user(cur_user: showUser = Depends(current_user)):
    return listUser.list_user(cur_user)

@router.get('/user/{id}',response_model = showUser)
def list_user_id(id: int,cur_user: showUser = Depends(current_user)):
    return listUser.list_user_id(id,cur_user)

@router.put('/user/{id}')
def update_user(id: int,data: userPydantic,cur_user: showUser = Depends(current_user)):
    return updateUser.update_user(id,data,cur_user)