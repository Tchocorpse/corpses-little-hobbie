<template>

  <div id="app-main">
    <h1>Input new message:</h1>
    <inputPart :defaultUrl="defaultUrl"/>
    <h2>Messages:</h2>

        <ReceiveMessage ref="loadRef" :defaultUrl="defaultUrl"/>
      <h3>Delete message by id:</h3>
      <input v-model="delete_id" placeholder="Id сообщения на удаление">
      <DeleteMessage :defaultUrl="defaultUrl" :message_id="delete_id"/>
    </div>
</template>

<script>
import inputPart from '@/components/inputPart'
import DeleteMessage from '@/components/DeleteMessage'
import ReceiveMessage from '@/components/ReceiveMessage'

export default ({ // eslint-disable-line no-new
  components: {
    inputPart, DeleteMessage, ReceiveMessage
  },
  data () {
    return {
      delete_id: null,
      defaultUrl: 'http://127.0.0.1:8000/hw_test/'
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

</style>
