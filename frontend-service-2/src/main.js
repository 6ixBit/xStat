// Local imports
import Vue from 'vue'
import App from './App.vue'
import Routes from './routes'
import { store } from "./store/store"

// Third party imports
import iView from 'iview';
import 'iview/dist/styles/iview.css';
import VueRouter from 'vue-router';
import VueMq from 'vue-mq'

Vue.config.productionTip = false

// Activate vue extensions
Vue.use(iView)
Vue.use(VueRouter)
Vue.use(VueMq, {
  breakpoints: {
    mobile: 450,
    tablet: 900,
    laptop: 1250,
    desktop: Infinity,
  }
})


// Register routes
const router = new VueRouter({routes: Routes})

new Vue({
  render: h => h(App),
  store: store,
  router: router
}).$mount('#app')

