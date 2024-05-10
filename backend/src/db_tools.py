import psycopg2
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from datetime import datetime


#подключение к базе данных
def connectionDB():

    load_dotenv()

    conn = psycopg2.connect(
        host = os.getenv("POSTGRESQL_HOSTNAME"),
        dbname = os.getenv("POSTGRESQL_DATABASE"),
        user = os.getenv("POSTGRESQL_USERNAME"),
        password = os.getenv("POSTGRESQL_PASSWORD"),
        port = os.getenv("POSTGRESQL_PORT")
    )

    return conn


#модель под аптеку 
class Pharmacy(BaseModel):
    ph_id : int | None = None
    ph_address : str
    ph_phone_number : str


#добавить аптеку
def addPharmacy(pharmacy : Pharmacy) -> None:

    conn = None
    cursor = None

    try:
        conn = connectionDB()

        cursor = conn.cursor()

        cursor.execute('''INSERT INTO pharmacy (ph_address, ph_phone_number) VALUES (%s,%s)''', 
                       (pharmacy.ph_address, pharmacy.ph_phone_number)
                       )
        
        conn.commit()


    except Exception as error:
        print(error)

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:        
            conn.close()


#получение всех аптек
def getAllPharmacy() -> list:
    conn = None
    cursor = None

    result = []

    try:
        conn = connectionDB()

        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM pharmacy''')

        pharmacys = cursor.fetchall()

        for p in pharmacys:
            result.append({
                "ph_id": p[0],
                "ph_address": p[1],
                "ph_phone_number": p[2]
            })
        
        conn.commit()

    except Exception as error:
        print(error)

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:        
            conn.close()

        return result
    
#удаление аптеки
def deletePharmacy(ph_id: int) -> None:
    conn = None
    cursor = None

    try:
        conn = connectionDB()
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM pharmacy WHERE ph_id = %s''', (ph_id, ))
        conn.commit()

    except Exception as error:
        print(error)

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:        
            conn.close()

#обновления данных аптеки
def updatePharmacy(pharmacy : Pharmacy) -> None:
    conn = None
    cursor = None

    try:
        conn = connectionDB()
        cursor = conn.cursor()
        cursor.execute('''
                       UPDATE pharmacy SET 
                       ph_address=%s, 
                       ph_phone_number=%s
                       WHERE ph_id=%s''', 
                       (
                           pharmacy.ph_address,
                           pharmacy.ph_phone_number,
                           pharmacy.ph_id
                           )
                       )

        conn.commit()
    
    except Exception as error:
        print(error)

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:        
            conn.close()

#модель для поставщика
class Supplier(BaseModel):
    s_id : int | None = None
    s_name : str


#добавление постащика в базу данных
def addSupplier(supplier : Supplier) -> None:
    conn = None
    cursor = None

    try:
        conn = connectionDB()
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO supplier(s_name) VALUES (%s)''', (supplier.s_name,))
        conn.commit()
    
    except Exception as error:
        print(error)

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()


#получения всех поставщиков из базы данных
def allSupplier() -> list:
    conn = None
    cursor = None

    result = []

    try:
        conn = connectionDB()
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM supplier''')
        suppliers = cursor.fetchall()

        for s in suppliers:
            result.append({
                "s_id": s[0],
                "s_name": s[1]
            })
    
    except Exception as error:
        print(error)

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
        return result


#удаление поставщика из базы данных
def deleteSupplier(s_id:int) -> None:
    conn = None
    cursor = None
    try:
        conn = connectionDB()
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM supplier WHERE s_id = %s''', (s_id,))
        conn.commit()
    
    except Exception as error:
        print(error)

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

#обновление данных о поставщике
def updateSupplier(supplier: Supplier) -> None:
    conn = None
    cursor = None
    try:
        conn = connectionDB()
        cursor = conn.cursor()
        cursor.execute('''UPDATE supplier SET
                       s_name = %s
                       where s_id = %s
                       ''', (supplier.s_name, supplier.s_id))
        conn.commit()
    except Exception as error:
        print(error)

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

#модель склада 
class Warehouse(BaseModel):
    w_id : int | None = None
    w_address : str
    w_director : str
    w_phone_number : str

#добавление склада в базу данных
def addWarehouse(warehouse:Warehouse) -> None:
    conn = None
    cursor = None

    try:
        conn = connectionDB()
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO 
                       warahouse(w_address, w_director, w_phone_number) 
                       values (%s, %s, %s)
                       ''', (warehouse.w_address, 
                             warehouse.w_director, 
                             warehouse.w_phone_number
                             )
                             )
        conn.commit()

    except Exception as error:
        print(error)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

#получение всех складов
def allWarehouse() -> list:
    conn = None
    cursor = None
    result = []

    try:
        conn = connectionDB()
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM warahouse''')
        warehouse = cursor.fetchall()
        for w in warehouse:
            result.append({
                "w_id": w[0],
                "w_address": w[1],
                "w_director": w[2],
                "w_phone_number": w[3]
            })
    except Exception as error:
        print(error)

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
        return result

#удаление склада из базы данных
def deleteWarehouse(w_id:int) -> None:
    conn = None
    cursor = None

    try:
        conn = connectionDB()
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM warahouse WHERE w_id = %s''', (w_id,))
        conn.commit()

    except Exception as error:
        print(error)

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

#обновление данных о складе
def updateWarehouse(warehouse:Warehouse) -> None:
    conn = None
    cursor = None
    try:
        conn = connectionDB()
        cursor = conn.cursor()
        cursor.execute('''UPDATE warahouse SET
                       w_address = %s,
                       w_director = %s,
                       w_phone_number = %s
                       WHERE w_id = %s
                       ''', 
                       (
                           warehouse.w_address,
                           warehouse.w_director,
                           warehouse.w_phone_number,
                           warehouse.w_id
                       )
                       )
        conn.commit()
    except Exception as error:
        print(error)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()


#модель медикамента
class Medication(BaseModel):
    med_id : int|None = None
    med_name : str
    med_category : str
    med_dosage : float
    med_price : float
    med_expiration_date: datetime
    med_receipts: datetime
    supplierID : int

#добавление медикамента в базу данных
def addMedication(medication:Medication) -> None:
    conn = None
    cursor = None

    try:
        conn = connectionDB()
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO 
                       medication(med_name, med_catagory,
                       med_dosage, med_price, med_expiration_date,
                       med_receipts, supplierID) 
                       values (%s, %s, %s, %s, %s, %s, %s)''',
                       (
                           medication.med_name,
                           medication.med_category,
                           medication.med_dosage,
                           medication.med_price,
                           medication.med_expiration_date,
                           medication.med_receipts,
                           medication.supplierID
                       )
                       )
        conn.commit()
    except Exception as error:
        print(error)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()


#получение всех медикаментов
def allMedication() -> list:
    conn = None
    cursor = None
    result = []

    try:
        conn = connectionDB()
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM medication''')
        medications = cursor.fetchall()

        for m in medications:
            result.append({
                "med_id":m[0],
                "med_name": m[1],
                "med_category": m[2],
                "med_dosage": m[3],
                "med_price": m[4],
                "med_expiration_date": m[5],
                "med_receipts": m[6],
                "supplierID": m[7]
            })
    except Exception as error:
        print(error)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
        return result
    

#удаление медикамента из базы данных
def deleteMedication(med_id:int) -> None:
    conn = None
    cursor = None
    try:
        conn = connectionDB()
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM medication WHERE med_id = %s''', (med_id,))
        conn.commit()
    except Exception as error:
        print(error)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()


#обновление данных о медикаменте
def updateMedication(medication:Medication) -> None:
    conn = None
    cursor = None
    try:
        conn = connectionDB()
        cursor = conn.cursor()
        cursor.execute('''UPDATE medication SET
                       med_name = %s,
                       med_catagory = %s,
                       med_dosage = %s,
                       med_price = %s,
                       med_expiration_date = %s,
                       med_receipts = %s,
                       supplierID = %s
                       where med_id = %s
                       ''', (
                           medication.med_name, medication.med_category,
                           medication.med_dosage, medication.med_price,
                           medication.med_expiration_date, medication.med_receipts,
                           medication.supplierID, medication.med_id
                           ))
        conn.commit()
    except Exception as error:
        print(error)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()