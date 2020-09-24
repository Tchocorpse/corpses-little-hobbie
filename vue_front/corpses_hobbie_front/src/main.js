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

new Vue({ // eslint-disable-line no-new
  el: '#app-router1',
  router,
  template: '<App/>',
  components: { App }
})

new Vue({ // eslint-disable-line no-new
  el: '#app-get',
  data () {
    return {
      info: 'placeholder',
      loading: true,
      errored: false
    }
  },
  mounted () {
    axios
      .get('http://127.0.0.1:8000/hw_test/', { params: { front: 1 } })
      .then(response => (this.info = response))
      .catch(error => {
        console.log(error)
        this.errored = true
      })
      .finally(() => (this.loading = false)) // Бушь ревьюить детальнее объясни как и зачем эта хуйня работает.
  }
})

new Vue({ // eslint-disable-line no-new
  el: '#app-delete-get',
  data: {
    loading: true,
    errored: false,
    delete_id: null
  },
  methods: {
    deleteMessage: function () {
      axios
        .get('http://127.0.0.1:8000/delete_test/' + encodeURIComponent(this.delete_id), { params: { front: 1 } })
        .then(response => (this.info = response))
        .catch(error => {
          console.log(error)
          this.errored = true
        })
        .finally(() => (this.loading = false))
    }
  }
})

new Vue({ // eslint-disable-line no-new
  el: '#app-input-post',
  data () {
    return {
      input_form: {
        input_title: '',
        input_body: ''
      }
    }
  },
  methods: {
    sendMessage: function () {
      console.log(document.cookie)
      axios
        .post('http://127.0.0.1:8000/hw_test/Test_separate_input', this.input_form, { withCredentials: true, params: { front: 1 } })
        .then(response => {
          // А зачем это?
        })
        .catch(error => {
          console.log(error)
        })
        // .finally(() => { this.input_form.input_title = '', this.input_form.input_body = '' })
    }
  }
})

var csrfCookie = Cookies.get('XSRF-TOKEN')
console.log(csrfCookie)
axios.post('http://127.0.0.1:8000/hw_test/Test_separate_input', {},
  {
    headers: {
      'X-CSRFTOKEN': csrfCookie
    }
  }
)
