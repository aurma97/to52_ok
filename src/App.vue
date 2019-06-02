<template>
    <div>
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.4/css/bulma.min.css">
      <link rel="stylesheet" href="https://cdn.materialdesignicons.com/2.5.94/css/materialdesignicons.min.css">
      <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.2.0/css/all.css">
      <app-header></app-header>
      <!-- <list-posts></list-posts> -->
      <router-view></router-view>
    </div>
</template>

<script>
import Header from './components/test/Header.vue'

export default {
    components:{
        'app-header': Header
    },
    data(){
      return {
        component:''
      }
    }
}
</script> 
