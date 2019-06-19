import Vue from 'vue'
import Router from 'vue-router'
import listPosts from '@/components/posts/listPosts.vue';
import showPost from '@/components/posts/showPost.vue';
import myPosts from '@/components/posts/myPosts.vue';
import addPost from '@/components/posts/addPost.vue';
import login from '@/components/accounts/Login.vue';
import register from '@/components/accounts/Register.vue';
import Accounts from '@/components/accounts/Accounts.vue';
import store from '@/store' 

Vue.use(Router)

let router = new Router({
  routes: [
    { 
      path: '/', 
      component: listPosts,
    },
    { 
        path: '/nouvelle-annonce', 
        component:addPost, 
        meta: { 
            requiresAuth: true
        }
    },
    { 
        path: '/connexion', 
        name: 'connexion',
        component:login
    },
    { 
      path: '/mon-compte', 
      component: Accounts,
      meta: {
        requiresAuth: true
      }
    },
    { 
        path: '/inscription', 
        component:register
    },
    { 
        path: '/annonce/:id', 
        component:showPost
    },
    { 
      path: '/mes-annonces', 
      component:myPosts,
      meta: { 
          requiresAuth: true
      }
  },
  ]
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // this route requires auth, check if logged in
    // if not, redirect to login page.
    if (!store.getters['authentication/isLoggedIn']) {
      next({ name: 'connexion' })
    } else {
      next() // go to wherever I'm going
    }
  } else {
    next() // does not require auth, make sure to always call next()!
  }
})

export default router;