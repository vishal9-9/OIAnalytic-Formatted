from database import databaseHelper
from http import HTTPStatus
from fastapi import HTTPException

def list_user(cur_user):
    role = databaseHelper.role_power(cur_user.id)
    if role == 'Superadmin':
        return databaseHelper.list_all_user()
    elif role == 'Admin':
        return databaseHelper.list_user_admin(cur_user)
    elif role == 'Supervisor':
        return databaseHelper.list_user_supervisor(cur_user)

def list_user_id(id: int,cur_user):
    role = databaseHelper.role_power(cur_user.id)
    user = databaseHelper.list_user_id(id)
    if user:
        if role == 'Superadmin':
            return user
        elif role == 'Admin':
            return databaseHelper.list_user_admin(cur_user)
        elif role == 'Supervisor':
            return databaseHelper.list_user_admin(cur_user)
        else:
            raise HTTPException(HTTPStatus.UNAUTHORIZED)
    else:
        raise HTTPException(status_code = HTTPStatus.NOT_FOUND)