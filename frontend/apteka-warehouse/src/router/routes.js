const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { 
        path: '', 
        component: () => import('pages/IndexPage.vue'),
        name: 'Index'
      },

      // склады
      {
        path: '/warehouse',
        component: () => import('pages/WarehousePage.vue'),
        name: 'Warehouse'
      },

      //поставщики
      {
        path: '/supplier',
        component: () => import('pages/SupplierPage.vue'),
        name: 'Supplier'
      },

      //аптеки
      {
        path: '/pharmacy',
        component: () => import('pages/PharmacyPage.vue'),
        name: 'Pharmacy'
      },

      //медикаменты
      {
        path: '/medication',
        component: () => import('pages/MedicationPage.vue'),
        name: 'Medication'
      },

      // заказы
      {
        path: '/order',
        component: () => import('pages/OrderPage.vue'),
        name: 'Order'
      },


      //пользователи
      {
        path: '/users',
        component: () => import('pages/UsersPage.vue'),
        name: 'Users'
      }
    ]
  },

  {
    path: '/login',
    component: () => import('layouts/LoginLayout.vue'),
    children : [
      { 
        path: '', 
        component: () => import('pages/LoginPage.vue'),
        name: 'Login'
      }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
