<template>
  <div>
    <div class=" media-content">
      <h1 class="">日志</h1>
      <br>
      <el-row :gutter="20" class="is-multiple">
        <el-col :span="24">
          <log-card :logInfo="logInfo"></log-card>
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
    data () {
      return {
        logInfo: {
          _id: 111111,
          startTime: '2019-2-18 15:48',
          logItems: [{
            date: '1945-08-15'
          }]
        },
        pagination: {
          offset: 0,
          limit: 20,
          total: 3
        }
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
