<template>
  <div v-if="data2">
    <el-header style="padding: 0;z-index: 1000">
      <el-menu
        :default-active="activeIndex2"
        mode="horizontal"
        @select="handleSelect"
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b">
        <el-row type="flex" justify="end">
          <el-menu-item index="1">处理中心</el-menu-item>
          <el-submenu index="2">
            <template slot="title">我的工作台</template>
            <el-menu-item index="2-1">选项1</el-menu-item>
            <el-menu-item index="2-2">选项2</el-menu-item>
            <el-menu-item index="2-3">选项3</el-menu-item>
            <el-submenu index="2-4">
              <template slot="title">选项4</template>
              <el-menu-item index="2-4-1">选项1</el-menu-item>
              <el-menu-item index="2-4-2">选项2</el-menu-item>
              <el-menu-item index="2-4-3">选项3</el-menu-item>
            </el-submenu>
          </el-submenu>
          <el-menu-item index="3">消息中心</el-menu-item>
          <el-menu-item index="4"><a href="https://www.ele.me" target="_blank">登陆</a></el-menu-item>
        </el-row>
      </el-menu>
    </el-header>
    <el-main style="background-color: #E8EBF0; margin-top: -3px;min-height: 45rem">
      <h1>{{ msg }}</h1>
      <h2>Essential Links</h2>
      <ul>
        <li><a href="https://vuejs.org" target="_blank">Core Docs</a></li>
        <li><a href="https://forum.vuejs.org" target="_blank">Forum</a></li>
        <li><a href="https://gitter.im/vuejs/vue" target="_blank">Gitter Chat</a></li>
        <li><a href="https://twitter.com/vuejs" target="_blank">Twitter</a></li>
        <br>
        <li><a href="http://vuejs-templates.github.io/webpack/" target="_blank">Docs for This Template</a></li>
      </ul>
      <h2>Ecosystem</h2>
      <ul>
        <li><a href="http://router.vuejs.org/" target="_blank">vue-router</a></li>
        <li><a href="http://vuex.vuejs.org/" target="_blank">vuex</a></li>
        <li><a href="http://vue-loader.vuejs.org/" target="_blank">vue-loader</a></li>
        <li><a href="https://github.com/vuejs/awesome-vue" target="_blank">awesome-vue</a></li>
      </ul>

      <div>
        <h2>GET data from Django API (/api/test)</h2>

        <div class="wrapper">
          <p>/api/test</p>
          <span>foo</span>: <span>{{ data2.foo }}</span>
          <span>foo</span>: <span>{{ data3 }}</span>
        </div>
      </div>
      Main
      <Header></Header>
    </el-main>
    <el-footer style="background-color: #E8EBF0;padding: 0;min-height: 10rem">
      <hr style="margin: 0;color: black">
      <el-row type="flex" class="row-bg" justify="center">
        <el-col :span="6">
          <div class="grid-content bg-purple-light">123</div>
        </el-col>
      </el-row>
    </el-footer>
  </div>
</template>

<script>
  import Header from './Index'

  export default {
    name: 'hello',
    data () {
      return {
        msg: 'Welcome to Your Vue.js App',
        testData: ''
      }
    },
    // 异步加载数据
    asyncComputed: {
      data2 () {
        return this.$api.get('/menu/test')
      },
      data3 () {
        return '11'
      }
    },
    components: {
      Header
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1, h2 {
    font-weight: normal;
  }

  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    display: inline-block;
    margin: 0 10px;
  }

  a {
    color: #42b983;
  }

  .wrapper {
    padding: 20px 40px;
    border: 1px solid #c0c0c0;
    max-width: 400px;
    margin: 0 auto;
    background: orange;
  }
</style>
