<template>
  <div id="app">
    <default-layout>
      <div slot="main-content">
        <router-view v-if="isRouterAlive"></router-view>
      </div>
    </default-layout>
  </div>
</template>

<script>
  import DefaultLayout from './components/index/IndexLayout'

  export default {
    provide () {
      return {
        reload: this.reload
      }
    },
    data () {
      return {
        isRouterAlive: true
      }
    },
    methods: {
      reload () {
        this.isRouterAlive = false
        this.$nextTick(function () {
          this.isRouterAlive = true
        })
      }
    },
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
