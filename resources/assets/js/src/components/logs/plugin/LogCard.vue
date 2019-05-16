<template>
  <div>
    <el-card class="box-card">
      <el-table
        :data="logInfo.logItems"
        style="width: 100%">
        <el-table-column
          prop="date"
          label="日期"
          width="150">
        </el-table-column>
      </el-table>
      <hr>
      <span class="is-text-gain is-text-small">{{logInfo.startTime}}</span>
      <br>
      <br>
    </el-card>
    <br>
  </div>
</template>

<script>
  export default {
    props: ['logInfo'],
    methods: {
    }
  }
</script>

<style scoped>

</style>
