import Vue from 'vue'
import App from '@/App.vue'

import store from '@/store' 
import router from '@/router'

import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
import DateRangePicker from "@gravitano/vue-date-range-picker";
import axios from 'axios'
import { Verify } from 'crypto';
import VeeValidate from 'vee-validate';

Vue.use(VeeValidate);
Vue.use(DateRangePicker);
Vue.use(Buefy)

Vue.prototype.$http = axios;
const token = localStorage.getItem('token')

if (token){
  Vue.prototype.$http.defaults.headers.common['Authorization'] = token
}


Vue.config.productionTip = false

// Vue.use(VueRouter)

const vue = new Vue({
  router,
  store,
  render: h => h(App)
})

vue.$mount('#app')
