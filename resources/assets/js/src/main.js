import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import { $api } from './plugins/api'
import VueSession from 'vue-session'
import AsyncComputed from 'vue-async-computed'
import '../../../../theme/index.css'
import 'font-awesome/scss/font-awesome.scss'
import '../../../../theme/main.css'

Vue.use(ElementUI)
Vue.use(AsyncComputed)
// ref:https://www.npmjs.com/package/vue-session
Vue.use(VueSession)
Vue.use({
  install: function (Vue, options) {
    Object.defineProperty(Vue.prototype, 'uniqId', {
      get: function uniqId () {
        return this._uid
      }
    })
  }
})
Vue.filter('isPrice', function (value) {
  if (!value) return 0
  const yuan = value / 100.0
  return yuan.toFixed(2)
})
Vue.prototype.$api = $api

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: {App}
})
