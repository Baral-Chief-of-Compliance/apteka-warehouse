<template>
    <q-page class="flex flex-center">
        <q-card class="my-card">
            <img height="300px" src="https://img.freepik.com/free-photo/packings-of-pills-and-capsules-of-medicines_1339-2254.jpg">
            <q-card-section>
                <div class="text-h6">ООО "Здоровье"</div>
                <div class="text-subtitle2">Административная панель</div>
            </q-card-section>
            <q-card-section>
                <q-input v-model="state.login" type="text" label="Логин" />
                <q-input v-model="state.pwd"  type="password" label="Пароль"  />


                
                <!-- баннер с ошибкой авторизации -->
                <div v-if="state.mistakeStatus" class="q-my-md text-center">
                    <q-banner inline-actions class="text-white bg-red">
                        <div class="text-h6">Ошибка авторизации</div>
                    </q-banner>
                </div>

                <!-- баннер с тем, что пользоваетль успешно авторизован -->
                <div v-if="state.successEnter" class="q-my-md text-center">
                    <q-banner inline-actions class="text-white bg-green">
                        <div class="text-h6">Успешеная авторизация</div>
                    </q-banner>
                </div>


                <div class="q-pa-md column">
                    <q-btn size="md" color="primary" label="Войти" @click="login()" />
                </div>
                
            </q-card-section>
        </q-card>
    </q-page>
</template>

<script setup>
import axios from 'axios';
import { reactive } from 'vue';


// реактивное состояние страницы
const state = reactive({
    login: "",
    pwd: "",
    mistakeStatus: false,
    successEnter: false,
})

//конфигурационный заголовок для входа
const config = {
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
}


// функция для входа в приложение
function login(){
    axios.post("http://localhost:5000/token",{
        username: state.login,
        password: state.pwd
    }, config)
    .then(function (response) {
        state.mistakeStatus = false;
        state.successEnter = true;
        
        // помещаем токен в локал сторадж для хранения
        localStorage.setItem("access_token", response.data.access_token)
    })
    .catch(function (error) {
        console.log(error);
        console.log("ошибка авторизации");
        state.successEnter = false;
        state.mistakeStatus = true;
    });
}

defineOptions({
  name: 'LoginPage'
});
</script>