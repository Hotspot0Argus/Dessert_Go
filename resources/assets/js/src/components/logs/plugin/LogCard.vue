<template>
  <div>
    <el-card class="box-card">
      <el-table
        :data="logInfo"
        style="width: 100%" max-height="600">
        <el-table-column
          label="桌号"
          width="150">
          <template slot-scope="scope">
            {{scope.row.fields.order_id?scope.row.fields.order_id:'无'}}
          </template>
        </el-table-column>
        <el-table-column
          label="操作员"
          width="150">
          <template slot-scope="scope">
            {{scope.row.fields.person_name}}
          </template>
        </el-table-column>
        <el-table-column
          label="开始时间"
          min-width="220">
          <template slot-scope="scope">
            {{scope.row.fields.start_time}}
          </template>
        </el-table-column>
        <el-table-column
          label="结束时间"
          min-width="220">
          <template slot-scope="scope">
            {{scope.row.fields.end_time||(scope.row.fields.order_id?'未用餐完毕':'还未下班')}}
          </template>
        </el-table-column>
      </el-table>
      <hr>
      <br>
      <br>
    </el-card>
    <br>
  </div>
</template>

<script>
  export default {
    props: ['logInfo'],
    methods: {}
  }
</script>

<style scoped>

</style>
