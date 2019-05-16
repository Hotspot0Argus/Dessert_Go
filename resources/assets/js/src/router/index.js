import Vue from 'vue'
import Router from 'vue-router'
import Index from '../components/index/Index'
import Orders from '../components/orders/Orders'
import Order from '../components/orders/Order'
import Menus from '../components/menus/Menus'
import Employees from '../components/employees/Employees'
import Logs from '../components/logs/Logs'
import System from '../components/system/System'
import ChangeInfo from '../components/user/ChangeUserInfo'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: Index
    },
    {
      path: '/user/change_info',
      name: 'user:change_info',
      component: ChangeInfo
    },
    {
      path: '/orders',
      name: 'orders',
      component: Orders
    },
    {
      path: '/orders/order',
      name: 'orders:order',
      component: Order
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
