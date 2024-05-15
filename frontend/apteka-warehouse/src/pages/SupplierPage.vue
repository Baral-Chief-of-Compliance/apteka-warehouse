<template>
  <q-page>
    <!-- <div class="text-center text-h3">Аптеки</div> -->



    <div class="q-pa-md">


      <q-table
        class="q-mt-xl"
        title="Поставщики в базе данных"
        :rows="state.supplier"
        :columns="state.columns"
        row-key="name"
      >


      <!-- изменяем отображение первого столбца -->
      <template v-slot:body-cell-ph_id="props">
        <q-td :props="props">
          <b>{{ props.row.s_id}}</b>
        </q-td>
      </template>

      <!-- Изменяем отображение для колонки информации о поставщике -->
      <template v-slot:body-cell-info="props">
        <q-td :props="props">
          <q-btn color="primary" icon="info"></q-btn>
        </q-td>
      </template>


      <!-- изменяем отображение для колонки обновление данных -->
      <template v-slot:body-cell-update="props">

        <q-td :props="props">
          <q-btn color="orange" icon="mode_edit" @click="showUpdateCard(
            props.row.s_name,
            props.row.s_id
            )"></q-btn>
        </q-td>
      </template>

      <!-- изменяем отображение для колонки удаление данных -->
      <template v-slot:body-cell-delete="props">
        <q-td :props="props">
          <q-btn color="red" icon="delete" @click="deleteSupplier(props.row.s_id)"></q-btn>
        </q-td>
      </template>
    
      </q-table>


      <!-- кнопка для добавлени поставщика -->
      <div class="q-mt-xl column">
        <q-btn  color="green" icon="add" label="Добавить поставщика" @click="state.addCard = true" />
      </div>
    </div>

    <!-- диалоговое окно для добавление gjcnfdobrf -->
    <q-dialog v-model="state.addCard" persistent>
      <q-card>
        <q-card-section class="items-center">

          <!-- заголовок карточки -->
          <div class="row">
            <q-avatar icon="chat" color="green" text-color="white" />
            <span class="q-ma-sm text-h5">Добавить нового поставщика</span>
          </div>

          
          <!-- инпуты для введения данных об новом поставщике-->
          <div>
            <q-input  type="text" label="Имя поставщика" v-model="state.add_supplier_name" />
          </div>
        </q-card-section>

        <!-- кнопки для взамиодействия карточкой -->
        <q-card-actions align="right">
          <q-btn flat label="Отмена" color="red" v-close-popup />

          <!-- кнопка для добавления поставщика, появялется при условии -->
          <q-btn v-if="state.add_supplier_name.length > 0" 
          flat label="Добавить" color="green" @click="addSupplier()" />
        </q-card-actions>
      </q-card>
    </q-dialog>
    <!-- конец диалогового окна для добавление поставщика -->


    <!-- диалоговое окно для обновления данных о поставщике -->
    <q-dialog v-model="state.updateCard" persistent>
      <q-card>
        <q-card-section class="items-center">

          <!-- заголовки карточки -->
          <div class="row">
            <q-avatar icon="chat" color="orange" text-color="white" />
            <span class="q-ma-sm text-h5">Обновить данные поставщика</span>
          </div>
            
          <!-- инпуты для обновления данных поставщика -->
          <div>
            <q-input  type="text" label="Имя поставщика" v-model="state.update_supplier_name" />
          </div>
          

        </q-card-section>
        <q-card-actions align="right">
          <q-btn flat label="Отмена" color="red" v-close-popup />
          <q-btn 
            v-if="state.update_supplier_name.length > 0"
            flat label="Обновить" color="orange" @click="updateSupplier()" />
        </q-card-actions>
      </q-card>
    </q-dialog>
    <!-- конец диалового окна для обновления данных о поставщике -->

  </q-page>
</template>

<script setup> 
import axios from 'axios';
import { onMounted, onUpdated, reactive } from 'vue';




//сотояние страницы
const state = reactive({


addCard: false, //параметр для отображение карты с добавлением склада

updateCard: false, //параметр для отображения карты с обновлением параметров склада

// параметры для добавления нового поставщика
add_supplier_name: "",
//


//параметры для обнолвения нового поставщика
update_supplier_name: "",
update_s_id: "",
//

supplier : [],
columns : [
{
  name: 's_id',
  required: true,
  label: 'Индекс',
  align: 'center',
  field: row => row.s_id,
  format: val => `${val}`,
  sortable: true
},
{ name: 's_name', align: 'center', label: 'Имя поставщика', field: row => row.s_name, sortable: true },
{ name: 'info', label: 'Иформация', align: 'center'},
{ name: 'update', label: 'Изменение данных', align: 'center'},
{ name: 'delete', label: 'Удаление склада', align: 'center', }
],

})

// функция получения всех поставщиков
function getSupplier(){
axios.get(
  "http://localhost:5000/supplier"
)
.then(function(response){
  state.supplier = response.data.suppliers;
}
)
}

// функция для добавления поставщика
function addSupplier(){
axios.post(
  "http://localhost:5000/supplier",
  {
    s_name: state.add_supplier_name,
  }
).then(function(response){
  getSupplier();
  state.addCard = false;
}

);
}

// функция для удаления поставщика
function deleteSupplier(s_id){
axios.delete(
  `http://localhost:5000/supplier/${s_id}`
).then(() => {
  getSupplier();
})
}

//функция для отображение карточки обновления данных о поставщике
function showUpdateCard(s_name, s_id){
state.update_supplier_name = s_name;
state.update_s_id = s_id;
state.updateCard = true;
}

//функция для обновления данных о поставщике
function updateSupplier(){
axios.put(
  `http://localhost:5000/supplier/${state.update_s_id}`,
  {
    s_id: state.update_s_id,
    s_name: state.update_supplier_name
  }
).then(() => {
  getSupplier();
  state.updateCard = false;
})
}


//хук жизни mounted
onMounted(() =>{
  getSupplier()
})

//при хуке жизни update мы вызываем обновление поставщиков
onUpdated(() => {
  getSupplier()
})
</script>