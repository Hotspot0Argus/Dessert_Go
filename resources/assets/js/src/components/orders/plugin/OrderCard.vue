<template>
  <div>
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>桌号{{orderInfo.tableId}}</span>
        <el-button style="float: right; padding: 3px 0" type="text" @click="$router.push({name:'orders:order'})">查看和编辑
        </el-button>
      </div>
      <order-card-content :orderInfo="orderInfo">
      </order-card-content>
      <hr>
      <span class="is-text-gain is-text-small">{{orderInfo.startTime}}</span>
      <span class="pull-right">总计:123</span>
      <br>
      <br>
    </el-card>
    <br>
  </div>
</template>

<script>
  import OrderCardContent from './OrderCardContent'

  export default {
    props: ['orderInfo'],
    components: {
      OrderCardContent
    }
  }
</script>

<style scoped>

</style>
