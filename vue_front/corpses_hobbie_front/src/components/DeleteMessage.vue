<template>
  <button v-on:click="delete_id=message_id; deleteMessage()">Удалить {{ message_id }} </button>
</template>

<script>
import axios from 'axios'

export default {
  delete_id: null,
  props: {
    message_id: {
      type: Number
    },
    defaultUrl: {
      type: String
    }
  },
  methods: {
    deleteMessage: function () {
      axios
        .get(this.defaultUrl + 'deletemes/' + encodeURIComponent(this.delete_id))
        .then(response => (this.delete_response = response))
        .catch(error => {
          console.log(error)
        })
        .finally(() => {
          console.log(this.$refs)
        })
    }
  }
}
</script>

<style scoped>

</style>
