<template>
  <router-view />
</template>

<script setup>
import { provide} from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

//роутер
const router = useRouter()


//возвращение на страницу с логином
function returnToLigonPage(){
  router.push({name: 'Login'})
}


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



//функция для получения всех аптек
function getPharmacy(){
  return axios.get(
    "http://localhost:5000/pharmacy", {
      headers: {Authorization: `Bearer ${localStorage.getItem('access_token')}`}
    }
  )
  .then((response)=> {
    return response.data.pharmacys;
  })
  .catch(function(error){
    returnToLigonPage()
  })
}

provide('supplier', {
  getSupplier
});

provide('med', {
  getMed
});

provide('pharmacy', {
  getPharmacy
});

defineOptions({
  name: 'App'
});
</script>
