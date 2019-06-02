import axios from 'axios'

const state = {
    status: '',
    token: localStorage.getItem('token') || '',
    user : ''
}

const getters = {
    isLoggedIn: state => !!state.token,
    authStatus: state => state.status,
}

const actions = {
    login({commit}, user){
        return new Promise((resolve, reject) => {
          commit('auth_request')
          axios({url: '/api/auth/obtain_token/', data: user, method: 'POST' })
          .then(resp => {
            const token = resp.data.token
            localStorage.setItem('token', token)
            //console.log(user)
            axios.defaults.headers.common['Authorization'] = token
            axios.post('/api/manage/account/login/', user)
            .then((response) =>{
              //console.log(response)
              commit('auth_success', token)
            })
            
            resolve(resp)
          })
          .catch(err => {
            commit('auth_error')
            localStorage.removeItem('token')
            reject(err)
          })
        })
      },
    logout({commit}){
        return new Promise((resolve) => {
          commit('logout')
          localStorage.removeItem('token')
          delete axios.defaults.headers.common['Authorization']
          axios.post('/api/manage/account/logout/')
          resolve()
        })
    }
}

const mutations = {
    auth_request(state){
        state.status = 'loading'
    },
    auth_success(state, token){
    state.status = 'success'
    state.token = token
    },
    auth_error(state){
    state.status = 'error'
    },
    logout(state){
    state.status = ''
    state.token = ''
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}