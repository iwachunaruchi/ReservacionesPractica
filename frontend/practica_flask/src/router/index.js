import { createRouter, createWebHistory } from 'vue-router'
import index from '../views/index.vue'
import details from '@/views/reservation/details/detailsProp.vue'
import login from '@/views/auth/login.vue'
import register from '@/views/auth/register.vue'
import User from '@/views/reservation/ReservationUser/User.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: index,
    },
    {
      path:'/register',
      name:'registro',
      component: register
    },
    {
      path:'/login',
      name:'login',
      component: login
    },
    {
      path:'/details/:id',
      name:'detalles',
      component:details,
      
    },
    {
      path:'/reservations',
      name:'reservations',
      component:User
    }
  ],
})

export default router
