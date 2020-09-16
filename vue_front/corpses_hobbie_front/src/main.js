import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import Router from 'vue-router'
import Home from '@/components/Home'
import tsthw from '@/components/testhw'
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'
axios.defaults.xsrfCookieName = 'csrftoken'
// import HelloWorld from "@/components/HelloWorld"

/*
const NotFound = { template: '<p>Страница не найдена</p>' }
const Home = { template: '<p>главная</p>' }
const TestHW = { template: '<p>test</p> <base-separate></base-separate>' }
const HelloWorldT = { template: '<p>Hello World?</p>' }

const routes = {
  '/': Home,
  '/HelloWorld': HelloWorldT,
  '/testhw': TestHW
}
*/

new Vue({ // eslint-disable-line no-new
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})

Vue.component('base-separate', {
  data: function () {
    return {
      count: 0
    }
  },
  template: '<button v-on:click="count++">Счётчик кликов — {{ count }}</button>'
})

new Vue({ // eslint-disable-line no-new
  el: '#app-get',
  data () {
    return {
      info: 'placeholder'
    }
  },
  mounted () {
    axios
      .get('http://127.0.0.1:8000/hw_test/', { params: { front: 1 } })
      .then(response => (this.info = response))
  }
})
