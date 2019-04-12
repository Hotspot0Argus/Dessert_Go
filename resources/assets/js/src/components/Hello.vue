<template>
  <div class="hello" v-if="data2">
    <Header></Header>
    <body>
      <h1>{{msg}}</h1>
    </body>
    <Footer></Footer>
  </div>
</template>

<script>
  import Header from './Header'
  import Footer from './Footer'

  export default {
    name: 'hello',
    data () {
      return {
        msg: '欢迎使用Dessert GO!',
        testData: ''
      }
    },
    // 异步加载数据
    asyncComputed: {
      data2 () {
        return this.$api.get('/menu/test')
      }
    },
    components: {
      Header,
      Footer
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>h1{
  font-family:"楷体"
}

</style>
