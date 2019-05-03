<template>
  <div style="background-color: #E8EBF0" class="close-top">
    <div class="media-content">
      <br>
      <br>
      <br>
      <br>
      <el-row :gutter="18">
        <el-col :span="16">
          <el-card shadow="never" class="box-card function-menu is-hoverable"
                   @click.native="$router.push({name: 'orders'})">
            <div class="title"><i class="fa fa-square fa-fw is-text-danger"></i>订单管理</div>
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card shadow="never" class="box-card function-menu is-hoverable"
                   @click.native="$router.push({name: 'menus'})">
            <div class="title">菜单管理</div>
          </el-card>
        </el-col>
      </el-row>
      <br>
      <el-row :gutter="18">
        <el-col :span="8">
          <el-card shadow="never" class="box-card function-menu is-hoverable"
                   @click.native="$router.push({name: 'employees'})">
            <div class="title item">员工管理</div>
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card shadow="never" class="box-card function-menu is-hoverable"
                   @click.native="$router.push({name: 'logs'})">
            <div class="title">日志管理</div>
          </el-card>
        </el-col>
        <el-col :span="8">
          <featured-card></featured-card>
        </el-col>
      </el-row>
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
    components: { FeaturedCard
    }
  }
</script>

<style scoped>
  .close-top {
    margin-top: -3px;
  }

  .media-content {
    width: 75%;
    padding-left: 12.5%;
  }

  .function-menu {
    height: 13rem;
    border-width: 1px;
  }

  .box-card {
    border-color: #DCDFE6;
    border-width: 1px;
  }
</style>
