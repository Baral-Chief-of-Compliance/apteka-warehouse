from typing import Union
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from dotenv import load_dotenv
import os
import db_tools
from fastapi.middleware.cors import CORSMiddleware #для настройки CORS


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
        "name": "Медикаменты на складе",
        "description": "Операции связанные с медикаментами на складе."
    },
    {
        "name": "Медикаменты",
        "description": "Опреации связанные с медикаментами."
    },
    {
        "name": "Заказы",
        "description": "Опреации связанные с заказами."
    },
    {
        "name": "Медикаменты в заказе",
        "description": "Опреации связанные с медикаментами в заказе."
    }
]


load_dotenv()

fake_db = {
    
    "test":{
        "username": "test",
        "full_name": "test_f_name",
        "email": "test_email",
        "role": "test_role",
        "hashed_password": "$2b$12$Zl0xzFl/Cjen1GKx1VilWOTV6hf1Gc9UsBhhZ5bsZqSoQdJOEi0om",
        "disabled": False
    },


    "admin":{
        "username": "admin",
        "full_name": "admin",
        "email": "emailadmin",
        "role": "admin",
        "hashed_password": "$2b$12$UKZBy4PmkMf7f4ots6XbeO7zl9HUxV6Y6AUyimgcjybdDiXkdSszy",
        "disabled": False
    },

    "warehouse_manager":{
        "username": "warehouse_manager",
        "full_name": "warehouse_manager",
        "email": "warehouse_manager",
        "role": "руководитель склада",
        "hashed_password": "$2b$12$0AXPOfMXPRo1fV.AYfc06OP83pV0x0PhdAEOEYlnbT/9p0jQKS0cG",
        "disabled": False
    },
    "ph_manager":{
        "username": "ph_manager",
        "full_name": "ph_manager",
        "email": "ph_manager",
        "role": "директор аптечного склада",
        "hashed_password": "$2b$12$qx8DiHxiK4LNu/nv6QGccOw8a9sJBRZ6JMuHVz6Oilz3SJV9OMsTC",
        "disabled": False
    },

    "worker":{
        "username": "worker",
        "full_name": "worker",
        "email": "worker",
        "role": "работник",
        "hashed_password": "$2b$12$kXGMlZ3Gfd8AzQKRY7E1VO.AJLRrSMrwx1/zSZM.mzaY3ulsbOgg.",
        "disabled": False
    },

    
}



class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username : str or None = None
    role: str or None = None

class User(BaseModel):
    username: str
    email: str or None = None
    full_name: str or None = None
    role: str
    disabled: bool or None = None


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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
def create_access_token(data: dict, expires_delta: timedelta or None = None):
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


print(get_password_hash("admin_pwd"))
print(get_password_hash("warehouse_manager_pwd"))
print(get_password_hash("ph_manager_pwd"))
print(get_password_hash("worker_pwd"))


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
        "token_type": "bearer",
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
def get_all_pharmacy(current_user: User = Depends(get_current_active_user)) -> dict:
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
def get_all_supplier(current_user: User = Depends(get_current_active_user)) -> dict:
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


@app.get('/warehouse/{w_id}', tags=["Склады"])
def getInfoAboutWarehouse(w_id:int, current_user: User = Depends(get_current_active_user)) -> dict:
    return {
        'warehouse_info': db_tools.getWarehouse(w_id),
        'medications':db_tools.getMedicationFromWareHouse(w_id),
    }

#получение всех складов
@app.get("/warehouse", tags=["Склады"])
def get_all_warehouse(current_user: User = Depends(get_current_active_user)) -> dict:
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
def get_all_medication(current_user: User = Depends(get_current_active_user)) -> dict:
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

#добавление медикамента на склад
@app.post("/medication-warehouse", tags=["Медикаменты на складе"])
def add_medication_to_warehouse(medicationWarehouse: db_tools.MedicationWarehouse) -> str:
    db_tools.addMedicationWarehouse(medicationWarehouse)
    return f"medication {medicationWarehouse.med_id} on warehouse with {medicationWarehouse}"

#удаление медикамента на складе
@app.delete("/medication-warehouse/{w_id}-{med_id}", tags=["Медикаменты на складе"])
def delete_medication_from_warehouse(w_id: int, med_id: int) -> str:
    db_tools.deleteMedicationWarehouse(w_id=w_id, med_id=med_id)
    return f"medication delete {med_id} from warehouse {w_id}"


#получение всех заказов
@app.get("/orders", tags=["Заказы"])
def get_all_orders(current_user: User = Depends(get_current_active_user)) -> dict:
    return {
        "orders": db_tools.allOrder()
    }

#добавление заказа
@app.post("/orders", tags=["Заказы"])
def add_order(order: db_tools.Order) -> dict:
    db_tools.addOreder(order)
    return {
        "ph_od_id": db_tools.getOrderMaxId()
    }

#удаление заказа
@app.delete("/orders/{ph_od_id}", tags=["Заказы"])
def delete_order(ph_od_id: int) -> str:
    db_tools.deleteOrder(ph_od_id)
    return f"order with id {ph_od_id} is deleted"

#получение медикаментов в заказе
@app.get("/orders/{ph_od_id}/details", tags=["Заказы"])
def getMedInOrder(ph_od_id: int) -> dict:
    return db_tools.getMedInOrder(ph_od_id)


#обновление статуса заказ
@app.put("/orders/status", tags=["Заказы"])
def update_status(order: db_tools.Order) -> str:
    db_tools.updateOrderStatus(order)
    return f"order {order.ph_od_id} status is {order.ph_od_status}"


#обновление даты отгрузки
@app.put("/orders/shipment-date", tags=["Заказы"])
def update_shipment_date(order: db_tools.Order) -> str:
    db_tools.updateShipmentDate(order)
    return f"order {order.ph_od_id} shipment date is {order.ph_od_date_shipment}"


#добавление медикамента в заказ
@app.post('/medication-order', tags=['Медикаменты в заказе'])
def add_medication_to_order(medication_order: db_tools.medicationOrder) -> str:
    db_tools.addMedOrder(medication_order)
    return f"med {medication_order.med_id} in quantity {medication_order.quantity} is add in order {medication_order.ph_od_id}"