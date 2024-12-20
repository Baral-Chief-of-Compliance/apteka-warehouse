<template>
    <q-page class="q-pa-md">
      <!-- кнопка чтобы вернуться на страницу к складам -->
      <q-btn color="primary" icon="warehouse" label="К складам" @click="router.push({name:'Warehouse'})" />
      <div class="column text-center text-h6">
        <span>Склад по адресу: <b>{{ state.w_address }}</b></span>
        <span>Номер телефона: <b>{{ state.w_phone_number }}</b></span>
        <span>Директор: <b>{{ state.w_director }}</b></span>
      </div>

      <div class="q-mt-xl">
        <!-- уведомление о том, что на складе нет медикаментов -->
        <div v-if="state.medication.length == 0" class="text-center text-h5 text-italic text-grey">
          <span>На данный момент на складе нету медикаментов</span>
        </div>
        <!-- таблица с медикаментами склада -->
        <div v-if="state.medication.length != 0">
          <q-table
            title="Медикаменты на складе"
            :rows="state.medication"
            :columns="state.columns"
            row-key="name"
          >

          <!-- изменяем отображение для колонки удаление данных -->
          <template v-slot:body-cell-delete="props">
            <q-td :props="props">
              <q-btn v-if="checkRightsAdminManagerPhManager()" color="red" icon="delete" @click="deleteMed(props.row.med_id)"></q-btn>
            </q-td>
          </template>
        
        </q-table>
        </div>


      </div>


      <!-- кнопка чтобы добавить склад -->
      <div class="q-mt-xl column">
        <q-btn v-if="checkRightsAdminManagerPhManager()" color="green" icon="add" label="Добавить медикаментов на склад" @click="state.addCard=true, state.selected_med = []" />
      </div>


      <q-dialog v-model="state.addCard" persistent>
        <q-card>
          <q-card-section class="column">
            <!-- заголовок карточки -->
            <div class="row">
              <q-avatar icon="medication" color="green" text-color="white" />
              <span class="q-ma-sm text-h5">Добавить медикаменты на склад</span>
            </div>

            <!-- список медикаментов, которые можно добавить -->
            <div class="column q-mt-md">
              <q-checkbox v-for="med in state.all_medication" :key="med.med_id" :val="med.med_id" v-model="state.selected_med" :label="med.med_name" />
            </div>

          </q-card-section>
          <q-card-actions align="right">
            <q-btn flat label="Отмена" color="red" v-close-popup />
            <q-btn v-if="state.selected_med.length != 0" flat label="Добавить" color="green" @click=addMedicationToWareHouse() />
          </q-card-actions>
        </q-card>
      </q-dialog>

    </q-page>
</template>

<script setup>
import { useRouter, useRoute  } from 'vue-router';
import axios from 'axios';
import { onMounted, reactive, inject } from 'vue';


//берем функцию для получения всех медикаментов
const { getMed } = inject('med');

//функция для проверки прва для админа и манагера склада
const { checkRightsAdminManager } = inject('role');

//функция для проверки прва для админа и манагера склада и манагера аптеки
const {checkRightsAdminManagerPhManager} = inject('role');

//роутер
const router = useRouter();
//маршрут
const route = useRoute();

const state = reactive({
  w_id: null,
  w_address: null,
  w_director: null,
  w_phone_number: null,

  medication: [], //медикаменты склада
  all_medication: [], //медикаменты все

  selected_med: [], //выбранне медикамены для добавление


  addCard: false,   //карточка добавление медикамента

  columns : [
  {
    name: 'med_id',
    required: true,
    label: 'Индекс',
    align: 'center',
    field: row => row.med_id,
    format: val => `${val}`,
    sortable: true
  },
  { name: 'med_name', align: 'center', label: 'Название', field: row => row.med_name, sortable: true },
  { name: 'med_category', align: 'center', label: 'Категория', field: row => row.med_catagory, sortable: true },
  { name: 'med_dosage', align: 'center', label: 'Доза', field: row => row.med_dosage, sortable: true },
  { name: 'med_price', align: 'center', label: 'Цена(руб.)', field: row => row.med_price, sortable: true },
  { name: 'med_expiration_date', align: 'center', label: 'Истечение срока годности', field: row => row.med_expiration_date, sortable: true },
  { name: 'med_receipts', align: 'center', label: 'Дата поступления', field: row => row.med_receipts, sortable: true },
  { name: 's_name', align: 'center', label: 'Поставщик', field: row => row.s_name, sortable: true },


  //кнопки для манипуляции с данными
  { name: 'delete', label: 'Удаление медикамента', align: 'center', }
  ],
})


//получить информацию о складе по его id
function getInfoWarehouse(){
  axios.get(
    `https://zdorovie.space/api/v1/warehouse/${route.params.w_id}`, {
      headers: {Authorization: `Bearer ${localStorage.getItem('access_token')}`}
    }
  )
  .then((response)=>{
    state.w_id = response.data.warehouse_info.w_id;
    state.w_address = response.data.warehouse_info.w_address;
    state.w_director = response.data.warehouse_info.w_director;
    state.w_phone_number = response.data.warehouse_info.w_phone_number;
    state.medication = response.data.medications
  }
  )
  .catch(function(error){
    returnToLigonPage()
  })
}

//функция добавление медикамента на склад
function addMedicationToWareHouse(){
  for (let index = 0; index < state.selected_med.length; index++) {
      axios.post(
        "https://zdorovie.space/api/v1/medication-warehouse",{
          w_id : state.w_id,
          med_id: state.selected_med[index]
        }
      )
    
  };
  state.addCard = false;
  getInfoWarehouse();
}

//функция удаление медикамента со склада
function deleteMed(med_id){
  axios.delete(
    `https://zdorovie.space/api/v1/medication-warehouse/${state.w_id}-${med_id}`
  ).then(async()=>{
    getInfoWarehouse();
  }
  )
}



onMounted(async ()=>{
  getInfoWarehouse();
  state.all_medication = await getMed();
})
</script>