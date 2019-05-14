import Vue from 'vue'
import System from '@/components/system/System.vue'

describe('System.vue', () => {
  it('should render correct contents', () => {
    const Constructor = Vue.extend(System)
    const vm = new Constructor().$mount()
    expect(vm.$el.querySelector('.sys h1').textContent)
      .to.equal('System')
  })
})
