import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/components/Home.vue'
import tsthw from '@/components/DisplayMessage'
import input from '@/components/inputPart'
import detail from '@/components/DeleteMessage'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/input',
    name: 'SeparateInput',
    component: input
  },
  {
    path: '/detail',
    name: 'Detail',
    component: detail
  },
  {
    path: '/testhw',
    name: 'test_hw',
    component: tsthw
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
