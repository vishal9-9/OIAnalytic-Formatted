from datetime import date
from marshmallow import Schema,fields
from pydantic import BaseModel

class userPydantic(BaseModel):
    c_id: int
    fullname: str
    email: str
    password: str
    contact_no: str
    working_under: int
    dob: date
    role_id: int

class user(Schema):
    c_id = fields.Integer(required = True)
    fullname = fields.String(required = True)
    email = fields.Email(required = True)
    password = fields.String(required = True)
    contact_no = fields.String(required = True)
    working_under = fields.Integer(required = True)
    dob = fields.Date(required = True)
    role_id = fields.Integer(required = True)
