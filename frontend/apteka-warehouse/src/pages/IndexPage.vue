<template>
  <q-page class="flex flex-center">
    <!-- <img
      alt="Quasar logo"
      src="~assets/quasar-logo-vertical.svg"
      style="width: 200px; height: 200px"
    > -->
    главная страница
  </q-page>
</template>

<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';


//роутер
const router = useRouter()

defineOptions({
  name: 'IndexPage'
});


onMounted(()=>{
  router.push({name: 'Order'});
})
</script>
