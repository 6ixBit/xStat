// Local imports
import Vue from 'vue'
import App from './App.vue'
import Routes from './routes'

// Third party imports
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VueRouter from 'vue-router'

Vue.config.productionTip = false

// Activate vue extensions
Vue.use(BootstrapVue)
Vue.use(VueRouter)

// Register routes
const router = new VueRouter({routes: Routes})

new Vue({
  render: h => h(App),
  router
}).$mount('#app')

