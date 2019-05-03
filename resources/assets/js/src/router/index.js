import Vue from 'vue'
import Router from 'vue-router'
import Index from '../components/index/Index'
import Orders from '../components/orders/Orders'
import Menus from '../components/menus/Menus'
import Employees from '../components/employees/Employees'
import Logs from '../components/logs/Logs'
import System from '../components/system/System'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: Index
    },
    {
      path: '/orders',
      name: 'orders',
      component: Orders
    },
    {
      path: '/menus',
      name: 'menus',
      component: Menus
    },
    {
      path: '/employees',
      name: 'employees',
      component: Employees
    },
    {
      path: '/logs',
      name: 'logs',
      component: Logs
    },
    {
      path: '/system',
      name: 'system',
      component: System
    }
  ]
})
