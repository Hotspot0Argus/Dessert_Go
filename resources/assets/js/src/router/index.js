import Vue from 'vue'
import Router from 'vue-router'
import Hello from '@/components/Hello'
import Listdd from '@/components/page/Listdd'
import Listcd from '@/components/page/Listcd'
import Listyg from '@/components/page/Listyg'
import Listrz from '@/components/page/Listrz'
import syst from '@/components/page/system'
import other from '@/components/page/other'

Vue.use(Router)
/* eslint-disable */
export default new Router({
  routes: [
    {
      path: '/',
      name: 'Hello',
      component: Hello
    },
    {
      path: '/List_dd',
      name: 'list_dd',
      component: Listdd
    },
    {
      path: '/List_cd',
      name: 'list_cd',
      component: Listcd
    }
    ,
    {
      path: '/List_yg',
      name: 'list_yg',
      component: Listyg
    },
    {
      path: '/List_rz',
      name: 'list_rz',
      component: Listrz
    },
    {
      path: '/system',
      name: 'system',
      component: syst
    },
    {
      path: '/other',
      name: 'other',
      component: other
    }
  ],
  mode: "history"
})
