<template>
  <div class="media-content" v-if="userInfo">
    <h1 @click="$router.push({name: 'index'})">个人信息预览</h1>
    <br>
    <br>
    <el-tabs v-model="page">
      <el-tab-pane label="信息设置" name="change_info"></el-tab-pane>
      <el-tab-pane label="修改密码" name="pwd"></el-tab-pane>
    </el-tabs>
    <el-card v-if="page==='change_info'">
      <div slot="header" class="clearfix">
        <span>信息设置</span>
      </div>
      <el-form label-position="right" label-width="80px" :model="userInfo">
        <el-form-item label="工号">
          <el-input v-model="userInfo.worker_id" disabled=""></el-input>
        </el-form-item>
        <el-form-item label="姓名">
          <el-input v-model="userInfo.name"></el-input>
        </el-form-item>
        <el-form-item label="电话号">
          <el-input v-model="userInfo.phone"></el-input>
        </el-form-item>
        <el-form-item label="家庭住址">
          <el-input v-model="userInfo.address"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="save()">保存</el-button>
        </el-form-item>
      </el-form>
    </el-card>
    <el-card v-if="page==='pwd'">
      <div slot="header" class="clearfix">
        <span>修改密码</span>
      </div>
      <el-form status-icon label-width="100px" class="demo-ruleForm">
        <el-form-item label="原密码" prop="pass">
          <el-input type="password" v-model="oldPwd" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="新密码" prop="pass">
          <el-input type="password" v-model="newPwd" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="确认密码" prop="checkPass">
          <el-input type="password" v-model="confirmPwd" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="savePwd()">保存</el-button>
        </el-form-item>
      </el-form>
    </el-card>
    <br>
    <br>
    <br>
  </div>
</template>
<script>
  export default {
    inject: ['reload'],
    data () {
      return {
        page: 'change_info',
        oldPwd: '',
        newPwd: '',
        confirmPwd: ''
      }
    },
    methods: {
      async savePwd () {
        if (!this.oldPwd) {
          this.$message(({
            message: '原密码不能为空',
            type: 'warning'
          }))
          return
        }
        if (!this.newPwd || !this.confirmPwd) {
          this.$message(({
            message: '新密码或确认密码不能为空',
            type: 'warning'
          }))
          return
        }
        if (this.newPwd !== this.confirmPwd) {
          this.$message(({
            message: '请确认密码和确认密码是否相同',
            type: 'warning'
          }))
          return
        }
        try {
          await this.$api.post('/persons/change_password', {old_password: this.oldPwd, new_pasword: this.newPwd})
          this.$message({
            message: '修改成功',
            type: 'success'
          })
          this.reload()
        } catch (e) {
          this.$message.error('修改失败,请重试')
        }
      },
      async save () {
        try {
          await this.$api.post('/persons/set_self_info', this.userInfo)
          this.$message({
            message: '修改成功',
            type: 'success'
          })
          this.reload()
        } catch (e) {
          this.$message.error('修改失败,请重试')
        }
      }
    },
    asyncComputed: {
      async userInfo () {
        return await this.$api.get('/persons/get_self_info')
      }
    }
  }
</script>

<style scoped>

</style>
