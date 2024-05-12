from typing import Union
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from dotenv import load_dotenv
import os
import db_tools


from pydantic import BaseModel


description = """
# API ООО 'Здоровье'

## Аптеки

Вы можете:
* **Добавить аптеку** (_not implemented_).
* **Получить список всех аптеки** (_not implemented_).
* **Удалить аптеку** (_not implemented_).
* **Обновить данные об апетки** (_not implemented_).
"""
tags_metadata = [
    {
        "name": "Аптеки",
        "description": "Операции связанные с аптеками."
    },
    {
        "name": "Поставщики",
        "description":"Операции связанные с поставщиками."
    },
    {
        "name": "Склады",
        "description": "Операции связанные со складами."
    },
    {
        "name": "Медикаменты",
        "description": "Опреации связанные с медикаментами."
    }
]


load_dotenv()
print(os.getenv("SECRET_KEY"), [os.getenv("ALGORITHM")])

fake_db = {
    
    "test":{
        "username": "test",
        "full_name": "test_f_name",
        "email": "test_email",
        "role": "test_role",
        "hashed_password": "$2b$12$Zl0xzFl/Cjen1GKx1VilWOTV6hf1Gc9UsBhhZ5bsZqSoQdJOEi0om",
        "disabled": False
    }
}

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username : str | None = None
    role: str | None = None

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    role: str
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated=["auto"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI(
    title="ООО 'Здоровье' API",
    summary="API для реализации работы системы учетов складов аптек",
    description=description,
    version="0.0.1",
    openapi_tags=tags_metadata
    )


#функции под тестовую авторизацию

#функция потверждения пароля, сравнение пароля и его хеша
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

#превращение пароля который ввел пользователь в хеш пароля
def get_password_hash(password: str):
    return pwd_context.hash(password)

#получения пользователя из базы данных
def get_user(db, username: str):
    if username in db:
        user_data = db[username]
        return UserInDB(**user_data)
    
#авторизация пользователя
def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)

    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


#создание токена для доступа access token
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expier = datetime.now() + expires_delta
    else:
        expier = datetime.now() + timedelta(minutes=15)

    to_encode.update({
        "exp": expier
    })

    encoded_jwt = jwt.encode(
        to_encode, 
        os.getenv("SECRET_KEY"), 
        algorithm=os.getenv("ALGORITHM")
    )

    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={
            "WWW-Authenticate": "Bearer"
        }
        )
    
    try:
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=[os.getenv("ALGORITHM")])
        username: str = payload.get("sub")
        if username is None:
            raise credential_exception
        
        token_data = TokenData(username=username)

    except JWTError:
        raise credential_exception
    
    user = get_user(fake_db, username=token_data.username)

    if user is None:
        raise credential_exception
    
    return user


async def get_current_active_user(current_user: UserInDB = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    
    return current_user


#token root
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Inccorect user name or password",
            headers={
                "WWW-Authenticate": "Bearer"
            }
            )
    
    access_token_expires = timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")))
    access_token = create_access_token(data={
        "sub": user.username
    },
    expires_delta=access_token_expires
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@app.get("/users/me/items")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [
        {
            "item_id": 1,
            "owner": current_user
        }
    ]


#добавление аптеки в базу данных
@app.post("/pharmacy", tags=["Аптеки"])
def add_pharmacy(pharmacy: db_tools.Pharmacy) -> str:
    db_tools.addPharmacy(pharmacy=pharmacy)
    return f"pharmasy on {pharmacy.ph_address} id add"


#получение всех аптек
@app.get("/pharmacy", tags=["Аптеки"])
def get_all_pharmacy() -> dict:
    return {
        "pharmacys" : db_tools.getAllPharmacy()
    }

#удаление аптеки по её id
@app.delete("/pharmacy/{ph_id}", tags=["Аптеки"])
def delete_Pharmacy(ph_id: int ) -> str:
    db_tools.deletePharmacy(ph_id)
    return f"pharmasy with ph_id = {ph_id} is deleted"


#обновление данных об аптеке
@app.put("/pharmacy/{ph_id}", tags=["Аптеки"])
def update_pharmacy(pharmacy: db_tools.Pharmacy) -> str:
    db_tools.updatePharmacy(pharmacy=pharmacy)
    return f"pharmacy with ph_id = {pharmacy.ph_id} is updated"


#добавления поставщика в базу данных
@app.post("/supplier", tags=["Поставщики"])
def add_supplier(supplier: db_tools.Supplier) -> str:
    db_tools.addSupplier(supplier=supplier)
    return f"supplier {supplier.s_name} is add"

#получение всех поставщиков
@app.get("/supplier", tags=["Поставщики"])
def get_all_supplier() -> dict:
    return {
        "suppliers": db_tools.allSupplier()
    }

#удаление поставщика
@app.delete("/supplier/{s_id}", tags=["Поставщики"])
def delete_supplier(s_id: int) -> str:
    db_tools.deleteSupplier(s_id=s_id)
    return f"supplier with s_id = {s_id} is deleted"


#обновление данных о поставщике
@app.put("/supplier/{s_id}", tags=["Поставщики"])
def update_supplier(supplier:db_tools.Supplier) -> str:
    db_tools.updateSupplier(supplier=supplier)
    return f"supplier with s_id = {supplier.s_id} is updated"


#добавление склада в базу данных
@app.post("/warehouse", tags=["Склады"])
def add_warehouse(warehouse:db_tools.Warehouse) -> str:
    db_tools.addWarehouse(warehouse=warehouse)
    return f"warehouse on {warehouse.w_address} is added"

#получение всех складов
@app.get("/warehouse", tags=["Склады"])
def get_all_warehouse() -> dict:
    return {
        "warehouse": db_tools.allWarehouse()
    }

#удаление склада
@app.delete("/warehouse/{w_id}", tags=["Склады"])
def delete_warehouse(w_id:int) -> str:
    db_tools.deleteWarehouse(w_id)
    return f"warehouse with w_id = {w_id} is deleted"

#обновление данных о складе
@app.put("/warehouse/{w_id}", tags=["Склады"])
def update_warehouse(warehouse:db_tools.Warehouse) -> str:
    db_tools.updateWarehouse(warehouse=warehouse)
    return f"warehouse with w_id = {warehouse.w_id} is updated"


#добавление медикаментов в базу данных
@app.post("/medication", tags=["Медикаменты"])
def add_medication(medication:db_tools.Medication) -> str:
    db_tools.addMedication(medication)
    return f"medication with name {medication.med_name} is add"


#получение всех медикаментов
@app.get("/medication", tags=["Медикаменты"])
def get_all_medication() -> dict:
    return {
        "medication": db_tools.allMedication()
    }

#удаление медикамента  из базы данных
@app.delete("/medication/{med_id}", tags=["Медикаменты"])
def delete_medication(med_id : int) -> str:
    db_tools.deleteMedication(med_id)
    return f"medications with med_id = {med_id} is deleted"

#обновления информации о медикаменте
@app.put("/medication/{med_id}", tags=["Медикаменты"])
def update_medication(medication:db_tools.Medication) -> str:
    db_tools.updateMedication(medication)
    return f"medication with med_id = {medication.med_id} is updated"