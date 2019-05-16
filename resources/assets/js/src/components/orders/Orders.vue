<template>
  <div>
    <div class=" media-content">
      <h1 @click="$router.push({name: 'index'})">所有订单</h1>
      <div class="is-multiple">
        <el-button size="small" type="primary" @click="newOrder">新建订单</el-button>
      </div>
      <br>
      <el-row :gutter="20" class="is-multiple">
        <el-col :span="8" v-for="order in orders">
          <order-card :orderInfo="order"></order-card>
        </el-col>
        <div v-if="orders.length ==0" class="has-text-center">
          无订单
        </div>
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
          _id: '',
          tableId: '',
          startTime: '',
          menuItems: []
        }
      }
    },
    asyncComputed: {
      async orders () {
        try {
          const orders = await this.$api.get('/orders/get_orders')
          return JSON.parse(orders)
        } catch (e) {
          return []
        }
      }
    },
    methods: {
      async newOrder () {
        try {
          const orderId = await this.$api.get('/orders/create')
          this.$router.push({name: 'orders:order', params: {order_id: orderId}})
        } catch (e) {
          this.$message.error('新建订单失败')
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
