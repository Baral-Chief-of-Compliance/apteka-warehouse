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
    ph_id : int or None = None
    ph_address : str
    ph_phone_number : str
    ph_name: str


#добавить аптеку
def addPharmacy(pharmacy : Pharmacy) -> None:

    conn = None
    cursor = None

    try:
        conn = connectionDB()

        cursor = conn.cursor()

        cursor.execute('''INSERT INTO pharmacy (ph_address, ph_phone_number, ph_name) VALUES (%s,%s, %s)''', 
                       (pharmacy.ph_address, pharmacy.ph_phone_number, pharmacy.ph_name)
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
                "ph_phone_number": p[2],
                "ph_name": p[3]
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
                       ph_phone_number=%s,
                       ph_name=%s
                       WHERE ph_id=%s''', 
                       (
                           pharmacy.ph_address,
                           pharmacy.ph_phone_number,
                           pharmacy.ph_name,
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
    s_id : int or None = None
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
    w_id : int or None = None
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


#получение ифнормации о складе по его id
def getWarehouse(w_id: int) -> dict:
    conn = None
    cursor = None
    result = {}

    try:
        conn = connectionDB()
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM warahouse where w_id = %s''', (w_id,))
        warehouse_info = cursor.fetchone()
        result = {
            'w_id': warehouse_info[0],
            'w_address': warehouse_info[1],
            'w_director': warehouse_info[2],
            'w_phone_number': warehouse_info[3]
        }
        
    except Exception as error:
        print(error)

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
        return result
    

#получение всех медикаментов со склада
def getMedicationFromWareHouse(w_id: int) -> list:
    conn = None
    cursor = None
    result = []

    try:
        conn = connectionDB()
        cursor = conn.cursor()
        cursor.execute('''SELECT * from get_medication_from_warehouse(%s)''', (w_id,))
        medication = cursor.fetchall()
        print(medication)

        for m in medication:
            result.append({
                "w_id": m[0],
                "w_director": m[1],
                "w_phone_number": m[2],
                "w_address": m[3],
                "warehouseid": m[4],
                "medicationid": m[5],
                "med_id": m[6],
                "med_name": m[7],
                "med_catagory": m[8],
                "med_dosage": m[9],
                "med_price": float(m[10][1:]),
                "med_expiration_date": m[11],
                "med_receipts": m[12],
                "supplierid": m[13],
                "s_id": m[14],
                "s_name": m[15]
            })

    except Exception as error:
        print(error)

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
        return result

        

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
    med_id : int or None = None
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
                "med_price": float(m[4][1:]),
                "med_expiration_date": m[5],
                "med_receipts": m[6],
                "supplierID": m[7],
                "quantity": 1
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


#модель медикаментов склада
class MedicationWarehouse(BaseModel):
    w_id : int
    med_id : int

#функция добавления медикаментов склада
def addMedicationWarehouse(medicationWarehouse: MedicationWarehouse) -> None:
    conn = None
    cursor = None
    try:
        conn = connectionDB()
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO
        medication_warehouse(warehouseid, medicationid) values (%s, %s)
        ''', (medicationWarehouse.w_id, medicationWarehouse.med_id))
        
        conn.commit()
    except Exception as error:
        print(error)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()


#функция удаление медикамента склада
def deleteMedicationWarehouse(w_id: int, med_id: int) -> None:
    conn = None
    cursor = None
    try:
        conn = connectionDB()
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM medication_warehouse WHERE medicationid = %s and warehouseid = %s''', (med_id, w_id))
        conn.commit()
    except Exception as error:
        print(error)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()


#модель заказа
class Order(BaseModel):
    ph_od_id : int or None = None
    ph_od_date: datetime = datetime.today
    ph_od_date_shipment: datetime or None = None
    ph_od_status: str or None = 'Создан'
    pharmacyid: int


#добавить заказ
def addOreder(order: Order) -> None:
    conn = None
    cursor = None
    try:
        conn = connectionDB()
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO pharmacy_order(ph_od_date, ph_od_status, pharmacyid) values (%s, %s, %s)''',
                       (order.ph_od_date, order.ph_od_status, order.pharmacyid))
        conn.commit()

    except Exception as error:
        print(error)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

#получить максимальный айди в таблице заказов
def getOrderMaxId() -> int:
    conn = None
    cursor= None
    result = 0
    try:
        conn = connectionDB()
        cursor = conn.cursor()
        cursor.execute('''SELECT MAX(ph_od_id) FROM pharmacy_order''')
        id = cursor.fetchone()
        result = id[0]
    except Exception as error:
        print(error)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
        return result


#изменение статуса заказа
def updateOrderStatus(order: Order) -> None:
    conn = None
    cursor = None
    try:
        conn = connectionDB()
        cursor = conn.cursor()
        cursor.execute('''UPDATE pharmacy_order SET ph_od_status = %s WHERE ph_od_id = %s''', 
                       (order.ph_od_status, order.ph_od_id))
        conn.commit()

    except Exception as error:
        print(error)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()


#изменение установка даты отгрузки заказа
def updateShipmentDate(order: Order) -> None:
    conn = None
    cursor = None
    try:
        conn = connectionDB()
        cursor = conn.cursor()
        cursor.execute('''UPDATE pharmacy_order SET ph_od_date_shipment = %s WHERE ph_od_id = %s''', 
                       (order.ph_od_date_shipment, order.ph_od_id))
        conn.commit()
    except Exception as error:
        print(error)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()


#отображение всех заказов
def allOrder() -> list:
    conn = None
    cursor = None
    result = []
    try:
        conn = connectionDB()
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM getorders();''')
        orders = cursor.fetchall()
        
        for o in orders:
            result.append({
                'ph_od_id': o[0],
                'ph_od_date': o[1],
                'ph_od_date_shipment': o[2],
                'ph_od_status': o[3],
                'ph_name': o[4],
                'ph_address': o[5],
                'ph_phone_number': o[6]
            })

    except Exception as error:
        print(error)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
        return result  


#удаление заказа
def deleteOrder(ph_od_id: int) -> None:
    conn = None
    cursor = None
    try:
        conn = connectionDB()
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM pharmacy_order WHERE ph_od_id = %s''', (ph_od_id,))
        conn.commit()
    except Exception as error:
        print(error)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()    
    

# модель для медикамента в заказ
class medicationOrder(BaseModel):
    med_id: int
    ph_od_id: int
    quantity: int


#добавить медикаменты в заказ
def addMedOrder(medicationOrder: medicationOrder) -> None:
    conn = None
    cursor = None
    try:
        conn = connectionDB()
        cursor = conn.cursor()
        cursor.execute('''
                       INSERT INTO medication_pharmacy_order(medicationid, pharmacy_orderid, med_ph_od_quantity) values (%s, %s, %s)''',
                       (medicationOrder.med_id, medicationOrder.ph_od_id, medicationOrder.quantity)
                       )
        conn.commit()
    except Exception as error:
        print(error)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close() 


#получить все медикаменты в заказе
def getMedInOrder(ph_od_id: int) -> dict:
    conn = None
    cursor = None
    result = {
        'medications': [],
        'amountPrice': 0
    }
    try:
        conn = connectionDB()
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM get_med_in_order(%s)''', (ph_od_id,))
        medications = cursor.fetchall()

        

        for m in medications:
            result["medications"].append({
                'med_name': m[0],
                'med_catagory': m[1],
                'med_dosage': m[2],
                'med_price': float(m[3][1:]),
                'med_expiration_date': m[4],
                'med_receipts': m[5],
                'med_quantity': m[6],
                'med_amount_price': m[6] * float(m[3][1:])
            })

            result['amountPrice'] += m[6] * float(m[3][1:])
    except Exception as error:
        print(error)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close() 
        return result
