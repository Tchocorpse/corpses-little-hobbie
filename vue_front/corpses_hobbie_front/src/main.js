import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import Router from 'vue-router'
import Home from '@/components/Home'
import tsthw from '@/components/testhw'

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
      loaded_messages: 'placeholder',
      delete_response: 'Nothing',
      loading_load: true,
      errored_load: false,
      delete_id: null,
      image_file: '',
      preview_url: '',
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
        .get(defaultUrl + 'deletemes/' + encodeURIComponent(this.delete_id))
        .then(response => (this.delete_response = response))
        .catch(error => {
          console.log(error)
        })
        .finally(() => {
          this.loadMessages()
        })
    },
    sendMessage: function () {
      axios
        .post(defaultUrl + 'sendmes', this.input_form)
        .then(response => {
          this.input_form.input_title = ''
          this.input_form.input_body = ''
        })
        .catch(error => {
          console.log(error)
        })
        // .finally(() => { this.loadMessages() })
      axios
        .post(defaultUrl + 'image_input', this.image_file, { headers: { 'Content-Type': 'multipart/form-data' } })
        .then(response => {
          this.image_file = ''
        })
        .catch(error => {
          console.log(error)
        })
        .finally(() => { this.loadMessages() })
    },
    loadMessages: function () {
      axios
        .get(defaultUrl + 'receivemes')
        .then(response => (this.loaded_messages = response))
        .catch(error => {
          console.log(error)
          this.errored_load = true
        })
        .finally(() => (this.loading_load = false))
    },
    catchFiles (event) {
      this.image_file = event.target.files[0]
      this.preview_url = URL.createObjectURL(this.image_file)
      console.log(this.image_file)
    }
  }
})
