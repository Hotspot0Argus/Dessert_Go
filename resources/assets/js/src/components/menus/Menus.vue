<template>
  <div>
    <div class=" media-content">
      <h1 @click="$router.push({name: 'index'})">甜品</h1>
      <div class="is-multiple">
        <el-button size="small" type="primary" @click="ui.addModal=true">添加甜品</el-button>
      </div>
      <br>
      <el-row :gutter="20" class="is-multiple">
        <el-col :span="24">
          <menu-card :menuInfo="menus"></menu-card>
        </el-col>
      </el-row>
      <br>
      <br>
      <br>
    </div>

    <el-dialog
      title="添加甜品"
      :visible.sync="ui.addModal"
      width="30%">
      <el-form ref="form" v-model="menuItem" label-width="80px">
        <el-form-item label="名称">
          <el-input v-model="menuItem.name"></el-input>
        </el-form-item>
        <el-form-item label="单价(分)">
          <el-input v-model="menuItem.price"></el-input>
        </el-form-item>
        <el-form-item label="折扣">
          <el-input place-holder="10为不打折,9为9折" v-model="menuItem.offset"></el-input>
        </el-form-item>
        <el-form-item label="在售">
          <el-switch
            v-model="menuItem.status">
          </el-switch>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="addItem">添加</el-button>
     </span>
    </el-dialog>

  </div>
</template>

<script>
  import MenuCard from './plugin/MenuCard'

  export default {
    inject: ['reload'],
    data () {
      return {
        ui: {
          addModal: false
        },
        sell: true,
        menuItem: {name: '', price: 0, offset: 10, status: true}
      }
    },
    asyncComputed: {
      async menus () {
        try {
          const res = await this.$api.get('/menus/get_menus')
          return JSON.parse(res)
        } catch (e) {
          return []
        }
      }
    },
    methods: {
      async addItem () {
        try {
          await this.$api.post('/menus/create', this.menuItem)
          this.$message({
            message: '创建成功',
            type: 'success'
          })
          this.ui.addModal = false
          this.reload()
        } catch (e) {
          this.$message.error('创建失败')
        }
      }
    },
    components: {
      MenuCard
    }
  }

</script>

<style scoped>
</style>
