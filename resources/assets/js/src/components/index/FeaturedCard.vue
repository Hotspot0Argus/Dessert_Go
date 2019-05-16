<template>
  <div class="is-padding-less">
    <el-card :body-style="{ padding: '0px' }" shadow="never" class="box-card is-padding-less function-menu is-hoverable"
             @click.native="click">
      <div class="title"><i class="fa fa-square fa-fw"
                            :class="{'is-text-danger':routeName==='orders','is-text-warning':routeName==='menus','is-text-info':routeName==='employees','is-text-primary':routeName==='logs','is-text-gain':routeName==='system'}"></i>{{category}}
      </div>
      <div class="is-footer is-text-small">{{detail}}</div>
    </el-card>
  </div>
</template>

<script>
  export default {
    props: ['category', 'routeName', 'detail'],
    computed: {
      user () {
        return this.$session.get('user')
      }
    },
    methods: {
      click () {
        if (this.user && this.user.person_id > 0) {
          if (this.routeName === 'orders') {
            this.$router.push({name: this.routeName})
          } else if (this.user.position > 1) {
            this.$router.push({name: this.routeName})
          }
          return
        }
        this.$message('请登录')
      }
    }
  }
</script>

<style scoped>


  .function-menu {
    height: 13rem;
    border-width: 1px;
  }

  .is-footer {
    height: 1.5rem;
    background-color: #E8EBF0;
    position: relative;
    text-align: center;
    top: 7rem;
  }

  .box-card {
    border-color: #DCDFE6;
    box-shadow: 0 1px 1px rgba(0, 0, 0, 0.28);
  }

  .title {
    padding: 1.5rem;
  }
</style>
