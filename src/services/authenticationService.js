import api from '@/services/api'

const config = {
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
}

export default {
  login(payload) {
    return api.post(`auth/obtain_token/`, payload)
              .then(response => response)
  }, 
}