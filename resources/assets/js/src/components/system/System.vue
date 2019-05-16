<template>
  <div class="sys">
    <div align="middle">
      <img src="../../assets/dessertgo.jpg" class="image">
    </div>
    <p class="tc" > Dessert_Go V1.0 版本</p>
    <p class="tc"> 北京理工大学假装是软件开发公司出品</p>
    <br>

    <p class="tc"> 谢谢大家 | https://github.com/Hotspot0Argus/Dessert_Go.git</p>
  </div>
</template>

<script>
  export default {
    inject: ['reload'],
    asyncComputed: {
    },
    methods: {
      openDialog () {
        this.$router.push({name: 'orders'})
      }
    }
  }

</script>

<style scoped>
.tc{text-align:center}
.image{
  height: 250px;
  width: 250px
  }
</style>
