import postService from '../../services/postService'

const state = {
  posts: [],
  post: [],
  myPosts: [],
  errors: ''
}

const getters = {
  posts: state => {
    return state.posts
  }
}

const actions = {
  getPosts ({ commit }) {
    postService.fetchPosts()
    .then(Posts => {
      commit('setPosts', Posts)
    })
  },

  getTypes ({ commit }) {
    postService.fetchTypes()
    .then(Types => {
      commit('setTypes', Types)
    })
  },

  getErrors () {
    return state.errors
  },

  getPost ({ commit }, id) {
    postService.showPost(id)
    .then(id => {
      commit('getPost', id)
    })
  },

  myPosts ({ commit }, id) {
    postService.myPosts(id)
    .then(myPosts => {
      commit('myPosts', myPosts)
    })
  },

  addPost({ commit }, Equipment) {
    postService.postPost(Equipment)
    .catch(err => state.errors = err.response.status)
    .then(() => {
      commit('addPost', Equipment)
    })
  },

  updatePost({ commit }, payload) {
    postService.updatePost(payload)
    .catch(err => state.errors = err.response.data)
    .then(() => {
      commit('addPost', payload)
    })
  },

  deletePost( { commit }, id) {
    postService.deletePost(id)
    .catch(err => state.errors = err.response.data)
    commit('deletePost', id)
  }
}

const mutations = {
  setPosts (state, posts) {
    state.posts = posts
  },
  getPost(state, post) {
    state.post = post
  },
  myPosts(state, myPosts) {
    state.myPosts = myPosts
  },
  addPost(state, post) {
    state.posts.push(post)
  },
  updatePost(state, id, payload) {
    state.posts = state.posts.filter(obj => obj.pk !== id)
    state.posts.push(payload)
  },
  deletePost(state, id) {
    state.posts = state.posts.filter(obj => obj.pk !== id)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}