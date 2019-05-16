<template>
  <div>
    <div class=" media-content">
      <h1 @click="$router.push({name: 'index'})">日志</h1>
      <br>
      <el-row :gutter="20" class="is-multiple">
        <el-col :span="24">
          <log-card :logInfo="logs"></log-card>
        </el-col>
      </el-row>
      <br>
      <br>
      <br>
    </div>
  </div>
</template>
<script>
  import LogCard from './plugin/LogCard'

  export default {
    asyncComputed: {
      async logs () {
        const res = await this.$api.get('/logs/get_logs')
        return JSON.parse(res)
      }
    },
    components: {
      LogCard
    },
    methods: {}
  }
</script>

<style scoped>
</style>
