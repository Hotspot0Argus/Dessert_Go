<template>
  <div class="sys media-content">
    <h1>系统管理</h1>
    <br>
    <div align="middle">
      <img src="../../assets/dessertgo.jpg" class="image">
    </div>
    <br>
    <p class="tc"> Dessert_Go V1.0 版本</p>
    <p class="tc"> 北京理工大学假装是软件开发公司出品</p>
    <br>
  </div>
</template>

<script>
  export default {
    inject: ['reload'],
    asyncComputed: {},
    methods: {
      openDialog () {
        this.$router.push({name: 'orders'})
      }
    }
  }

</script>

<style scoped>
  .tc {
    text-align: center
  }

  .image {
    height: 250px;
    width: 250px
  }
</style>
