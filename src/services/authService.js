import api from '@/services/api'

const config = {
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
}

export default {
  logout() {
    return api.get(`account/logout/`)
              .then(response => response.data)
  },
  login(payload) {
    return api.post(`auth/login/`, payload)
              .then(response => response.data)
  },
  //obtainJwt = api.get,
}