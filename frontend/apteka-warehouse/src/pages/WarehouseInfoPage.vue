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



      </div>


      <!-- кнопка чтобы добавить склад -->
      <div class="q-mt-xl column">
        <q-btn color="green" icon="add" label="Добавить медикаментов на склад" @click="state.addCard=true, state.selected_med = []" />
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
            <q-btn v-if="state.selected_med.length != 0" flat label="Добавить" color="green" v-close-popup />
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


  addCard: false   //карточка добавление медикамента
})

function getInfoWarehouse(){
  axios.get(
    `http://localhost:5000/warehouse/${route.params.w_id}`
  )
  .then((response)=>{
    state.w_id = response.data.warehouse_info.w_id;
    state.w_address = response.data.warehouse_info.w_address;
    state.w_director = response.data.warehouse_info.w_director;
    state.w_phone_number = response.data.warehouse_info.w_phone_number;
  }
  )
}


onMounted(async ()=>{
  getInfoWarehouse();
  state.all_medication = await getMed();
})
</script>