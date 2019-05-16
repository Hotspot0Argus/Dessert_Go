<template>
  <div>
    <div class=" media-content">
      <h1>员工管理系统</h1>
      <div class="is-multiple">
        <el-button size="small" type="primary">增加员工</el-button>
      </div>
      <br>
      <el-row :gutter="20" class="is-multiple">
        <el-col :span="24">
          <employee-card :employeeInfo="employeeInfo"></employee-card>
        </el-col>
      </el-row>
      <br>
      <br>
      <br>
    </div>
  </div>
</template>

<script>
  import EmployeeCard from './plugin/EmployeeCard'

  export default {
    data () {
      return {
        employeeInfo: {
          _id: 111111,
          startTime: '2019-2-18 15:48',
          employeeItems: [{
            _id: 111,
            date: '2016-05-02',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1518 弄'
          }, {
            _id: 112,
            date: '2016-05-04',
            name: '王小猫',
            address: '上海市普陀区金沙江路 1517 弄'
          }, {
            _id: 614,
            date: '2016-05-01',
            name: '王小狗',
            address: '上海市普陀区金沙江路 1519 弄'
          }, {
            _id: 707,
            date: '2016-05-03',
            name: '王小狼',
            address: '上海市普陀区金沙江路 1516 弄'
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
      EmployeeCard
    }
  }
</script>

<style scoped>
</style>
