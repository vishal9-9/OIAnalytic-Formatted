from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from login import login

router = APIRouter(
    tags = ['Login']
)

@router.post('/login')
def auth(request: OAuth2PasswordRequestForm = Depends()):
    return login.login_user(request)