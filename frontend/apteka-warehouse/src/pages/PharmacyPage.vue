<template>
    <q-page>
      <!-- <div class="text-center text-h3">Аптеки</div> -->



      <div class="q-pa-md">


        <q-table
          class="q-mt-xl"
          title="Аптеки в базе данных"
          :rows="state.pharmacys"
          :columns="state.columns"
          row-key="name"
        >


        <!-- изменяем отображение первого столбца -->
        <template v-slot:body-cell-ph_id="props">
          <q-td :props="props">
            <b>{{ props.row.ph_id}}</b>
          </q-td>
        </template>

        <!-- Изменяем отображение для колонки информации об аптеки -->
        <template v-slot:body-cell-info="props">
          <q-td :props="props">
            <q-btn color="primary" icon="info"></q-btn>
          </q-td>
        </template>


        <!-- изменяем отображение для колонки обновление данных -->
        <template v-slot:body-cell-update="props">

          <q-td :props="props">
            <q-btn color="orange" icon="mode_edit" @click="showUpdateCard(
              props.row.ph_name,
              props.row.ph_address,
              props.row.ph_phone_number,
              props.row.ph_id
              )"></q-btn>
          </q-td>
        </template>

        <!-- изменяем отображение для колонки удаление данных -->
        <template v-slot:body-cell-delete="props">
          <q-td :props="props">
            <q-btn color="red" icon="delete" @click="deletePharmacy(props.row.ph_id)"></q-btn>
          </q-td>
        </template>
      
        </q-table>


        <!-- кнопка для добавлени аптеки -->
        <div class="q-mt-xl column">
          <q-btn  color="green" icon="add" label="Добавить аптеку" @click="state.addCard = true" />
        </div>
      </div>

      <!-- диалоговое окно для добавление аптеки -->
      <q-dialog v-model="state.addCard" persistent>
        <q-card>
          <q-card-section class="items-center">

            <!-- заголовок карточки -->
            <div class="row">
              <q-avatar icon="domain" color="green" text-color="white" />
              <span class="q-ma-sm text-h5">Добавить новую аптеку</span>
            </div>

            
            <!-- инпуты для введения данных об новой аптеки -->
            <div>
              <q-input  type="text" label="Название" v-model="state.add_pharmacy_name" />
              <q-input  type="text" label="Адрес" v-model="state.add_pharmacy_address" />
              <q-input type="text" label="Номер телефона" v-model=state.add_pharmacy_phone />
            </div>
          </q-card-section>

          <!-- кнопки для взамиодействия карточкой -->
          <q-card-actions align="right">
            <q-btn flat label="Отмена" color="red" v-close-popup />

            <!-- кнопка для добавления аптеки, появялется при условии -->
            <q-btn v-if="
            state.add_pharmacy_address.length > 0 &&
            state.add_pharmacy_name.length > 0 && 
            state.add_pharmacy_phone.length > 0
            " 
            flat label="Добавить" color="green" @click="addPharmacy()" />
          </q-card-actions>
        </q-card>
      </q-dialog>
      <!-- конец диалогового окна для добавление аптеки -->


      <!-- диалоговое окно для обновления данных об аптеки -->
      <q-dialog v-model="state.updateCard" persistent>
        <q-card>
          <q-card-section class="items-center">

            <!-- заголовки карточки -->
            <div class="row">
              <q-avatar icon="domain" color="orange" text-color="white" />
              <span class="q-ma-sm text-h5">Обновить данные аптеки</span>
            </div>
              
            <!-- инпуты для обновления данных аптеки -->
            <div>
              <q-input  type="text" label="Название" v-model="state.update_pharmacy_name" />
              <q-input  type="text" label="Адрес" v-model="state.update_pharmacy_address" />
              <q-input type="text" label="Номер телефона" v-model=state.update_pharmacy_phone />
            </div>
            

          </q-card-section>
          <q-card-actions align="right">
            <q-btn flat label="Отмена" color="red" v-close-popup />
            <q-btn 
              v-if="
                state.update_pharmacy_name.length > 0 &&
                state.update_pharmacy_address.length > 0 &&
                state.update_pharmacy_phone.length > 0
              "
              flat label="Обновить" color="orange" @click="updatePharmacy()" />
          </q-card-actions>
        </q-card>
      </q-dialog>
      <!-- конец диалового окна для обновления данных об аптеки -->

    </q-page>
  </template>

<script setup> 
import axios from 'axios';
import { onMounted, onUpdated, reactive } from 'vue';




//сотояние страницы
const state = reactive({


  addCard: false, //параметр для отображение карты с добавлением аптеки

  updateCard: false, //параметр для отображения карты с обновлением параметров аптеки

  // параметры для добавления новой аптеки
  add_pharmacy_name: "",
  add_pharmacy_address: "",
  add_pharmacy_phone: "",
  //


  //параметры для обнолвения новой аптеки
  update_pharmacy_name: "",
  update_pharmacy_address: "",
  update_pharmacy_phone: "",
  update_ph_id: "",
  //

  pharmacys : [],
  columns : [
  {
    name: 'ph_id',
    required: true,
    label: 'Индекс',
    align: 'center',
    field: row => row.ph_id,
    format: val => `${val}`,
    sortable: true
  },
  { name: 'ph_name', align: 'center', label: 'Наименование', field: row => row.ph_name, sortable: true },
  { name: 'ph_address', align: 'center', label: 'Адрес', field: row => row.ph_address, sortable: true },
  { name: 'ph_phone_number', align: 'center', label: 'Номер телефона', field: row => row.ph_phone_number, sortable: true },
  { name: 'info', label: 'Иформация', align: 'center'},
  { name: 'update', label: 'Изменение данных', align: 'center'},
  { name: 'delete', label: 'Удаление аптеки', align: 'center', }
  // { name: 'carbs', label: 'Carbs (g)', field: 'carbs' },
  // { name: 'protein', label: 'Protein (g)', field: 'protein' },
  // { name: 'sodium', label: 'Sodium (mg)', field: 'sodium' },
  // { name: 'calcium', label: 'Calcium (%)', field: 'calcium', sortable: true, sort: (a, b) => parseInt(a, 10) - parseInt(b, 10) },
  // { name: 'iron', label: 'Iron (%)', field: 'iron', sortable: true, sort: (a, b) => parseInt(a, 10) - parseInt(b, 10) }
],

})

// функция получения всех аптек
function getPharmacy(){
  axios.get(
    "http://localhost:5000/pharmacy"
  )
  .then(function(response){
    state.pharmacys = response.data.pharmacys;
  }
  )
}

// функция для добавления аптеки
function addPharmacy(){
  axios.post(
    "http://localhost:5000/pharmacy",
    {
      ph_address: state.add_pharmacy_address,
      ph_phone_number: state.add_pharmacy_phone,
      ph_name: state.add_pharmacy_name
    }
  ).then(function(response){
    getPharmacy();
    state.addCard = false
  }

  );
}

// функция для удаления аптеки
function deletePharmacy(ph_id){
  axios.delete(
    `http://localhost:5000/pharmacy/${ph_id}`
  ).then(() => {
    getPharmacy();
  })
}

//функция для отображение карточки обновления данных об аптеки
function showUpdateCard(ph_name, ph_address, ph_phone_number, ph_id){
  state.update_pharmacy_name = ph_name;
  state.update_pharmacy_address = ph_address;
  state.update_pharmacy_phone = ph_phone_number;
  state.update_ph_id = ph_id;
  state.updateCard = true;
}

//функция для обновления данных об аптеки
function updatePharmacy(){
  axios.put(
    `http://localhost:5000/pharmacy/${state.update_ph_id}`,
    {
      ph_id: state.update_ph_id,
      ph_address: state.update_pharmacy_address,
      ph_phone_number: state.update_pharmacy_phone,
      ph_name: state.update_pharmacy_name
    }
  ).then(() => {
    getPharmacy();
    state.updateCard = false;
  })
}


//хук жизни mounted
onMounted(() =>{
  getPharmacy()
})

//при хуке жизни update мы вызываем обновление аптек
onUpdated(() => {
  getPharmacy()
})
</script>