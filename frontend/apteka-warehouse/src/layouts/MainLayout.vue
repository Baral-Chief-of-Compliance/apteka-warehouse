<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title>
          ООО "Здоровье"
        </q-toolbar-title>
        <div>{{ getUserName() }}|{{ getUserRole() }}</div>
        <q-btn class="q-mx-xl"  color="red" icon="close" label="ВЫЙТИ" @click="exitFromApp()" />
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
    >
      <q-list>
        <q-item-label
          header
        >
          Навигация
        </q-item-label>

        <EssentialLink
          v-for="link in linksList"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { ref } from 'vue';
import EssentialLink from 'components/EssentialLink.vue';
import { useRouter } from 'vue-router';


defineOptions({
  name: 'MainLayout'
})

const linksList = [
  {
    title: 'Склады',
    caption: 'просмотр, добавление, удаление',
    icon: 'warehouse',
    link: 'Warehouse'
  },
  {
    title: 'Аптеки',
    caption: 'просмотр, добавление, удаление',
    icon: 'domain',
    link: 'Pharmacy'
  },
  {
    title: 'Поставщики',
    caption: 'просмотр, добавление, удаление',
    icon: 'chat',
    link: 'Supplier'
  },
  {
    title: 'Медикаменты',
    caption: 'просмотр, добавление, удаление',
    icon: 'medication',
    link: 'Medication'
  },
  {
    title: 'Заказы',
    caption: 'просмотр, добавление, удаление',
    icon: 'circle',
    link: 'Order'
  },
  // {
  //   title: 'Пользователи',
  //   caption: 'просмотр, добавление, удаление',
  //   icon: 'person',
  //   link: 'Users'
  // }
]


//получить имя пользовает
function getUserName(){
  return localStorage.getItem('username');
}

//получить роль пользователя
function getUserRole(){
  return localStorage.getItem('role');
}

const leftDrawerOpen = ref(false)

function toggleLeftDrawer () {
  leftDrawerOpen.value = !leftDrawerOpen.value
}


const router = useRouter()

// функция для выхода из приложения
function exitFromApp(){
  localStorage.removeItem("access_token");
  localStorage.removeItem('username');
  localStorage.removeItem('role');
  router.push({name: "Login"})
}
</script>
