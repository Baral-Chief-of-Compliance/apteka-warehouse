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
    "https://zdorovie.space/api/v1/supplier", {
      headers: {Authorization: `Bearer ${localStorage.getItem('access_token')}`}
    }
  )
  .then((response) => {
    return response.data.suppliers;
  }
  )
  .catch(function(error){
    returnToLigonPage()
  })
}


// функция получения всех медикаментов
function getMed(){
  return axios.get(
    "https://zdorovie.space/api/v1/medication", {
      headers: {Authorization: `Bearer ${localStorage.getItem('access_token')}`}
    }
  )
  .then((response) =>{
    return response.data.medication;
  }
  )
  .catch(function(error){
    returnToLigonPage()
  })
}



//функция для получения всех аптек
function getPharmacy(){
  return axios.get(
    "https://zdorovie.space/api/v1/pharmacy", {
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

//функция для получение роли пользователя
function getRole(){
  return localStorage.getItem('role')
}

//функция для проверки прав админа и манагера
function checkRightsAdminManager(){
  return getRole() === 'admin' | getRole() === 'руководитель склада'
}

//функция для проверки прав админа, манагера и манагер аптеки
function checkRightsAdminManagerPhManager(){
  return getRole() === 'admin' | getRole() === 'руководитель склада' | getRole() === 'директор аптечного склада'
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

provide('role', {
  getRole,
  checkRightsAdminManager,
  checkRightsAdminManagerPhManager
});


defineOptions({
  name: 'App'
});
</script>
