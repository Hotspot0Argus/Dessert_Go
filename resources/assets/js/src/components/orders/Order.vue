<template>
  <div v-if="getOrder">
    <div class="media-content">
      <h1 @click="$router.push({name:'orders'})">
        修改订单
      </h1>
      <br>
      <el-card>
        <el-row :gutter="50">
          <el-col :span="8">
            桌号:
            <el-input v-model="getOrder.table_id" placeholder="请输入内容" style="width: 120px" size="small"></el-input>
            <hr>
            <el-table max-height="550"
                      :data="menuList"
                      style="width: 100%">
              <el-table-column
                prop="name"
                label="名称"
                width="100">
              </el-table-column>
              <el-table-column
                label="数量">
                <template slot-scope="scope">
                  <el-input-number size="small" v-model="scope.row.number" :min="0"
                                   label="描述文字"></el-input-number>
                </template>
              </el-table-column>
              <el-table-column
                label="折后价"
                width="100">
                <template slot-scope="scope">
                  {{scope.row.price|isPrice}}
                </template>
              </el-table-column>
            </el-table>
          </el-col>
          <el-col :span="16">
            <div class="is-multiple">
              <el-button type="primary" size="small" @click="addSelectedDessert">添加所选甜品</el-button>
            </div>
            <el-table
              :data="menus"
              style="width: 100%" max-height="450" @selection-change="handleSelectionChange">
              <el-table-column
                type="selection"
                width="55">
              </el-table-column>
              <el-table-column
                label="名称"
                min-width="150">
                <template slot-scope="scope">
                  {{scope.row.fields.name}}
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
          </el-col>
        </el-row>
        <br>
        <hr>
        <br>
        <el-button type="danger" class="pull-right" @click="ui.finishOrder = true">结账</el-button>
        <el-button type="primary" @click="saveOrder">保存订单</el-button>
        <el-button type="primary" @click="canOrder">取消订单</el-button>
      </el-card>
      <br>
      <br>
      <br>
    </div>
    <el-dialog title="结账" :visible.sync="ui.finishOrder">
      <order-card-content :menuInfo="menuList"></order-card-content>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="finishOrder">确定结账共 {{count()|isPrice}} 元</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
  import OrderCardContent from './plugin/OrderCardContent'

  export default {
    prop: ['menuInfo'],
    data () {
      return {
        ui: {
          finishOrder: false,
          cancelOrder: false
        },
        selectedItems: [],
        menuList: []
      }
    },
    asyncComputed: {
      async menus () {
        try {
          const res = await this.$api.get('/menus/get_menus_on_sell')
          return JSON.parse(res)
        } catch (e) {
          return []
        }
      },
      async getOrder () {
        try {
          const id = this.$route.params.order_id
          const info = await this.$api.get('/orders/get_order', {order_id: id})
          if (info) {
            this.menuList = JSON.parse(info.menu_list)
            return info
          }
        } catch (e) {
          this.menuList = []
          return []
        }
      }
    },
    methods: {
      async finishOrder () {
        try {
          const id = this.$route.params.order_id
          await this.$api.post('/orders/finish_order', {
            order_id: id,
            status: 'finish'
          })
          this.$message('入账成功,请打开收款机收款')
        } catch (e) {
          this.$message.error('入账失败')
        }
      },
      count () {
        let total = 0
        for (const item of this.menuList) {
          total += parseInt(item.price) * parseInt(item.number)
        }
        return total
      },
      addSelectedDessert () {
        if (!this.menuList) {
          this.menuList = this.selectedItems
          return
        }
        this.menuList = this.menuList.concat(this.selectedItems)
      },
      handleSelectionChange (items) {
        this.selectedItems = []
        for (const item of items) {
          this.selectedItems.push({
            item_id: item.pk,
            name: item.fields.name,
            number: 1,
            price: item.fields.price * 0.1 * item.fields.offset
          })
        }
      },
      async saveOrder () {
        try {
          const id = this.$route.params.order_id
          await this.$api.post('/orders/modify_order', {
            order_id: id,
            table_id: this.getOrder.table_id,
            menu_list: JSON.stringify(this.menuList),
            status: 'ing'
          })
          this.$message('保存成功')
        } catch (e) {
          this.$message.error('保存失败')
        }
      },
      async canOrder () {
        try {
          const id = this.$route.params.order_id
          await this.$api.post('/orders/modify_order', {
            order_id: id,
            table_id: this.getOrder.table_id,
            menu_list: JSON.stringify(this.menuList),
            status: 'err'
          })
          this.$message('取消成功')
        } catch (e) {
          this.$message.error('取消失败')
        }
      }
    },
    components: {
      OrderCardContent
    }
  }
</script>

<style scoped>
</style>
