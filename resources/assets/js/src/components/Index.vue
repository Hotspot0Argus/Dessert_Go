<template>
  <div>


    <br>
    <br>
    <br>
    <form name='form' action="">
      <input id="username" type="text" placeholder="请输入手机号码或用户名"/>
      <input id='pwd' type="password" placeholder="请输入密码"/>
      <button>登录</button>
    </form>
    <div class="account">
      <p class="forget" style="float:right">忘记密码?</p>
      <div class="register">
        <span>还没有账号?</span>
        <a href="#">手机注册</a>
      </div>
    </div>
    <el-button>默认按钮</el-button>
    <el-button type="primary" @click.native="login">主要按钮</el-button>
    <el-button type="text">文字按钮</el-button>
  </div>
</template>

<script>

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
    }
  }
</script>

<style scoped>

</style>
