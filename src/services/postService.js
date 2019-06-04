import api from '@/services/api'

const config = {
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
}

export default {
  fetchPosts() {
    return api.get(`post/all`)
              .then(response => response.data)
  },
  showPost(id) {
    return api.get(`post/:${id}`)
              .then(response => response.data)
  },
  myPosts(id){
    return api.get('/post/author/?author_id='+id)
              .then(response => response.data)
  },
  showTypes(){
    return api.get('post/type')
              .then(response => response.data)
  },
  postPost(payload) {
    return api.post(`post/`, payload)
              .then(response => response.data)
  },
  updatePost(payload) {
    return api.put(`post/${payload.id}`, payload)
              .then(response => response.data)
  },
  deletePost(id) {
    return api.delete(`post/${id}`)
              .then(response => response.data)
  }
}