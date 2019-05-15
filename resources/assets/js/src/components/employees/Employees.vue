<template>
  <div class="media-content">
    <h1>员工管理系统</h1>
    <div class="is-multiple">
      <el-button size="small" type="primary">123</el-button>
      <el-button size="small" type="primary">123</el-button>
      <el-button size="small" type="primary">123</el-button>
      <el-button size="small" type="primary">123</el-button>
      <el-button size="small" type="primary">123</el-button>
    </div>
    <br>
    <div>
    </div>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        tableData: [{
          date: '2016-05-02',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄',
          _id: 111
        }, {
          date: '2016-05-04',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1517 弄'
        }, {
          date: '2016-05-01',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1519 弄'
        }, {
          date: '2016-05-03',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1516 弄'
        }],
        pagination: {
          offset: 0,
          limit: 20,
          total: 3
        }
      }
    }
  }
</script>

<style scoped>
</style>
