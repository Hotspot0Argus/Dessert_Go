<template>
  <div>
    <el-header style="padding: 0;z-index: 1000">
      <el-menu
        mode="horizontal">
        <el-row type="flex" justify="end">
          <el-menu-item index="1">处理中心</el-menu-item>
          <el-submenu index="2">
            <template slot="title">我的工作台</template>
            <el-menu-item index="2-1">选项1</el-menu-item>
            <el-menu-item index="2-2">选项2</el-menu-item>
            <el-menu-item index="2-3">选项3</el-menu-item>
            <el-submenu index="2-4">
              <template slot="title">选项4</template>
              <el-menu-item index="2-4-1">选项1</el-menu-item>
              <el-menu-item index="2-4-2">选项2</el-menu-item>
              <el-menu-item index="2-4-3">选项3</el-menu-item>
            </el-submenu>
          </el-submenu>
          <el-menu-item index="3" @click="testSession()">消息中心</el-menu-item>
          <el-menu-item index="4"><a target="_blank">登陆</a></el-menu-item>
        </el-row>
      </el-menu>
    </el-header>

    <div>
      <slot name="main-content"></slot>
    </div>

    <el-footer style="background-color: #E8EBF0;padding: 0;min-height: 10rem">
      <hr style="margin: 0;color: black">
      <el-row type="flex" class="row-bg" justify="center">
        <el-col :span="6">
          <div class="grid-content bg-purple-light">123</div>
        </el-col>
      </el-row>
    </el-footer>
  </div>
</template>

<script>
  export default {
    methods: {
      testSession () {
        this.$session.set('token', '123')
        console.log(this.$session.get('token'))
      }
    }
  }
</script>

<style scoped>
</style>
