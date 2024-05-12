<template>
    <q-page class="flex flex-center">
        <q-card class="my-card">
            <img src="https://izvestiaur.ru/upload/resize_cache/iblock/cb4/3pz6o3i7kh0jttgrh3rroqueh54k7z3m/888_500_2/lekarstva.jpg">
            <q-card-section>
                <div class="text-h6">ООО "Здоровье"</div>
                <div class="text-subtitle2">Административная панель</div>
            </q-card-section>
            <q-card-section>
                <q-input v-model="text" type="text" label="Логин" />
                <q-input v-model="text" type="text" label="Пароль" />
                <div class="q-pa-md column">
                    <q-btn color="primary" label="Войти" @click="onClick" />
                </div>
                
            </q-card-section>
        </q-card>
    </q-page>
</template>

<script setup>
defineOptions({
  name: 'LoginPage'
});
</script>