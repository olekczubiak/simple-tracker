import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Home from '@/views/Home.vue'
import Login from '@/views/Login.vue'
import Register from '@/views/Register.vue'
import Panel from '@/views/Panel.vue'
import Analysis from '@/views/Analysis.vue'
import Monitor from '@/views/Monitor.vue'
import Calendar from '@/views/Calendar.vue'


const routes: Array<RouteRecordRaw> = [
  {path: '', component: Home},
  {path: '/login', component: Login},
  {path: '/register', component: Register},
  {path: '/panel', component: Panel},
  {path: '/panel/monitor', component: Monitor},
  {path: '/panel/analysis', component: Analysis},
  {path: '/panel/calendar', component: Calendar},
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
