<template>
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
</template>

<script>
import axios from 'axios'

export default {
  props: {
    defaultUrl: {
      type: String
    }
  },
  data () {
    return {
      input_form: {
        hello_title: '',
        hello_body: ''
      },
      preview_url: ''
    }
  },
  methods: {
    sendMessage: function () {
      // if (this.image_file != null) {
      var formData = new FormData()
      formData.append('file', this.image_file)
      formData.append('hello_title', this.input_form.hello_title)
      formData.append('hello_body', this.input_form.hello_body)
      axios
        .post(this.defaultUrl + 'sendmes', formData, { headers: { 'Content-Type': 'multipart/form-data' } })
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
          this.$refs.loadref.loadMessages()
        })
    },
    catchFiles (event) {
      this.image_file = event.target.files[0]
      event.target.files = null
      this.preview_url = URL.createObjectURL(this.image_file)
      console.log(this.image_file)
    }
  }
}
</script>

<style scoped>
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
