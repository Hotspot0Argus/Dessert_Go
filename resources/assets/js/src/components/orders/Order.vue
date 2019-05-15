<template>
  <div>
    <div class="media-content">
      <h1>
        <el-button type="info" style="margin-top: -5px"><i class="fa fa-arrow-left"></i><span style="font-size: 30px">修改订单</span>
        </el-button>
      </h1>
      <br>
      <el-card>
        <el-row :gutter="50">
          <el-col :span="8">
            <h3>{{orderInfo.tableId}} 号桌</h3>
            <hr>
            <el-table max-height="550"
                      :data="orderInfo.menuItems"
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
                label="单价"
                width="100">
                <template slot-scope="scope">
                  {{scope.row.price|isPrice}}
                </template>
              </el-table-column>
            </el-table>
          </el-col>
          <el-col :span="16">
            <div class="is-multiple">
              <el-button type="primary" size="small">添加所选甜品</el-button>
            </div>
          </el-col>
        </el-row>
        <br>
        <hr>
        <br>
        <el-button type="danger" class="pull-right" @click="ui.finishOrder = true">结账</el-button>
        <el-button type="primary">保存订单</el-button>
        <el-button type="primary">取消订单</el-button>
      </el-card>
      <br>
      <br>
      <br>
    </div>
    <el-dialog title="结账" :visible.sync="ui.finishOrder">
      <order-card-content :orderInfo="orderInfo"></order-card-content>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="innerVisible = true">确定结账共 {{orderInfo.total}} 元</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
  import OrderCardContent from './plugin/OrderCardContent'

  export default {
    data () {
      return {
        ui: {
          finishOrder: false,
          cancelOrder: false
        },
        orderInfo: {
          _id: 111111,
          tableId: 6,
          startTime: '2019--2-18 15:48',
          total: 123,
          menuItems: [{
            _id: 15,
            name: '榴莲煎饼',
            number: 1,
            price: 1500
          }, {
            _id: 1,
            name: '魅蓝四季春',
            number: 2,
            price: 2700
          }, {
            _id: 9,
            name: '热狗',
            number: 1,
            price: 800
          }, {
            _id: 1,
            name: '魅蓝四季春',
            number: 2,
            price: 2700
          }, {
            _id: 9,
            name: '热狗',
            number: 1,
            price: 800
          }, {
            _id: 1,
            name: '魅蓝四季春',
            number: 2,
            price: 2700
          }, {
            _id: 9,
            name: '热狗',
            number: 1,
            price: 800
          }, {
            _id: 1,
            name: '魅蓝四季春',
            number: 2,
            price: 2700
          }, {
            _id: 9,
            name: '热狗',
            number: 1,
            price: 800
          }, {
            _id: 1,
            name: '魅蓝四季春',
            number: 2,
            price: 2700
          }, {
            _id: 9,
            name: '热狗',
            number: 1,
            price: 800
          }, {
            _id: 1,
            name: '魅蓝四季春',
            number: 2,
            price: 2700
          }, {
            _id: 9,
            name: '热狗',
            number: 1,
            price: 800
          }, {
            _id: 1,
            name: '魅蓝四季春',
            number: 2,
            price: 2700
          }, {
            _id: 9,
            name: '热狗',
            number: 1,
            price: 800
          }, {
            _id: 1,
            name: '魅蓝四季春',
            number: 2,
            price: 2700
          }, {
            _id: 9,
            name: '热狗',
            number: 1,
            price: 800
          }, {
            _id: 1,
            name: '魅蓝四季春',
            number: 2,
            price: 2700
          }, {
            _id: 9,
            name: '热狗',
            number: 1,
            price: 800
          }, {
            _id: 1,
            name: '魅蓝四季春',
            number: 2,
            price: 2700
          }, {
            _id: 9,
            name: '热狗',
            number: 1,
            price: 800
          }, {
            _id: 1,
            name: '魅蓝四季春',
            number: 2,
            price: 2700
          }, {
            _id: 9,
            name: '热狗',
            number: 1,
            price: 800
          }, {
            _id: 1,
            name: '魅蓝四季春',
            number: 2,
            price: 2700
          }, {
            _id: 9,
            name: '热狗',
            number: 1,
            price: 800
          }, {
            _id: 1,
            name: '魅蓝四季春',
            number: 2,
            price: 2700
          }, {
            _id: 9,
            name: '热狗',
            number: 1,
            price: 800
          }, {
            _id: 1,
            name: '魅蓝四季春',
            number: 2,
            price: 2700
          }, {
            _id: 9,
            name: '热狗',
            number: 1,
            price: 800
          }, {
            _id: 1,
            name: '魅蓝四季春',
            number: 2,
            price: 2700
          }, {
            _id: 9,
            name: '热狗',
            number: 1,
            price: 800
          }, {
            _id: 1,
            name: '魅蓝四季春',
            number: 2,
            price: 2700
          }, {
            _id: 9,
            name: '热狗',
            number: 1,
            price: 800
          }, {
            _id: 1,
            name: '魅蓝四季春',
            number: 2,
            price: 2700
          }, {
            _id: 9,
            name: '热狗',
            number: 1,
            price: 800
          }, {
            _id: 1,
            name: '魅蓝四季春',
            number: 2,
            price: 2700
          }, {
            _id: 9,
            name: '热狗',
            number: 1,
            price: 800
          }, {
            _id: 1,
            name: '魅蓝四季春',
            number: 2,
            price: 2700
          }, {
            _id: 9,
            name: '热狗',
            number: 1,
            price: 800
          }, {
            _id: 23,
            name: 'Mx Tacoo',
            number: 1,
            price: 3700
          }]
        }
      }
    },
    methods: {
      finishOrder () {
        //  请求订单信息
      }
    },
    components: {
      OrderCardContent
    }
  }

</script>

<style scoped>
</style>
