<template>
  <q-page>
    <!-- <div class="text-center text-h3">Аптеки</div> -->



    <div class="q-pa-md">


      <q-table
        class="q-mt-xl"
        title="Склады в базе данных"
        :rows="state.warehouse"
        :columns="state.columns"
        row-key="name"
      >


      <!-- изменяем отображение первого столбца -->
      <template v-slot:body-cell-ph_id="props">
        <q-td :props="props">
          <b>{{ props.row.w_id}}</b>
        </q-td>
      </template>

      <!-- Изменяем отображение для колонки информации об складе -->
      <template v-slot:body-cell-info="props">
        <q-td :props="props">
          <q-btn color="primary" icon="info" @click="router.push({name: 'WarehouseInfo', params: {w_id:props.row.w_id}})"></q-btn>
        </q-td>
      </template>


      <!-- изменяем отображение для колонки обновление данных -->
      <template v-slot:body-cell-update="props">

        <q-td :props="props">
          <q-btn v-if="checkRightsAdminManagerPhManager()" color="orange" icon="mode_edit" @click="showUpdateCard(
            props.row.w_director,
            props.row.w_address,
            props.row.w_phone_number,
            props.row.w_id
            )"></q-btn>
        </q-td>
      </template>

      <!-- изменяем отображение для колонки удаление данных -->
      <template v-slot:body-cell-delete="props">
        <q-td :props="props">
          <q-btn v-if="checkRightsAdminManagerPhManager()" color="red" icon="delete" @click="deleteWarehouse(props.row.w_id)"></q-btn>
        </q-td>
      </template>
    
      </q-table>


      <!-- кнопка для добавлени склада -->
      <div class="q-mt-xl column">
        <q-btn v-if="checkRightsAdminManagerPhManager()"  color="green" icon="add" label="Добавить склад" @click="state.addCard = true" />
      </div>
    </div>

    <!-- диалоговое окно для добавление склада -->
    <q-dialog v-model="state.addCard" persistent>
      <q-card>
        <q-card-section class="items-center">

          <!-- заголовок карточки -->
          <div class="row">
            <q-avatar icon="warehouse" color="green" text-color="white" />
            <span class="q-ma-sm text-h5">Добавить новый склад</span>
          </div>

          
          <!-- инпуты для введения данных об новом складе-->
          <div>
            <q-input  type="text" label="Директор" v-model="state.add_warehouse_director" />
            <q-input  type="text" label="Адрес" v-model="state.add_warehouse_address" />
            <q-input type="text" label="Номер телефона" v-model=state.add_warehouse_phone />
          </div>
        </q-card-section>

        <!-- кнопки для взамиодействия карточкой -->
        <q-card-actions align="right">
          <q-btn flat label="Отмена" color="red" v-close-popup />

          <!-- кнопка для добавления склада, появялется при условии -->
          <q-btn v-if="
          state.add_warehouse_address.length > 0 &&
          state.add_warehouse_director.length > 0 && 
          state.add_warehouse_phone.length > 0
          " 
          flat label="Добавить" color="green" @click="addWarehouse()" />
        </q-card-actions>
      </q-card>
    </q-dialog>
    <!-- конец диалогового окна для добавление склада -->


    <!-- диалоговое окно для обновления данных о складе -->
    <q-dialog v-model="state.updateCard" persistent>
      <q-card>
        <q-card-section class="items-center">

          <!-- заголовки карточки -->
          <div class="row">
            <q-avatar icon="warehouse" color="orange" text-color="white" />
            <span class="q-ma-sm text-h5">Обновить данные склада</span>
          </div>
            
          <!-- инпуты для обновления данных склада -->
          <div>
            <q-input  type="text" label="Директор" v-model="state.update_warehouse_director" />
            <q-input  type="text" label="Адрес" v-model="state.update_warehouse_address" />
            <q-input type="text" label="Номер телефона" v-model=state.update_warehouse_phone />
          </div>
          

        </q-card-section>
        <q-card-actions align="right">
          <q-btn flat label="Отмена" color="red" v-close-popup />
          <q-btn 
            v-if="
              state.update_warehouse_director.length > 0 &&
              state.update_warehouse_address.length > 0 &&
              state.update_warehouse_phone.length > 0
            "
            flat label="Обновить" color="orange" @click="updateWarehouse()" />
        </q-card-actions>
      </q-card>
    </q-dialog>
    <!-- конец диалового окна для обновления данных о складе -->

  </q-page>
</template>

<script setup> 
import axios from 'axios';
import { onMounted, onUpdated, reactive, inject } from 'vue';
import { useRouter } from 'vue-router';


//роутер
const router = useRouter();

//функция для проверки прва для админа и манагера склада
const { checkRightsAdminManager } = inject('role');

//функция для проверки прва для админа и манагера склада и манагера аптеки
const {checkRightsAdminManagerPhManager} = inject('role');

//сотояние страницы
const state = reactive({


addCard: false, //параметр для отображение карты с добавлением склада

updateCard: false, //параметр для отображения карты с обновлением параметров склада

// параметры для добавления нового склада
add_warehouse_director: "",
add_warehouse_address: "",
add_warehouse_phone: "",
//


//параметры для обнолвения нового склада
update_warehouse_director: "",
update_warehouse_address: "",
update_warehouse_phone: "",
update_w_id: "",
//

warehouse : [],
columns : [
{
  name: 'w_id',
  required: true,
  label: 'Индекс',
  align: 'center',
  field: row => row.w_id,
  format: val => `${val}`,
  sortable: true
},
{ name: 'w_director', align: 'center', label: 'Директор', field: row => row.w_director, sortable: true },
{ name: 'w_address', align: 'center', label: 'Адрес', field: row => row.w_address, sortable: true },
{ name: 'w_phone_number', align: 'center', label: 'Номер телефона', field: row => row.w_phone_number, sortable: true },
{ name: 'info', label: 'Иформация', align: 'center'},
{ name: 'update', label: 'Изменение данных', align: 'center'},
{ name: 'delete', label: 'Удаление склада', align: 'center', }
],

})

// функция получения всех складов
function getWarehouse(){
axios.get(
  "https://zdorovie.space/api/v1/warehouse"
)
.then(function(response){
  state.warehouse = response.data.warehouse;
}
)
}

// функция для добавления склада
function addWarehouse(){
axios.post(
  "https://zdorovie.space/api/v1/warehouse",
  {
    w_address: state.add_warehouse_address,
    w_phone_number: state.add_warehouse_phone,
    w_director: state.add_warehouse_director
  }
).then(function(response){
  getWarehouse();
  state.addCard = false
}

);
}

// функция для удаления склада
function deleteWarehouse(w_id){
axios.delete(
  `https://zdorovie.space/api/v1/warehouse/${w_id}`
).then(() => {
  getWarehouse();
})
}

//функция для отображение карточки обновления данных о складе
function showUpdateCard(w_director, w_address, w_phone_number, w_id){
state.update_warehouse_director = w_director;
state.update_warehouse_address = w_address;
state.update_warehouse_phone = w_phone_number;
state.update_w_id = w_id;
state.updateCard = true;
}

//функция для обновления данных о складе
function updateWarehouse(){
axios.put(
  `https://zdorovie.space/api/v1/warehouse/${state.update_w_id}`,
  {
    w_id: state.update_w_id,
    w_address: state.update_warehouse_address,
    w_phone_number: state.update_warehouse_phone,
    w_director: state.update_warehouse_director
  }
).then(() => {
  getWarehouse();
  state.updateCard = false;
})
}


//хук жизни mounted
onMounted(() =>{
  getWarehouse()
})

//при хуке жизни update мы вызываем обновление складов
onUpdated(() => {
  getWarehouse()
})
</script>