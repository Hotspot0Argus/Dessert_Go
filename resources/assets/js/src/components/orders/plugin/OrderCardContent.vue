<template>
  <el-table
    :data="orderInfo.menuItems"
    style="width: 100%" max-height="450">
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
</template>

<script>
  export default {
    props: ['orderInfo']
  }
</script>

<style scoped>

</style>
