<template>
  <div>
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>桌号: {{parseInt(orderInfo.fields.table_id)<0?'未确定':orderInfo.fields.table_id}}</span>
        <el-button style="float: right; padding: 3px 0" type="text"
                   @click="$router.push({name:'orders:order',params:{order_id:orderInfo.pk}})">查看和编辑
        </el-button>
      </div>
      <order-card-content :menuInfo="JSON.parse(orderInfo.fields.menu_list)">
      </order-card-content>
      <hr>
      <span class="is-text-gain is-text-small">{{orderInfo.fields.start_time}}</span>
      <span class="pull-right">总计:{{count|isPrice}}</span>
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
    data () {
      return {
        menuList: [
          {
            'name': '',
            'number': 1,
            'price': 0
          }
        ]
      }
    },
    computed: {
      count () {
        let total = 0
        for (const item of JSON.parse(this.orderInfo.fields.menu_list)) {
          total += parseInt(item.price) * parseInt(item.number)
        }
        return total
      }
    },
    components: {
      OrderCardContent
    }
  }
</script>

<style scoped>

</style>
