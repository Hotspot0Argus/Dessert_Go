<template>
  <div>
    <el-card class="box-card">
      <el-table
        :data="menuInfo"
        style="width: 100%">
        <el-table-column
          label="名称"
          min-width="150">
          <template slot-scope="scope">
            <el-button size="small"
                       @click="selectedItem = scope.row.fields;selectedItem.item_id = scope.row.pk;ui.edit = true">
              {{scope.row.fields.name}}
            </el-button>
          </template>
        </el-table-column>
        <el-table-column
          label="单价"
          min-width="150">
          <template slot-scope="scope">
            {{parseInt(scope.row.fields.price)|isPrice}}
          </template>
        </el-table-column>
        <el-table-column
          label="折扣"
          min-width="150">
          <template slot-scope="scope">
            {{scope.row.fields.offset}}
          </template>
        </el-table-column>
        <el-table-column
          label="状态"
          min-width="150">
          <template slot-scope="scope">
            {{scope.row.fields.status.toString() ==='true'?'在售':'暂不出售'}}
          </template>
        </el-table-column>
      </el-table>
      <br>
      <br>
    </el-card>
    <br>
    <el-dialog
      title="添加甜品"
      :visible.sync="ui.edit"
      width="30%">
      <el-form ref="form" v-model="selectedItem" label-width="80px">
        <el-form-item label="名称">
          <el-input v-model="selectedItem.name"></el-input>
        </el-form-item>
        <el-form-item label="单价(分)">
          <el-input v-model="selectedItem.price"></el-input>
        </el-form-item>
        <el-form-item label="折扣">
          <el-input place-holder="10为不打折,9为9折" v-model="selectedItem.offset"></el-input>
        </el-form-item>
        <el-form-item label="在售">
          <el-switch
            v-model="selectedItem.status">
          </el-switch>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button type="danger" @click="removeItem">删除甜品</el-button>
        <el-button type="primary" @click="addItem">保存改动</el-button>
     </span>
    </el-dialog>
  </div>
</template>

<script>
  export default {
    props: ['menuInfo'],
    inject: ['reload'],
    data () {
      return {
        selectedItem: {},
        ui: {
          edit: false
        }
      }
    },
    methods: {
      async addItem () {
        try {
          await this.$api.post('/menus/modify_menu', this.selectedItem)
          this.$message({
            message: '修改成功',
            type: 'success'
          })
          this.reload()

          this.ui.edit = false
        } catch (e) {
          this.$message.error('修改失败,请重试')
        }
      },
      async removeItem () {
        try {
          await this.$api.post('/menus/remove_menu', {item_id: this.selectedItem.item_id})
          this.$message({
            message: '删除成功',
            type: 'success'
          })
          this.reload()
          this.ui.edit = false
        } catch (e) {
          this.$message.error('删除失败,请重试')
        }
      }
    }
  }
</script>

<style scoped>

</style>
