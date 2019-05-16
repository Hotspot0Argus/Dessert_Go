<template>
  <div>
    <el-card class="box-card">
      <el-table
        :data="employeeInfo"
        style="width: 100%">
        <el-table-column
          label="工号"
          width="120">
          <template slot-scope="scope">
            <el-button size="small" @click="selectedUser=scope.row.fields;ui.changeInfo=true">
              {{scope.row.fields.worker_id}}
            </el-button>
          </template>
        </el-table-column>
        <el-table-column
          prop="fields.name"
          label="姓名"
          width="100">
        </el-table-column>
        <el-table-column
          prop="fields.address"
          label="地址"
          min-width="200">
        </el-table-column>
        <el-table-column
          prop="fields.phone"
          label="电话"
          min-width="150">
        </el-table-column>
        <el-table-column
          label="职位"
          width="350">
          <template slot-scope="scope">
            {{scope.row.fields.position>1?'管理员':'普通员工'}}
          </template>
        </el-table-column>
      </el-table>
      <hr>
      <br>
      <br>
    </el-card>
    <br>
    <el-dialog title="修改和查看" :visible.sync="ui.changeInfo">
      <el-form :model="selectedUser">
        <el-form-item label="工号" :label-width="formLabelWidth">
          <el-input v-model="selectedUser.worker_id" disabled autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="姓名" :label-width="formLabelWidth">
          <el-input v-model="selectedUser.name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="住址" :label-width="formLabelWidth">
          <el-input v-model="selectedUser.address" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="电话" :label-width="formLabelWidth">
          <el-input v-model="selectedUser.phone" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="职位" :label-width="formLabelWidth">
          <el-select v-model="selectedUser.position" placeholder="职位">
            <el-option label="普通员工(1)" value="1"></el-option>
            <el-option label="管理员(9)" value="9"></el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button type="danger" @click="remove(selectedUser)">删除该用户</el-button>
        <el-button type="primary" @click="saveInfo(selectedUser)">保 存</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
  export default {
    props: ['employeeInfo'],
    inject: ['reload'],
    data () {
      return {
        selectedUser: '',
        formLabelWidth: '220px',
        ui: {changeInfo: false}
      }
    },
    methods: {
      async saveInfo (user) {
        try {
          await this.$api.post('/persons/set_others_info', user)
          this.$message({
            message: '修改成功',
            type: 'success'
          })
          this.ui.changeInfo = false
        } catch (e) {
          this.$message.error('修改失败,请重试')
        }
      },
      async remove (user) {
        try {
          await this.$api.post('/persons/remove_other', {worker_id: user.worker_id})
          this.$message({
            message: '删除成功',
            type: 'success'
          })
          this.reload()
          this.ui.changeInfo = false
        } catch (e) {
          this.$message.error('删除失败,请重试')
        }
      }
    }
  }
</script>

<style scoped>

</style>
