<template>
  <div>
    <el-header style="padding: 0;z-index: 1000">
      <el-menu mode="horizontal">
        <el-menu-item index="1" @click.native="$router.push({name: 'index'}); $router.go(0)">首页</el-menu-item>
        <el-row type="flex" justify="end">
          <el-submenu index="2">
            <template slot="title">快速导航</template>
            <el-menu-item index="2-1" @click="$router.push({name: 'orders'})">订单管理</el-menu-item>
            <el-menu-item index="2-2" @click="$router.push({name: 'menus'})">菜单管理</el-menu-item>
            <el-menu-item index="2-3" @click="$router.push({name: 'employees'})">员工管理</el-menu-item>
            <el-menu-item index="2-4" @click="$router.push({name: 'logs'})">日志管理</el-menu-item>
            <el-menu-item index="2-5" @click="$router.push({name: 'system'})">系统管理</el-menu-item>
          </el-submenu>
          <el-menu-item v-if="rcToken === ''" index="3" type="primary" @click="ui.loginModal=true">
            登录
          </el-menu-item>
          <el-menu-item v-else type="primary" index="4" @click="logout">
            退出
          </el-menu-item>
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
        rcToken: ''
      }
    },
    asyncComputed: {
      isLogin () {
        const token = this.$session.get('token')
        console.log('1')
        if (token) {
          console.log('2')
          // try {
          //   this.$api.get('/session/verify', {'token': token})
          //   return true
          // } catch (e) {
          //   return false
          // }
          this.rcToken = '123'
        }
      }
    },
    methods: {
      async login () {
        // const token = await this.$api.post('/session/login', {
        //   worker_id: this.loginInfo.workerId,
        //   password: this.loginInfo.password
        // })
        this.$session.set('token', 'token')
        this.rcToken = '123'
        this.ui.loginModal = false
      },
      logout () {
        this.$session.clear()
        this.rcToken = ''
      }
    }
  }
</script>

<style scoped>
</style>
