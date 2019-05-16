<template>
  <div class="sys">
    <h1>System</h1>
    <el-button type="primary" @click="openDialog">主要按钮</el-button>
  </div>
</template>

<script>
  export default {
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
</style>
