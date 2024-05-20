<template>
    <q-page class="q-pa-md">

      <!-- уведомление о том, что заказов нет -->
      <div v-if="state.orders.length == 0" class="text-center text-h5 text-italic text-grey">
        <span>На данный момент заказов нет</span>
      </div>

      <!-- таблица с заказами -->
      <div v-if="state.orders.length != 0">
        <q-table
          title="Заказы"
          :rows="state.orders"
          :columns="state.columnsOrders"
          row-key="name"
        >
          <!-- кнопка удаление заказа -->
          <template v-slot:body-cell-delete="props">
            <q-td :props="props">
              <q-btn v-if="checkRightsAdminManagerPhManager()" color="red" icon="delete" @click="deleteOrder(props.row.ph_od_id)"></q-btn>
            </q-td>
          </template>

          <!-- кнопка установка статуса заказа -->
          <template v-slot:body-cell-updateStatus="props">
            <q-td :props="props">
              <q-btn v-if="checkRightsAdminManagerPhManager()" color="orange" icon="toc" @click="state.updateStatusCard = openCard(props.row.ph_od_id)"></q-btn>
            </q-td>
          </template>

          <!-- кнопка установка даты отгрузки -->
          <template  v-slot:body-cell-updateDate="props">
            <q-td :props="props">
              <q-btn v-if="checkRightsAdminManagerPhManager()" color="orange" icon="schedule" @click="state.updateDateCard = openCard(props.row.ph_od_id)"></q-btn>
            </q-td>
          </template>

          <!-- кнопка детали заказа -->
          <template v-slot:body-cell-details="props">
            <q-td :props="props">
              <q-btn color="primary" icon="info" @click="getMedicationInOrder(props.row.ph_od_id)"></q-btn>
            </q-td>
          </template>


        </q-table>
      </div>

      <!-- кнопка для добавления заказа -->
      <div v-if="checkRightsAdminManagerPhManager()" class="column">
        <q-btn color="green" icon="add" label="Добавить заказ" @click="state.addCard = true" />
      </div>

      <!-- диалоговое окно для добавления заказа -->
      <q-dialog v-model="state.addCard" persistent>
        <q-card class="col-8">
          <q-card-section class="column">

            <!-- заголовки карточки -->
            <div>
              <q-avatar icon="circle" color="green" text-color="white" />
              <span class="q-ma-sm text-h5">Создать новый заказ</span>
            </div>


            <!-- список аптек для заказа -->
            <div>
              <span class="q-ma-xl text-h6">ШАГ 1: Выбрать аптеку для заказа</span>

              <div class="column">
                <q-radio class="q-my-md" v-for="ph in state.pharmacy" :key="ph.ph_id" :val="ph.ph_id" v-model="state.selectPharmacy">
                    <q-card class="" style="width: 350px">
                      <q-card-section>


                        <div>
                          <b>Адрес: </b>{{ ph.ph_address }}
                        </div>
                        <div>
                          <b> Директор: </b> {{ ph.ph_address }}
                        </div>
                        <div>
                          <b> Телефон: </b> {{ ph.ph_phone_number }}
                        </div>

                      </q-card-section>

                    </q-card>                    
                </q-radio>
              </div>
            </div>

            <!-- список медикаментов -->
            <div v-if="state.selectPharmacy != null">
              <span class="q-ma-xl text-h6">ШАГ 2: Выбрать медикаменты</span>

              <div class="column q-mt-md">

                <!-- таблица с медикаментами, в которой можно выбирать медикаменты -->
                <q-table
                  color="primary"
                  title="Медикаменты"
                  :rows="state.medication"
                  :columns="state.columns"
                  row-key="med_id"
                  selection="multiple"
                  v-model:selected="state.selected_med"
                >
                  <!-- поле для изменения количество медикаментов -->
                  <template v-slot:body-cell-quantity="props">
                    <q-td :props="props">
                      <q-input  min="1" v-model="props.row.quantity" type="number" />
                    </q-td>
                  </template>

                  <!-- поле для цены медикаментов -->
                  <template v-slot:body-cell-med_price="props">
                    <q-td :props="props">
                      {{getMedPrice(props.row.quantity, props.row.med_price)}}
                    </q-td>
                  </template>

                </q-table>

              </div>
            </div>


          </q-card-section>
          <q-card-actions align="right">
            <q-btn flat label="Отмена" color="red" @click="closeAddCard()" />
            <q-btn v-if="state.selectPharmacy != null && state.selected_med.length !=0" flat label="Создать" color="green" @click="addOrder()" />
          </q-card-actions>
        </q-card>
      </q-dialog>
      <!-- конец диалогового окно для добавления заказа -->

      <!-- диалоговое окно для изменения статуса заказов -->
      <q-dialog v-model="state.updateStatusCard" persistent>
        <q-card>
          <q-card-section class="items-center">
            <!-- заголовок картчоки -->
            <div class="row">
              <q-avatar icon="toc" color="orange" text-color="white" />
              <span class="q-ma-sm text-h5">Изменить статус заказа</span>
            </div>

            <div class="column q-mt-xl">
              <!-- выбор статуса заказа -->
              <q-radio v-model="state.selectedStatus" val="В обработке" label="В обработке" />
              <q-radio v-model="state.selectedStatus" val="Сборка" label="Сборка" />
              <q-radio v-model="state.selectedStatus" val="Отправлен" label="Отправлен" />
              <q-radio v-model="state.selectedStatus" val="Доставлено" label="Доставлено" />
              <q-radio v-model="state.selectedStatus" val="Отменен" label="Отменен" />
            </div>

          </q-card-section>
          <q-card-actions align="right">
            <q-btn flat label="Отмена" color="red" v-close-popup />
            <q-btn v-if="state.selectedStatus != null" flat label="Обновить" color="orange" @click="updateStatus()" />
          </q-card-actions>
        </q-card>
      </q-dialog>
      <!-- конец диалогового окна для изменения статуса заказов -->


      <!-- диалоговое окно для изменение даты отгрузки заказа -->
      <q-dialog v-model="state.updateDateCard" persistent>
        <q-card>
          <q-card-section class="items-center">
            <!-- заголовок карточки -->
            <div class="row">
              <q-avatar icon="schedule" color="orange" text-color="white" />
              <span class="q-ma-sm text-h5">Установить дату отгрузки</span>
            </div>
            
            <!-- поле для ввода даты отгрузки -->
            <q-input v-model="state.dateShipment" type="date" label="Дата отгрузки" />


          </q-card-section>
          <q-card-actions align="right">
            <q-btn flat label="Отмена" color="red" v-close-popup />
            <q-btn v-if="state.dateShipment!=null" flat label="Установить" color="orange" @click="updateDateShipment()" />
          </q-card-actions>
        </q-card>
      </q-dialog>
      <!-- конец диалогового окна для изменения даты отгрузки заказа -->


      <!-- диалоговое окно для деталей заказа -->
      <q-dialog v-model="state.detailOrderCard" persistent>
        <q-card class="col-6">
          <q-card-section class="row items-center">
            <!-- заголовок картчоки -->
            <div class="column">
              <div class="row">
                <q-avatar icon="info" color="primary" text-color="white" />
                <span class="q-ma-sm text-h5">Детали заказов</span>
              </div>

              <div class="q-mt-xl">
                <q-table
                  title="Медикаменты в заказе"
                  :rows="state.medicationsInOrder"
                  :columns="state.columnsMedicationInOrder"
                  row-key="name"
                />

                <div class="text-h5 q-ma-xs">Сумма заказа: {{ state.amountPrice }} руб.</div>
              </div>
            </div>

          </q-card-section>
          <q-card-actions align="right">
            <q-btn flat label="Назад" color="red" v-close-popup />
            <!-- <q-btn flat label="Turn on Wifi" color="primary" v-close-popup /> -->
          </q-card-actions>
        </q-card>
      </q-dialog>
      <!-- конец диалового окна для деталей заказа -->

    </q-page>
  </template>

<script setup>
import { useRouter } from 'vue-router';
import { onMounted, reactive, inject } from 'vue';
import axios from 'axios';

//берем функцию для получения всех аптек
const { getPharmacy } = inject('pharmacy');

//берем функцию для получения всех медикаментов
const { getMed } = inject('med');

//функция для проверки прва для админа и манагера склада
const { checkRightsAdminManager } = inject('role');

//функция для проверки прва для админа и манагера склада и манагера аптеки
const {checkRightsAdminManagerPhManager} = inject('role');


const state = reactive({

  updateStatusCard: false, //состояние карточки для обновления статуса 
  updateDateCard: false, //состояние карточки для обновление даты откгрузки
  detailOrderCard: false, //состояние карточки для деталей заказа

  addCard: false, //состояние карточки для добавления
  pharmacy: [], // все аптек
  medication: [], //все медикаменты

  selected_med: [], //выбранные медикаменты,

  dateShipment: null, //переменная для даты отгрузки
  selectedStatus: null, //переменная для статусов
  selectedOrderId: null, // переменная для текущего заказа

  selectPharmacy: null, // выбрання аптека
  orderId: null, //id заказа который мы получаем при создании

  orders: [], //список всех заказов

  medicationsInOrder: [], //список медикаментов в заказе
  amountPrice: 0, //цена за заказа

  columnsMedicationInOrder: [ //наименование колонн для таблицы медикаментов в заказе
    { name: 'med_name', align: 'center', label: 'Название', field: row => row.med_name, sortable: true },
    { name: 'med_catagory', align: 'center', label: 'Категория', field: row => row.med_catagory, sortable: true },
    { name: 'med_dosage', align: 'center', label: 'Доза', field: row => row.med_dosage, sortable: true },
    { name: 'med_price', align: 'center', label: 'Цена за шт.(руб)', field: row => row.med_price, sortable: true },
    { name: 'med_expiration_date', align: 'center', label: 'Истечение срока годности', field: row => row.med_expiration_date, sortable: true },
    { name: 'med_receipts', align: 'center', label: 'Дата поступления', field: row => row.med_receipts, sortable: true },
    { name: 'med_quantity', align: 'center', label: 'Количество в заказе', field: row => row.med_quantity, sortable: true },
    { name: 'med_amount_price', align: 'center', label: 'Сумма', field: row => row.med_amount_price, sortable: true }
  ],

  columnsOrders: [ //наименование колонн для таблицы отображение заказа
    { name: 'ph_od_date', align: 'center', label: 'Дата создания', field: row => row.ph_od_date, sortable: true },
    { name: 'ph_od_date_shipment', align: 'center', label: 'Дата отправки', field: row => row.ph_od_date_shipment, sortable: true },
    { name: 'ph_od_status', align: 'center', label: 'Статус', field: row => row.ph_od_status, sortable: true },
    { name: 'ph_name', align: 'center', label: 'Название аптеки', field: row => row.ph_name, sortable: true },
    { name: 'ph_address', align: 'center', label: 'Адрес аптеки', field: row => row.ph_address, sortable: true },
    { name: 'ph_phone_number', align: 'center', label: 'Номер телефона', field: row => row.ph_phone_number, sortable: true },

    //кнопки для манипуляции с данными 
    { name: 'delete', align: 'center', label: 'Удаление'},
    { name: 'updateStatus', align: 'center', label: 'Изменение статуса'},
    { name: 'updateDate', align: 'center', label: 'Изменение даты отгрузки'},
    { name: 'details', align: 'center', label: 'Детали заказа'}
  ],

  columns : [ //наименования колонн для таблицы с добавлением медикаментов
  { name: 'med_name', align: 'center', label: 'Название', field: row => row.med_name, sortable: true },
  { name: 'quantity', align: 'center', label: 'Количество', field: row => row.quantity, sortable: true },
  { name: 'med_price', align: 'center', label: 'Цена (руб)', field: row => row.med_price, sortable: true }
  ],



})

//закрыть карточку c добавлением заказа
function closeAddCard(){
  state.selectPharmacy = null;
  state.selected_med = [];
  state.addCard = false;
}

//функция для расчета цены за медикаменты
function getMedPrice(quantity, price){
  return quantity * price
}

//функция для добавление заказа
function addOrder(){
  axios.post(
    'https://zdorovie.space/api/v1/orders', {
      ph_od_date: "2024-05-19T16:55:09.690Z",
      ph_od_date_shipment: "2024-05-19T16:55:09.690Z",
      ph_od_status: "Создан",
      pharmacyid: state.selectPharmacy
    }
  ).then((res)=>{
    state.orderId = res.data.ph_od_id

    for (let index = 0; index < state.selected_med.length; index++) {
      axios.post(
        'https://zdorovie.space/api/v1/medication-order',
        {
          med_id: state.selected_med[index]['med_id'],
          ph_od_id: state.orderId,
          quantity: state.selected_med[index]['quantity']

        }
      )
        
    }
    state.selectPharmacy = null;
    state.selected_med = [];
    state.orderId = null;
    state.addCard = false;
    getAllOrders();
  })
}

// функция для получения всех заказов
function getAllOrders(){
  axios.get('https://zdorovie.space/api/v1/orders')
  .then((res)=>{
    state.orders = res.data.orders;
  })
}


//функция удаление заказа
function deleteOrder(ph_od_id){
  axios.delete(`https://zdorovie.space/api/v1/orders/${ph_od_id}`)
  .then((res)=>{
    getAllOrders();
  })
}

//функция получения медикаментов в заказе
function getMedicationInOrder(ph_od_id){
  axios.get(`https://zdorovie.space/api/v1/orders/${ph_od_id}/details`)
  .then((res)=>{
    state.amountPrice = res.data.amountPrice;
    state.medicationsInOrder = res.data.medications;
    state.detailOrderCard = true;
  })
}

//функция для обновления даты заказов
function updateDateShipment(){
  axios.put(`https://zdorovie.space/api/v1/orders/shipment-date`, {
    ph_od_id: state.selectedOrderId,
    ph_od_date: "2024-05-19T17:55:23.906Z",
    ph_od_date_shipment: state.dateShipment,
    ph_od_status: "Создан",
    pharmacyid: 0
  })
  .then((res)=>{
    getAllOrders();
    state.updateDateCard = false;
  })
}

//функция для обновления статуса заказов
function updateStatus(){
  axios.put(`https://zdorovie.space/api/v1/orders/status`, {
    ph_od_id: state.selectedOrderId,
    ph_od_date: "2024-05-19T17:55:23.906Z",
    ph_od_date_shipment: "2024-05-19T17:55:23.906Z",
    ph_od_status: state.selectedStatus,
    pharmacyid: 0
  })
  .then((res)=>{
    getAllOrders();
    state.updateStatusCard = false;
  })
}

//функция для открытия карт обновления
function openCard(ph_od_id){
  state.selectedOrderId = ph_od_id;
  return true;
}

onMounted(async() => {
  state.pharmacy = await getPharmacy();
  state.medication = await getMed();
  getAllOrders();
})

</script>