import Vue from 'vue'
import App from './App.vue'
import Vuex from 'vuex'
import storeConfig from './store/index.js'
import vuetify from '@/plugins/vuetify' // path to vuetify export

let update = () => {store.dispatch('templates/getListPatterns')}
// Vue.config.productionTip = false
// Vue.config.keyCodes.enter = 13
Vue.use(Vuex)
export const eventBus = new Vue()


document.addEventListener('DOMContentLoaded', function (event) {
  let store = new Vuex.Store(storeConfig)
  global['store'] = store

  window.vm = new Vue({
    store,
    vuetify,
    render: h => h(App)
  }).$mount('#app')

  store.dispatch('templates/getListPatterns')
  setInterval(update(), 1*60*1000)
})
