import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import axios from 'axios'
import { $api } from './api'
import 'element-ui/lib/theme-chalk/index.css'

Vue.use(ElementUI)
Vue.prototype.$axios = axios
Vue.prototype.$api = $api

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: {App}
})
