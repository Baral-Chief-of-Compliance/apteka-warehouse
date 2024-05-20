<template>
  <q-page>
    <!-- <div class="text-center text-h3">Аптеки</div> -->



    <div class="q-pa-md">


      <q-table
        class="q-mt-xl"
        title="Медикаменты в базе данных"
        :rows="state.medication"
        :columns="state.columns"
        row-key="name"
      >


      <!-- изменяем отображение первого столбца -->
      <template v-slot:body-cell-ph_id="props">
        <q-td :props="props">
          <b>{{ props.row.med_id}}</b>
        </q-td>
      </template>

      <!-- Изменяем отображение для колонки информации о медикаменте -->
      <template v-slot:body-cell-info="props">
        <q-td :props="props">
          <q-btn  color="primary" icon="info"></q-btn>
        </q-td>
      </template>


      <!-- изменяем отображение для колонки обновление данных -->
      <template v-slot:body-cell-update="props">

        <q-td :props="props">
          <q-btn v-if="checkRightsAdminManager()" color="orange" icon="mode_edit" @click="showUpdateCard(
            props.row.med_name,
            props.row.med_category,
            props.row.med_dosage,
            props.row.med_price,
            props.row.med_expiration_date,
            props.row.med_receipts,
            props.row.supplierID,
            props.row.med_id
            )"></q-btn>
        </q-td>
      </template>

      <!-- изменяем отображение для колонки удаление данных -->
      <template v-slot:body-cell-delete="props">
        <q-td :props="props">
          <q-btn v-if="checkRightsAdminManager()" color="red" icon="delete" @click="deleteMed(props.row.med_id)"></q-btn>
        </q-td>
      </template>
    
      </q-table>


      <!-- кнопка для добавлени медикаментов -->
      <div v-if="checkRightsAdminManager()" class="q-mt-xl column">
        <q-btn  color="green" icon="add" label="Добавить медикамент" @click="state.addCard = true" />
      </div>
    </div>

    <!-- диалоговое окно для добавление медикамента -->
    <q-dialog v-model="state.addCard" persistent>
      <q-card>
        <q-card-section class="items-center">

          <!-- заголовок карточки -->
          <div class="row">
            <q-avatar icon="medication" color="green" text-color="white" />
            <span class="q-ma-sm text-h5">Добавить новый медикамент</span>
          </div>

          
          <!-- инпуты для введения данных об новом медикамент-->
          <div>
            <q-input  type="text" label="Название" v-model="state.add_med_name" />
            <q-input  type="text" label="Категория" v-model="state.add_med_category" />
            <q-input type="number" step="0.01" label="Доза" v-model=state.add_med_dosage />
            <q-input type="number" step="0.01" min="0.00" max="10000.00" label="Цена" v-model=state.add_med_price />
            <q-input type="date" label="Истечение срока годности" v-model=state.add_med_expiration_date />
            <q-input type="date" label="Дата поступления" v-model=state.add_med_receipts />


          </div>
          <span class="q-ma-xl text-h6 center">Выберите поставщика</span>
          <div class="column">
            <q-radio v-for="s in state.supplier" :key="s.s_id" v-model="state.add_supplierID" :val="s.s_id" :label="s.s_name" />
          </div>
        </q-card-section>

        <!-- кнопки для взамиодействия карточкой -->
        <q-card-actions align="right">
          <q-btn flat label="Отмена" color="red" v-close-popup />

          <!-- кнопка для добавления медикамента, появялется при условии -->
          <q-btn v-if="state.add_supplierID != null" 
          flat label="Добавить" color="green" @click="addMed()" />
        </q-card-actions>
      </q-card>
    </q-dialog>
    <!-- конец диалогового окна для добавление медикамента -->


    <!-- диалоговое окно для обновления данных о медекаменте -->
    <q-dialog v-model="state.updateCard" persistent>
      <q-card>
        <q-card-section class="items-center">

          <!-- заголовки карточки -->
          <div class="row">
            <q-avatar icon="medication" color="orange" text-color="white" />
            <span class="q-ma-sm text-h5">Обновить данные медикамента</span>
          </div>
            
          <!-- инпуты для обновления данных медикамента -->
          <div>
            <q-input type="text" label="Название" v-model="state.update_med_name" />
            <q-input type="text" label="Категория" v-model="state.update_med_category" />
            <q-input type="number" step="0.01" label="Доза" v-model=state.update_med_dosage />
            <q-input type="number" step="0.01" label="Цена" min="0.00" max="10000.00" v-model=state.update_med_price />
            <q-input type="date" label="Истечение срока годности" v-model=state.update_med_expiration_date />
            <q-input type="date" label="Дата поступления" v-model=state.update_med_receipts />
          </div>
          <span class="q-ma-xl text-h6 center">Выберите поставщика</span>
          <div class="column">
            <q-radio v-for="s in state.supplier" :key="s.s_id" v-model="state.update_supplierID" :val="s.s_id" :label="s.s_name" />
          </div>
          

        </q-card-section>
        <q-card-actions align="right">
          <q-btn flat label="Отмена" color="red" v-close-popup />
          <q-btn 
            v-if="true"
            flat label="Обновить" color="orange" @click="updateMed()" />
        </q-card-actions>
      </q-card>
    </q-dialog>
    <!-- конец диалового окна для обновления данных о медикаменте -->

  </q-page>
</template>

<script setup> 
import axios from 'axios';
import { onMounted, onUpdated, reactive, inject } from 'vue';


//берем функцию для получения всех поставщиков
const { getSupplier } = inject('supplier');
//берем функцию для получения всех медикаментов
const { getMed } = inject('med');

//функция для получения роли пользователя
const { getRole } = inject('role');

//функция для проверки прва для админа и манагера склада
const { checkRightsAdminManager } = inject('role');




//сотояние страницы
const state = reactive({

//поставщики
supplier: [],


//айдишник чтобы добавить поставщика
add_supplierID: null,

//айдишник для обновления поставщика
update_supplierID: null,

addCard: false, //параметр для отображение карты с добавлением медикамента

updateCard: false, //параметр для отображения карты с обновлением параметров медикаментов

// параметры для добавления нового медикамента
add_med_name: "",
add_med_category: "",
add_med_dosage: "",
add_med_price: "",
add_med_expiration_date: "",
add_med_receipts: "",
//


//параметры для обнолвения медикамента
update_med_name: "",
update_med_category: "",
update_med_dosage: "",
update_med_price: "",
update_med_expiration_date: "",
update_med_receipts: "",
update_med_id: "",
//

medication : [],
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
{ name: 'med_category', align: 'center', label: 'Категория', field: row => row.med_category, sortable: true },
{ name: 'med_dosage', align: 'center', label: 'Доза', field: row => row.med_dosage, sortable: true },
{ name: 'med_price', align: 'center', label: 'Цена(руб.)', field: row => row.med_price, sortable: true },
{ name: 'med_expiration_date', align: 'center', label: 'Истечение срока годности', field: row => row.med_expiration_date, sortable: true },
{ name: 'med_receipts', align: 'center', label: 'Дата поступления', field: row => row.med_receipts, sortable: true },


//кнопки для манипуляции с данными
// { name: 'info', label: 'Иформация', align: 'center'},
{ name: 'update', label: 'Изменение данных', align: 'center'},
{ name: 'delete', label: 'Удаление медикамента', align: 'center', }
],

})

// функция для добавления медикамента
function addMed(){
axios.post(
  "https://zdorovie.space/api/v1/medication",
  {
    med_name: state.add_med_name,
    med_category: state.add_med_category,
    med_dosage: state.add_med_dosage,
    med_price: state.add_med_price,
    med_expiration_date: state.add_med_expiration_date,
    med_receipts: state.add_med_receipts,
    supplierID: state.add_supplierID
  }
).then(async (response) =>{
  state.medication = await getMed();
  state.addCard = false
}

);
}

// функция для удаления медикамента
function deleteMed(med_id){
axios.delete(
  `https://zdorovie.space/api/v1/medication/${med_id}`
).then(async () => {
  state.medication = await getMed();
})
}

//функция для отображение карточки обновления данных о медикаменте
function showUpdateCard(
  med_name, 
  med_category, 
  med_dosage, 
  med_price,
  med_expiration_date,
  med_receipts,
  supplierID,
  med_id
)
{
state.update_med_name = med_name;
state.update_med_category = med_category;
state.update_med_dosage = med_dosage;
state.update_med_price = med_price;
state.update_med_expiration_date = med_expiration_date;
state.update_med_receipts = med_receipts;
state.update_supplierID = supplierID;
state.update_med_id = med_id;
state.updateCard = true;
}

//функция для обновления данных о медикаменте
function updateMed(){
axios.put(
  `https://zdorovie.space/api/v1/medication/${state.update_med_id}`,
  {
    med_id: state.update_med_id,
    med_name: state.update_med_name,
    med_category: state.update_med_category,
    med_dosage: state.update_med_dosage,
    med_price: state.update_med_price,
    med_expiration_date: state.update_med_expiration_date,
    med_receipts: state.update_med_receipts,
    supplierID: state.update_supplierID
  }
).then(async () => {
  state.medication = await getMed();
  state.updateCard = false;
})
}


//хук жизни mounted
onMounted(async () =>{
  state.supplier = await getSupplier();
  state.medication = await getMed();
})

</script>