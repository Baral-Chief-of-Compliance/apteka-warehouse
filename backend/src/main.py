from typing import Union
from fastapi import FastAPI
from dotenv import load_dotenv
import db_tools


load_dotenv()

app = FastAPI()


@app.get("/")
def index():
    return {"Hello": "world"}


#добавление аптеки в базу данных
@app.post("/pharmacy")
def addPharmacy(pharmacy: db_tools.Pharmacy) -> str:
    db_tools.addPharmacy(pharmacy=pharmacy)
    return f"pharmasy on {pharmacy.ph_address} id add"


#получение всех аптек
@app.get("/pharmacy")
def getAllPharmacy() -> dict:
    return {
        "pharmacys" : db_tools.getAllPharmacy()
    }

#удаление аптеки по её id
@app.delete("/pharmacy/{ph_id}")
def deletePharmacy(ph_id: int) -> str:
    db_tools.deletePharmacy(ph_id)
    return f"pharmasy with ph_id = {ph_id} is deleted"


#обновление данных об аптеке
@app.put("/pharmacy/{ph_id}")
def updatePharmacy(pharmacy: db_tools.Pharmacy) -> str:
    db_tools.updatePharmacy(pharmacy=pharmacy)
    return f"pharmacy with ph_id = {pharmacy.ph_id} is updated"


#добавления поставщика в базу данных
@app.post("/supplier")
def addSupplier(supplier: db_tools.Supplier) -> str:
    db_tools.addSupplier(supplier=supplier)
    return f"supplier {supplier.s_name} is add"

#получение всех поставщиков
@app.get("/supplier")
def allSupplier() -> dict:
    return {
        "suppliers": db_tools.allSupplier()
    }

#удаление поставщика
@app.delete("/supplier/{s_id}")
def deleteSupplier(s_id: int) -> str:
    db_tools.deleteSupplier(s_id=s_id)
    return f"supplier with s_id = {s_id} is deleted"


#обновление данных о поставщике
@app.put("/supplier/{s_id}")
def updateSupplier(supplier:db_tools.Supplier) -> str:
    db_tools.updateSupplier(supplier=supplier)
    return f"supplier with s_id = {supplier.s_id} is updated"


#добавление склада в базу данных
@app.post("/warehouse")
def addWarehouse(warehouse:db_tools.Warehouse) -> str:
    db_tools.addWarehouse(warehouse=warehouse)
    return f"warehouse on {warehouse.w_address} is added"

#получение всех складов
@app.get("/warehouse")
def allWarehouse() -> dict:
    return {
        "warehouse": db_tools.allWarehouse()
    }

#удаление склада
@app.delete("/warehouse/{w_id}")
def deleteWarehouse(w_id:int) -> str:
    db_tools.deleteWarehouse(w_id)
    return f"warehouse with w_id = {w_id} is deleted"

#обновление данных о складе
@app.put("/warehouse/{w_id}")
def updateWarehouse(warehouse:db_tools.Warehouse) -> str:
    db_tools.updateWarehouse(warehouse=warehouse)
    return f"warehouse with w_id = {warehouse.w_id} is updated"


#добавление медикаментов в базу данных
@app.post("/medication")
def addMedication(medication:db_tools.Medication) -> str:
    db_tools.addMedication(medication)
    return f"medication with name {medication.med_name} is add"


#получение всех медикаментов
@app.get("/medication")
def allMedication() -> dict:
    return {
        "medication": db_tools.allMedication()
    }

#удаление медикамента  из базы данных
@app.delete("/medication/{med_id}")
def deleteMedication(med_id : int) -> str:
    db_tools.deleteMedication(med_id)
    return f"medications with med_id = {med_id} is deleted"

#обновления информации о медикаменте
@app.put("/medication/{med_id}")
def updateMedication(medication:db_tools.Medication) -> str:
    db_tools.updateMedication(medication)
    return f"medication with med_id = {medication.med_id} is updated"
