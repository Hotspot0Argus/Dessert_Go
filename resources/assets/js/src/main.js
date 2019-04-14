import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import { $api } from './plugins/api'
import SessionPlugin from './plugins/session'
import AsyncComputed from 'vue-async-computed'
import '../../../../theme/index.css'

Vue.use(ElementUI)
Vue.use(SessionPlugin)
Vue.use(AsyncComputed)
Vue.prototype.$api = $api

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: {App}
})
