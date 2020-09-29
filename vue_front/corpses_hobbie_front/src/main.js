import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import Router from 'vue-router'
import Home from '@/components/Home'
import tsthw from '@/components/testhw'
import Cookies from 'js-cookie'

axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.withCredentials = true
export default axios

const defaultUrl = 'http://127.0.0.1:8000/hw_test/'

new Vue({ // eslint-disable-line no-new
  el: '#app-router1',
  router,
  template: '<App/>',
  components: { App }
})

new Vue({ // eslint-disable-line no-new
  el: '#app-main',
  data () {
    return {
      info: 'placeholder',
      loading_load: true,
      errored_load: false,
      loading_del: true,
      errored_del: false,
      delete_id: null,
      input_form: {
        hello_title: '',
        hello_body: ''
      }
    }
  },
  mounted () {
    this.loadMessages()
  },
  methods: {
    deleteMessage: function () {
      axios
        .get(defaultUrl + 'delete_test/' + encodeURIComponent(this.delete_id), { params: { front: 1 } })
        .then(response => (this.info = response))
        .catch(error => {
          console.log(error)
          this.errored_del = true
        })
        .finally(() => {
          (this.loading_del = false)
          this.loadMessages()
        })
    },
    sendMessage: function () {
      axios
        .post(defaultUrl + 'Test_separate_input', this.input_form, { params: { front: 1 } })
        .then(response => {
          // А зачем это?
          this.input_form.input_title = ''
          this.input_form.input_body = ''
        })
        .catch(error => {
          console.log(error)
        })
        .finally(() => { this.loadMessages() })
    },
    loadMessages: function () {
      axios
        .get(defaultUrl, { params: { front: 1 } })
        .then(response => (this.info = response))
        .catch(error => {
          console.log(error)
          this.errored_load = true
        })
        .finally(() => (this.loading_load = false)) // Бушь ревьюить детальнее объясни как и зачем эта хуйня работает.
    }
  }
})
