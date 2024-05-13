<template>
    <q-page class="flex flex-center">
        <q-card class="my-card">
            <img src="https://izvestiaur.ru/upload/resize_cache/iblock/cb4/3pz6o3i7kh0jttgrh3rroqueh54k7z3m/888_500_2/lekarstva.jpg">
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
        console.log(response);
        console.log(response.data.access_token);
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