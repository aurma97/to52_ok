import postService from '../../services/postService'

const state = {
  posts: [],
  post: [],
  myPosts: [],
  types: [],
  categories: [],
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
    postService.showTypes()
    .then(Types => {
      commit('setTypes', Types)
    })
  },

  getCategories ({ commit }) {
    postService.showCategories()
    .then(Categories => {
      commit('setCategories', Categories)
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

  updatePost({ commit },  payload) {
    postService.updatePost(payload)
    .catch(err => state.errors = err.response.status)
    .then(() => {
      commit('addPost', payload)
    })
  },

  deletePost( { commit }, id) {
    postService.deletePost(id)
    .catch(err => state.errors = err.response.status)
    commit('deletePost', id)
  }
}

const mutations = {
  setPosts (state, posts) {
    state.posts = posts
  },
  setTypes (state, types) {
    state.types = types
  },
  setCategories (state, categories) {
    state.categories = categories
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