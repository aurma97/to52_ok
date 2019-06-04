import Vue from 'vue'
import Router from 'vue-router'
import listPosts from '@/components/posts/listPosts.vue';
import showPost from '@/components/posts/showPost.vue';
import myPosts from '@/components/posts/myPosts.vue';
import addPost from '@/components/posts/addPost.vue';
import login from '@/components/accounts/Login.vue';
import register from '@/components/accounts/Register.vue';

Vue.use(Router)

let router = new Router({
  routes: [
    { 
      path: '/', 
      component: listPosts,
      meta: { 
        requiresAuth: true
      }
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
        component:login
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
      component:myPosts
  },
  ]
})

export default router;