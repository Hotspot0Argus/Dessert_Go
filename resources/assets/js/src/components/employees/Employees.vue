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
      <flex-table
        :dataset="tableData"
        height="60vh">
        <flex-table-column type="selection"></flex-table-column>
        <flex-table-column
          prop="name"
          width="100"
          align="center">
          <template slot="header">
            <a class="problem-name single-line">
              <span>
                <i class="fa fa-long-arrow-down fa-fw"></i>姓名</span>
            </a>
          </template>
        </flex-table-column>

        <flex-table-column
          prop="address"
          label="住址"
          align="center"
          width="560">
          <template slot="header">
            <a class="problem-name single-line">
              <span @click="changeOrder('student_id')">
                <i class="fa fa-long-arrow-down fa-fw"></i>住址</span>
            </a>
          </template>
        </flex-table-column>
        <flex-table-column
          prop="address"
          label="住址"
          align="center"
          width="300">
          <template slot="header">
            <a class="problem-name single-line">
              <span @click="changeOrder('student_id')">
                <i class="fa fa-long-arrow-down fa-fw"></i>住址</span>
            </a>
          </template>
        </flex-table-column>
      </flex-table>
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
