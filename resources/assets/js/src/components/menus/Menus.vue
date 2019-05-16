<template>
  <div>
    <div class=" media-content">
      <h1 class="">菜单</h1>
      <div class="is-multiple">
        <el-button size="small" type="primary" @click="ui.addModal=true">添加菜品</el-button>
      </div>
      <br>
      <el-row :gutter="20" class="is-multiple">
        <el-col :span="24">
          <menu-card :menuInfo="menuInfo"></menu-card>
        </el-col>
      </el-row>
      <br>
      <br>
      <br>
    </div>

    <el-dialog
      title="添加菜品"
      :visible.sync="ui.addModal"
      width="30%">
      <el-form ref="form" :model="menuInfo" label-width="80px">
        <el-form-item label="名称">
          <el-input></el-input>
        </el-form-item>
        <el-form-item label="单价">
          <el-input></el-input>
        </el-form-item>
        <el-form-item label="折扣">
          <el-input></el-input>
        </el-form-item>
        <el-form-item label="在售">
          <el-switch
            v-model="sell">
          </el-switch>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="ui.addModal=false">取 消</el-button>
        <el-button type="primary">确 定</el-button>
     </span>
    </el-dialog>

  </div>
</template>

<script>
  import MenuCard from './plugin/MenuCard'

  export default {
    data () {
      return {
        ui: {
          addModal: false
        },
        sell: true,
        menuInfo: {
          _id: 111111,
          startTime: '2019-2-18 15:48',
          menuItems: [{
            _id: 15,
            name: '榴莲煎饼',
            price: 1500
          }, {
            _id: 1,
            name: '魅蓝四季春',
            price: 2700
          }, {
            _id: 9,
            name: '热狗',
            price: 800
          }, {
            _id: 23,
            name: 'Mx Tacoo',
            price: 3700
          }, {
            _id: 2,
            name: '猪肉白菜炖粉条',
            price: 3800
          }, {
            _id: 3,
            name: 'T-34坦克',
            price: 40000550
          }]
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
