import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import Router from 'vue-router'
import detail from '@/components/DeleteMessage'

axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.withCredentials = true
// export default axios

new Vue({ // eslint-disable-line no-new
  el: '#app-main',
  template: '<App/>',
  components: { App }
})
