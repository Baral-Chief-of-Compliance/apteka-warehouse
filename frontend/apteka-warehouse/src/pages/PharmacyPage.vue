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

        <!-- изменяем отображение стоблца с кнопками
        <template v-slot:body-cell-actions="props">
          <q-td :props="props">
            <q-btn icon="mode_edit" @click="onEdit(props.row)"></q-btn>
            <q-btn icon="delete" @click="onDelete(props.row)"></q-btn>
          </q-td>
        </template> -->



        <!-- изменяем отображение для колонки обновление данных -->
        <template v-slot:body-cell-update="props">

          <q-td :props="props">
            <q-btn color="orange" icon="mode_edit" @click="onEdit(props.row)"></q-btn>
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
          <q-card-section class="column items-center">

            <!-- заголовок карточки -->
            <div class="row">
              <q-avatar icon="domain" color="primary" text-color="white" />
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
            <q-btn flat label="Добавить" color="green" @click="addPharmacy()" />
          </q-card-actions>
        </q-card>
      </q-dialog>

    </q-page>
  </template>

<script setup> 
import axios from 'axios';
import { onMounted, onUpdated, reactive } from 'vue';




//сотояние страницы
const state = reactive({


  addCard: false, //параметр для отображение карты с добавлением аптеки

  // параметры для добавления новой аптеки
  add_pharmacy_name: "",
  add_pharmacy_address: "",
  add_pharmacy_phone: "",
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


//хук жизни mounted
onMounted(() =>{
  getPharmacy()
})

//при хуке жизни update мы вызываем обновление аптек
onUpdated(() => {
  getPharmacy()
})
</script>