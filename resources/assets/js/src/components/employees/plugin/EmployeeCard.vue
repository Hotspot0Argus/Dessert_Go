<template>
  <div>
    <el-card class="box-card">
      <el-table
        :data="employeeInfo.employeeItems"
        style="width: 100%">
        <el-table-column
          prop="_id"
          label="工号"
          width="75">
        </el-table-column>
        <el-table-column
          prop="name"
          label="姓名"
          width="100">
        </el-table-column>
        <el-table-column
          prop="date"
          label="入职日期"
          width="150">
        </el-table-column>
        <el-table-column
          prop="address"
          label="住址"
          width="350">
        </el-table-column>
        <el-table-column
          label=" "
          width="200">
          <template slot-scope="scope">
            <el-button size="small" type="primary" round>修改信息</el-button>
            <el-button size="small" type="danger" round>删除员工</el-button>
          </template>
        </el-table-column>
      </el-table>
      <hr>
      <span class="is-text-gain is-text-small">{{employeeInfo.startTime}}</span>
      <br>
      <br>
    </el-card>
    <br>
  </div>
</template>

<script>
  export default {
    props: ['employeeInfo'],
    methods: {
    }
  }
</script>

<style scoped>

</style>
