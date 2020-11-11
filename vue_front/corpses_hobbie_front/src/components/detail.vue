<template>
  <div class="TestDiv">
    <!-- <div id="app-router1"></div>  -->
    {{ message.id }} <p>{{ message.hello_title}}</p>
    {{ message.hello_body}}
    {{ receiveImage }}
    <p>test detail</p>

    <p>{{ message.publishing_dt }}</p>
    <button v-on:click="delete_id=message.id; deleteMessage()">Удалить {{ message.id }} </button>
  </div>
</template>

<script>
export default {
  name: 'detail'
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
