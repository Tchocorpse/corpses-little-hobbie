<template>
  <div class="TestDiv">

    {{ message.id }} <p>{{ message.hello_title}}</p>
    <img v-if="image_url" :src="image_url" style="max-width: 500px; max-height: 500px">
    <br>
    {{ message.hello_body }}
    <p>{{ message.publishing_dt }}</p>
    <DeleteMessage :defaultUrl="defaultUrl" :message_id="message.id"/>
    {{  }}
    {{ image_url }}
  </div>
</template>

<script>
import axios from 'axios'
import DeleteMessage from '@/components/DeleteMessage'

export default {
  components: { DeleteMessage },
  props: {
    message: {
      type: Object
    },
    defaultUrl: {
      type: String
    }
  },
  data () {
    return {
      image_url: '',
      image_file: null
    }
  },
  methods: {
    receiveImage: function (receiveImageId) {
      axios
        .get(this.defaultUrl + 'image/' + encodeURIComponent(receiveImageId))
        .then(response => (this.image_url = response))
        .catch(error => {
          console.log(error)
        })
        .finally(() => {
          this.receive_image_id = -1
        })
    }
  },
  mounted () {
    this.receiveImage(this.message.id)
  }
}
</script>

<style scoped>
.TestDiv {
  border: 4px outset black;
  text-align: center;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #886A08;
}
</style>
