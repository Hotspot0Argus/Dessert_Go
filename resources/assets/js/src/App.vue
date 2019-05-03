<template>
  <div id="app">
    <default-layout>
      <div slot="main-content">
        <router-view></router-view>
      </div>
    </default-layout>
  </div>
</template>

<script>
  import DefaultLayout from './components/index/IndexLayout'

  export default {
    components: {
      DefaultLayout
    }
  }
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
    margin: 0;
  }
</style>
