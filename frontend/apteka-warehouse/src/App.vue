<template>
  <router-view />
</template>

<script setup>
import { provide } from 'vue';
import axios from 'axios';


// функция получения всех поставщиков
function getSupplier(){
  return axios.get(
    "http://localhost:5000/supplier"
  )
  .then((response) => {
    return response.data.suppliers;
  }
  )
}


// функция получения всех медикаментов
function getMed(){
  return axios.get(
    "http://localhost:5000/medication"
  )
  .then((response) =>{
    return response.data.medication;
  }
  )
}

provide('supplier', {
  getSupplier
});

provide('med', {
  getMed
});

defineOptions({
  name: 'App'
});
</script>
