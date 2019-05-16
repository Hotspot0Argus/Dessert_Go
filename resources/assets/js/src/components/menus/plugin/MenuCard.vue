<template>
  <div>
    <el-card class="box-card">
      <el-table
        :data="menuInfo.menuItems"
        style="width: 100%">
        <el-table-column
          prop="name"
          label="名称"
          width="150">
        </el-table-column>
        <el-table-column
          label="单价"
          width="150">
          <template slot-scope="scope">
            {{scope.row.price|isPrice}}
          </template>
        </el-table-column>
        <el-table-column
          label=" "
          width="200">
          <template slot-scope="scope">
            <el-button size="small" type="primary" round>修改菜品</el-button>
            <el-button size="small" type="danger" round>删除菜品</el-button>
          </template>
        </el-table-column>
      </el-table>
      <hr>
      <span class="is-text-gain is-text-small">{{menuInfo.startTime}}</span>
      <br>
      <br>
    </el-card>
    <br>
  </div>
</template>

<script>
  export default {
    props: ['menuInfo']
  }
</script>

<style scoped>

</style>
