<template>
  <section v-if="errored_load">
            <p>Something gone wrong. Cannot reach or get backend data.</p>
        </section>

        <section v-else>
            <div v-if="loading_load">Loading...</div>

            <div v-else>

                <div v-for="message in loaded_messages.data.MesHe" v-bind:key="message.id">
                    <DisplayMessage :defaultUrl="defaultUrl" :message="message"/>
                    <br>
                </div>

            </div>

        </section>
</template>

<script>
import axios from 'axios'
import DisplayMessage from '@/components/DisplayMessage'

export default {
  name: 'ReceiveMessage',
  components: {
    DisplayMessage
  },
  props: {
    defaultUrl: {
      type: String
    }
  },
  data () {
    return {
      loaded_messages: 'placeholder',
      delete_response: 'Nothing',
      loading_load: true,
      errored_load: false

    }
  },
  mounted () {
    this.loadMessages()
  },
  methods: {
    loadMessages: function () {
      axios
        .get(this.defaultUrl + 'receivemes')
        .then(response => (this.loaded_messages = response))
        .catch(error => {
          console.log(error)
          this.errored_load = true
        })
        .finally(() => (this.loading_load = false))
    }
  }
}
</script>

<style scoped>

</style>
