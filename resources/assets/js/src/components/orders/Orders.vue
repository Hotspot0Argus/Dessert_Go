<template>
  <div>
    <div class=" media-content">
      <h1 @click="$router.push({name: 'index'})">所有订单</h1>
      <br>
      <div class="is-multiple">
        <el-button size="small" type="primary" @click="newOrder">新建订单</el-button>
      </div>
      <br>
      <el-row :gutter="20" class="is-multiple">
        <el-col :span="8">
          <order-card :orderInfo="orderInfo"></order-card>
        </el-col>
      </el-row>
      <br>
      <br>
      <br>
    </div>
  </div>
</template>

<script>
  import OrderCard from './plugin/OrderCard'

  export default {
    data () {
      return {
        orderInfo: {
          _id: 111111,
          tableId: 6,
          startTime: '2019--2-18 15:48',
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
            _id: 23,
            name: 'Mx Tacoo',
            number: 1,
            price: 3700
          }]
        }
      }
    },
    asyncComputed: {
      async getOrders () {
        try {
          const orders = await this.$api.get('/orders/get_orders')
          return orders
        } catch (e) {
          return []
        }
      }
    },
    components: {
      OrderCard
    }
  }

</script>

<style scoped>
</style>
