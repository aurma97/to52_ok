import Vue from 'vue'
import Vuex from 'vuex'
import authentication from './modules/authentication'
import post from './modules/post'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    authentication,
    post
  }
})