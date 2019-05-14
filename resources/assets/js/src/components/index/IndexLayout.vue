<template>
  <div>
    <el-header style="padding: 0;z-index: 1000">
      <el-menu
        mode="horizontal">
        <el-row type="flex" justify="end">
          <el-menu-item index="1" @click.native="$router.push({name: ' '}); $router.go(0)">首页</el-menu-item>
          <el-submenu index="2">
            <template slot="title">快速导航</template>
            <el-menu-item index="2-1" @click.native="$router.push({name: 'orders'})">订单管理</el-menu-item>
            <el-menu-item index="2-2" @click.native="$router.push({name: 'menus'})">菜单管理</el-menu-item>
            <el-menu-item index="2-3" @click.native="$router.push({name: 'employees'})">员工管理</el-menu-item>
            <el-menu-item index="2-4" @click.native="$router.push({name: 'logs'})">日志管理</el-menu-item>
            <el-menu-item index="2-5" @click.native="$router.push({name: 'system'})">系统管理</el-menu-item>
          </el-submenu>
          <el-menu-item index="3">消息中心</el-menu-item>
          <el-menu-item index="4"><a href="https://ele.me" target="_blank">登陆</a></el-menu-item>
        </el-row>
      </el-menu>
    </el-header>

    <div>
      <slot name="main-content"></slot>
    </div>

    <el-footer style="background-color: #E8EBF0;padding: 0;min-height: 1rem">
      <hr style="margin: 0;color: black">
      <el-row type="flex" class="row-bg" justify="center">
        <el-col :span="36">
          <div class="grid-content bg-purple-light">
          互联网食品信息服务资格证书:(北理工)-经营性-2019-0510 | 北理工工商行政管理 Copyright ©2019-2029 北京理工假装是工程师有限公司, All Rights Reserved.
          </div>
        </el-col>
      </el-row>
    </el-footer>
  </div>
</template>

<script>
  export default {}
</script>

<style scoped>
</style>
