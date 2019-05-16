<template>
  <div>
    <div class=" media-content">
      <h1 @click="$router.push({name: 'index'})">员工管理系统</h1>
      <div class="is-multiple">
        <el-button size="small" type="primary" @click="ui.addInfo=true">增加员工</el-button>
      </div>
      <br>
      <el-row :gutter="20" class="is-multiple">
        <el-col :span="24" v-if="workersInfo">
          <employee-card :employeeInfo="workersInfo"></employee-card>
        </el-col>
      </el-row>
      <br>
      <br>
      <br>
    </div>
    <el-dialog title="新增员工" :visible.sync="ui.addInfo">
      <el-form :model="user">
        <el-form-item label="工号" :label-width="formLabelWidth">
          <el-input v-model="user.worker_id" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="姓名" :label-width="formLabelWidth">
          <el-input v-model="user.name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="住址" :label-width="formLabelWidth">
          <el-input v-model="user.address" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="电话" :label-width="formLabelWidth">
          <el-input v-model="user.phone" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="职位" :label-width="formLabelWidth">
          <el-select v-model="user.position" placeholder="职位">
            <el-option label="普通员工(1)" value="1"></el-option>
            <el-option label="管理员(9)" value="9"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="默认密码" :label-width="formLabelWidth">
          <span>123123123</span>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="addPerson()">新增</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
  import EmployeeCard from './plugin/EmployeeCard'

  export default {
    inject: ['reload'],
    data () {
      return {
        user: {
          worker_id: '',
          name: '',
          address: '',
          phone: '',
          position: 1
        },
        formLabelWidth: '220px',
        ui: {addInfo: false}
      }
    },
    asyncComputed: {
      async workersInfo () {
        const res = await this.$api.get('/persons/get_all_info')
        return JSON.parse(res)
      }
    },
    methods: {
      async addPerson () {
        try {
          await this.$api.post('/persons/create', this.user)
          this.$message({
            message: '创建成功',
            type: 'success'
          })
          this.ui.addInfo = false
          this.reload()
        } catch (e) {
          this.$message.error('创建失败')
        }
      }
    },
    components: {
      EmployeeCard
    }
  }
</script>

<style scoped>
</style>
