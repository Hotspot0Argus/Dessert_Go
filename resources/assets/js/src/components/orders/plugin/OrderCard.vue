<template>
  <div>
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>桌号{{orderInfo.tableId}}</span>
        <el-button style="float: right; padding: 3px 0" type="text">查看和编辑</el-button>
      </div>
      <el-table
        :data="orderInfo.menuItems"
        style="width: 100%">
        <el-table-column
          prop="name"
          label="名称"
          width="100">
        </el-table-column>
        <el-table-column
          prop="number"
          label="数量">
        </el-table-column>
        <el-table-column
          label="单价"
          width="100">
          <template slot-scope="scope">
            {{scope.row.price|isPrice}}
          </template>
        </el-table-column>
      </el-table>
      <hr>
      <span class="is-text-gain is-text-small">{{orderInfo.startTime}}</span>
      <span class="pull-right">总计:123</span>
      <br>
      <br>
    </el-card>
    <br>
  </div>
</template>

<script>
  export default {
    props: ['orderInfo']
  }
</script>

<style scoped>

</style>
