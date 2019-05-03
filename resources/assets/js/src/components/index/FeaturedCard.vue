<template>
  <div class="is-padding-less">
    <el-card :body-style="{ padding: '0px' }" shadow="never" class="box-card is-padding-less function-menu is-hoverable"
             @click.native="$router.push({name: 'system'})">
      <div class="title"><i class="fa fa-square fa-fw is-text-danger"></i>系统管理</div>
      <div class="is-footer">123</div>
    </el-card>

  </div>
</template>

<script>
  export default {}
</script>

<style scoped>


  .function-menu {
    height: 13rem;
    border-width: 1px;
  }

  .is-footer {
    height: 2.5rem;
    background-color: #E8EBF0;
    position: relative;
    top: 6rem;
  }

  .box-card {
    border-color: #DCDFE6;
    box-shadow: 0 1px 1px rgba(0, 0, 0, 0.28);
  }

  .title {
    padding: 1.5rem;
  }
</style>
