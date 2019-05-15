<template>
  <div>
    <el-header style="padding: 0;z-index: 1000">
      <el-menu mode="horizontal">
        <el-menu-item index="1" @click.native="$router.push({name: 'index'})">首页</el-menu-item>
        <el-menu-item style="float:right" v-if="workerId === ''" index="3" type="primary" @click="ui.loginModal=true">
          登录
        </el-menu-item>
        <el-submenu index="4" v-else style="float:right">
          <template slot="title">工号：{{workerId}}</template>
          <el-menu-item index="4-1" @click="logout">退出账号</el-menu-item>
          <el-menu-item index="4-2" @click="$router.push({name: 'user:change_info'})">账号设置</el-menu-item>
        </el-submenu>
        <el-submenu index="2" style="float:right">
          <template slot="title">快速导航</template>
          <el-menu-item index="2-1" @click="$router.push({name: 'orders'})">订单管理</el-menu-item>
          <el-menu-item index="2-2" @click="$router.push({name: 'menus'})">菜单管理</el-menu-item>
          <el-menu-item index="2-3" @click="$router.push({name: 'employees'})">员工管理</el-menu-item>
          <el-menu-item index="2-4" @click="$router.push({name: 'logs'})">日志管理</el-menu-item>
          <el-menu-item index="2-5" @click="$router.push({name: 'system'})">系统管理</el-menu-item>
        </el-submenu>
      </el-menu>
    </el-header>

    <div>
      <slot name="main-content"></slot>
    </div>

    <el-footer class="is-footer" style="min-height: calc(100vh - 720px)">
      <hr style="margin: 0;color: black">
      <el-row type="flex" class="row-bg" justify="center">
        <el-col :span="36">
          <div class="has-text-center">
            <p> 互联网食品信息服务资格证书:(北理工)-经营性-2019-0510</p>
            <p> 北理工工商行政管理 Copyright ©2019-2029 北京理工-假装是工程师有限公司, All Rights Reserved.</p>
            <br>
            <p> 版权所有: 公开 github | https://github.com/Hotspot0Argus/Dessert_Go.git</p>
          </div>
        </el-col>
      </el-row>
    </el-footer>
    <el-dialog
      title="登录"
      :visible.sync="ui.loginModal"
      width="30%">
      <el-form ref="form" :model="loginInfo" label-width="80px">
        <el-form-item label="工号">
          <el-input v-model="loginInfo.workerId"></el-input>
        </el-form-item>
        <el-form-item label="密码">
          <el-input type="password" v-model="loginInfo.password" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="ui.loginModal = false">取 消</el-button>
        <el-button type="primary" @click="login">登 录</el-button>
     </span>
    </el-dialog>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        ui: {
          loginModal: false
        },
        loginInfo: {
          workerId: '',
          password: ''
        },
        workerId: ''
      }
    },
    asyncComputed: {
      isLogin () {
        const token = this.$session.get('token')
        this.$api.setToken(token)
        if (token) {
          try {
            this.$api.get('/session/verify', {'token': token})
            this.workerId = this.$session.get('user').worker_id
          } catch (e) {
            this.$api.setToken('')
            this.$session.clear()
          }
        }
      }
    },
    methods: {
      async login () {
        const res = await this.$api.post('/session/login', {
          worker_id: this.loginInfo.workerId,
          password: this.loginInfo.password
        })
        this.$session.set('token', res.token)
        this.$session.set('user', res.info)
        this.$api.setToken(res.token)
        this.workerId = res.info.worker_id
        this.ui.loginModal = false
      },
      async logout () {
        try {
          // await this.$api.get('/session/logout')
          this.$session.clear()
          this.$api.setToken('')
          this.workerId = ''
        } catch (e) {
        }
      }
    }
  }
</script>

<style scoped>
  .is-footer {
    background-color: #E8EBF0;
    padding: 0;
    height: calc(100vh - 200px);
  }
</style>
