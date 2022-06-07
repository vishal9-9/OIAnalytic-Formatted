from pyexpat import model
from database.engine import session
import datetime
import bcrypt
from models import models
from config import logError
from helpers import passhash

db = session

def if_user_exist(email: str):
    is_exist = db.query(models.Users).filter(models.Users.email == email).first()
    return is_exist

def role_power(user_id: int):
    query = f'SELECT role_power FROM role INNER JOIN users on role.role_id = users.role_id where id = {user_id}'
    res = db.execute(query)
    roles = res.fetchall()
    if roles != []:
        for x in roles:
            return x[0]
    else:
        return logError.NO_USER_WITH_THAT_ID_ERROR

def list_of_cid():
    companyid = db.query(models.Company).with_entities(models.Company.company_id)
    id_list = []
    for company_id in companyid:
        id_list.append(company_id[0])
    return id_list

def add_new_user(user_schema):
    salt = bcrypt.gensalt()
    password = user_schema.password
    new_user = models.Users(c_id = user_schema.c_id,fullname = user_schema.fullname,email = user_schema.email,password = passhash.genrate_hash_password(password.encode('utf-8'),salt),salt = salt,contact_no = user_schema.contact_no, working_under = user_schema.working_under, dob = user_schema.dob, isactive = 1 , role_id = user_schema.role_id,created_at = datetime.datetime.now())
    db.add(new_user)
    db.commit()
    db.close()

def update_user(user_schema,id: int):
    query = f'UPDATE users SET c_id = {user_schema.c_id}, fullname = "{user_schema.fullname}", email = "{user_schema.email}", contact_no = "{user_schema.contact_no}", working_under = {user_schema.working_under}, dob = "{user_schema.dob}", role_id = {user_schema.role_id}, updated_at = "{datetime.datetime.now()}"  where id = {id}'
    res = db.execute(query)
    db.commit()
    db.close()

def list_all_user():
    return db.query(models.Users).all()

def list_user_admin(cur_user):
    query = f"SELECT * FROM users WHERE role_id != 0 AND c_id = {cur_user.c_id}"
    return db.execute(query).fetchall()

def list_user_supervisor(cur_user):
    query = f"SELECT * FROM users WHERE role_id != 0 AND role_id != 1 AND c_id = {cur_user.c_id}"
    return db.execute(query).fetchall()

def list_user_id(id: int):
    return db.query(models.Users).get(id)

def list_user_id_admin(id: int,cur_user):
    query = f"SELECT * FROM users WHERE id = {id} AND role_id != 0 AND c_id = {cur_user.c_id}"
    return db.execute(query).fetchone()

def list_user_id_supervisor(id: int,cur_user):
    query = f"SELECT * FROM users WHERE id = {id} AND role_id != 0 AND role_id != 1 AND c_id = {cur_user.c_id}"
    return db.execute(query).fetchone()

def update_email_check(id: int):
    query = f"SELECT email FROM users WHERE id != '{id}'"
    return db.execute(query).fetchall()