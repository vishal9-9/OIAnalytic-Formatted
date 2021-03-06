from fastapi import FastAPI
from routes.login import login
from routes.users import userRoutes
# from routes.company import companyRoutes
from database import databaseHelper
app = FastAPI()

@app.get('/')
def index():
    return 'Hello'

app.include_router(login.router)
app.include_router(userRoutes.router)
# app.include_router(companyRoutes.router)
