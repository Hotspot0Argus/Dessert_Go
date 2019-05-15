<template>
  <div style="background-color: #E8EBF0" class="close-top">
    <div class="media-content">
      <br>
      <br>
      <br>
      <br>
      <br>
      <el-row :gutter="18">
        <el-col :span="16">
          <featured-card category="订单管理" routeName="orders" detail="管理当前所有活动订单"></featured-card>

        </el-col>
        <el-col :span="8">
          <featured-card category="菜单管理" routeName="menus" detail="增加和修改甜品菜单"></featured-card>
        </el-col>
      </el-row>
      <br>
      <br>
      <br>
      <el-row :gutter="18">
        <el-col :span="8">
          <featured-card category="员工管理" routeName="employees" detail="员工管理"></featured-card>
        </el-col>
        <el-col :span="8">
          <featured-card category="日志管理" routeName="logs" detail="账单系统"></featured-card>
        </el-col>
        <el-col :span="8">
          <featured-card category="系统管理" routeName="system" detail="系统版本信息"></featured-card>
        </el-col>
      </el-row>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
    </div>
  </div>
</template>

<script>
  import FeaturedCard from './FeaturedCard'

  export default {
    methods: {
      async login () {
        try {
          const result = await this.$api.post('/post', {'name': '123', 'pwd': '1a1a1a1'})
          console.log(result)
        } catch (e) {
          console.log(e)
        }
      }
    },
    components: {
      FeaturedCard
    }
  }
</script>

<style scoped>
  .function-menu {
    height: 13rem;
    border-width: 1px;
  }

  .box-card {
    border-color: #DCDFE6;
    border-width: 1px;
  }
</style>
