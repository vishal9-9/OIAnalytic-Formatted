from database import databaseHelper
from helpers import passhash,tokens
from fastapi import HTTPException,Depends
from http import HTTPStatus
from fastapi.security import OAuth2PasswordRequestForm

def login_user(request: OAuth2PasswordRequestForm = Depends()):
    user = databaseHelper.if_user_exist(request.username)
    if user is None:
        raise HTTPException(status_code = HTTPStatus.UNAUTHORIZED)
    if not user.isactive == 1:
        raise HTTPException(status_code = HTTPStatus.FORBIDDEN)
    psswd = request.password
    password = passhash.check_hash(psswd,user.password)
    if not password:
        raise HTTPException(status_code = HTTPStatus.UNAUTHORIZED)
    access_token = tokens.create_access_token(data = {'sub': user.email})
    return {"access_token" : access_token , "token_type": "bearer"}