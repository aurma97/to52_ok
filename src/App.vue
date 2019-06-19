<template>
    <div>
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.4/css/bulma.min.css">
      <link rel="stylesheet" href="https://cdn.materialdesignicons.com/2.5.94/css/materialdesignicons.min.css">
      <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.2.0/css/all.css">
      <link rel="stylesheet" href="https://unpkg.com/vue-multiselect@2.1.0/dist/vue-multiselect.min.css">
      <app-header></app-header>
      <!-- <list-posts></list-posts> -->
      <router-view></router-view>
      <br>
      <br>
      <app-footer></app-footer>
    </div>
</template>

<script>
/* eslint-disable */ 
import Header from './components/test/Header.vue'
import Footer from './components/test/Footer.vue'

export default {
    components:{
        'app-header': Header,
        'app-footer': Footer,
    },
    data(){
      return {
        component:''
      }
    }
}
</script> 
