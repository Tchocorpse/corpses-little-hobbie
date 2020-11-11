<template>

  <div id="app-main">
      <h1>Input new message:</h1>
      <div class="TestDiv2">
          <input maxlength="20" v-model="input_form.hello_title" placeholder="Заголовок">
          <p>{{ input_form.hello_title }}</p>
          <textarea v-model="input_form.hello_body" placeholder="Сообщение"></textarea>
          <br>
          <p style="white-space: pre-line;">{{ input_form.hello_body }}</p>
          <button v-on:click="sendMessage"> Отправить </button>
          <p>File sending:</p>
          <input type="file" @change="catchFiles" name="img_file">
          <img v-if="preview_url" :src="preview_url" style="max-width: 500px; max-height: 500px">

      </div>
        <h2>Messages:</h2>

        <section v-if="errored_load">
            <p>Something gone wrong. Cannot reach or get backend data.</p>
        </section>

        <section v-else>
            <div v-if="loading_load">Loading...</div>

            <div v-else>

                <div v-for="message in loaded_messages.data.MesHe" v-bind:key="message.id">
                    <div class="TestDiv">

                        {{ message.id }} <p>{{ message.hello_title}}</p>
                        {{ message.hello_body}}

                        <p>{{ message.publishing_dt }}</p>
                        <button v-on:click="delete_id=message.id; deleteMessage()">Удалить {{ message.id }} </button>
                    </div>
                    <br>
                </div>

            </div>

        </section>
      <h3>Delete message by id:</h3>
      <input v-model="delete_id" placeholder="Id сообщения на удаление">
      <button v-on:click="deleteMessage" >Удалить {{ delete_id }} </button>
    </div>
</template>

<script>
import axios from 'axios'
const defaultUrl = 'http://127.0.0.1:8000/hw_test/'

export default ({ // eslint-disable-line no-new
  data () {
    return {
      loaded_messages: 'placeholder',
      delete_response: 'Nothing',
      loading_load: true,
      errored_load: false,
      delete_id: null,
      image_file: null,
      preview_url: '',
      input_form: {
        hello_title: '',
        hello_body: ''
      },
      receive_image_id: -1,
      images_url_list: [],
      response_tmp: ''
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
      // if (this.image_file != null) {
      var formData = new FormData()
      formData.append('file', this.image_file)
      formData.append('hello_title', this.input_form.hello_title)
      formData.append('hello_body', this.input_form.hello_body)
      axios
        .post(defaultUrl + 'sendmes', formData, { headers: { 'Content-Type': 'multipart/form-data' } })
        .then(response => {
          this.image_file = null
          this.preview_url = ''
          this.input_form.input_title = ''
          this.input_form.input_body = ''
        })
        .catch(error => {
          console.log(error)
        })
        .finally(() => {
          this.loadMessages()
        })
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
      event.target.files = null
      this.preview_url = URL.createObjectURL(this.image_file)
      console.log(this.image_file)
    },
    receiveImage: function (receiveImageId) {
      axios
        .get(defaultUrl + 'image/' + encodeURIComponent(receiveImageId))
        .then(response => (this.response_tmp = response))
        .catch(error => {
          console.log(error)
        })
        .finally(() => {
          this.receive_image_id = -1
        })
      const newImage = {
        image_url: this.response_tmp,
        id: receiveImageId
      }
      this.images_url_list.push(newImage)
      return this.response_tmp
    }
  },
  computed: {
    receiveImageComputed: {

    }
  }
})

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

.TestDiv {
            border: 4px outset black;
            text-align: center;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
            color: #886A08;
        }
.TestDiv2 {
            border: 2px groove #867052;
            text-align: center;
            width: 600px;
            padding: 50px;
            margin: auto;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }

</style>
