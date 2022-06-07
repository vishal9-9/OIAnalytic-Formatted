from fastapi import APIRouter

router = APIRouter(
    tags = ['Company']
)

@router.post('/company')
def add_new_company():
    return 'add new company'