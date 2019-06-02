<template>
    <div>
        <search></search>
        <div class="container">
            <div class="columns">
                <div class="column">
                    <div class="columns">
                        <div class="column is-2">
                            <strong>{{posts.length}} Annonces</strong>
                        </div>
                        <div class="column">
                            <!-- <section>
                                <div class="block">
                                    <b-checkbox type="is-info"
                                        native-value="Flint">
                                        Etudiants <strong><span class="has-text-link">100 000</span></strong>
                                    </b-checkbox>
                                </div>
                            </section> -->
                        </div>
                        <div class="column">
                            <!-- <section>
                                <div class="block">
                                    <b-checkbox type="is-info"
                                        native-value="Flint">
                                        Personnel <strong><span class="has-text-link">100 000</span></strong>
                                    </b-checkbox>
                                </div>
                            </section> -->
                        </div>
                        <div class="column">
                            <section>
                                <b-field type="is-fullwidth"> 
                                    <b-select placeholder="Trier">
                                        <option>Tri : Prix croissants</option>
                                        <option>Tri : Prix décroissants</option>
                                        <option>Tri : Plus anciennes</option>
                                        <option>Tri : Plus récentes</option>
                                    </b-select>
                                </b-field>
                            </section>
                        </div>
                    </div>
                    <div class="notification" v-for="post in posts">
                        <article class="media">
                            <figure class="media-left">
                                <p class="image is-128x128">
                                    <img v-bind:src="url+post.image_one">
                                </p>
                            </figure>
                            <div class="media-content">
                                <div class="content">
                                    <p>
                                        <router-link v-bind:to="'/annonce/'+ post.id"><h3>{{post.title}}</h3></router-link>
                                        <br>
                                        {{post.content}}
                                        <p>
                                             {{post.Category_title}}<br>
                                            {{post.city}} {{post.postalcode}} <br>
                                            {{post.created_at}}
                                        </p>
                                    </p>
                                </div>
                            </div>
                            <div class="media-right">
                                <span class="fas fa-heart"></span>
                            </div>
                        </article>
                        
                    </div>
                </div>
                <div class="column is-3">
                    <div v-for="special in specials">
                        <div class="card">
                            <div class="card-image">
                                <figure class="image is-4by3">
                                    <img :src="url+special.image_one" alt="Placeholder image">
                                </figure>
                            </div>
                            <div class="card-content">
                                <div class="media">
                                    <div class="media-content">
                                        <router-link v-bind:to="'/annonce/'+ special.id"><p class="title is-4">{{special.title}}</p></router-link>
                                    </div>
                                    <div class="media-right">
                                        <span class="fas fa-heart"></span>
                                    </div>
                                </div>
                                <div class="content">
                                {{special.content}}
                                <hr>
                                <p>
                                    {{special.Category_title}}<br>
                                    {{special.city}} {{special.postalcode}}
                                </p>
                                </div>
                            </div>
                        </div>
                        <br>
                    </div>
                    
                </div>
            </div>
            <hr>
        </div>
    
    
    </div>
</template>

<script>
import Search from '../../components/search/Search.vue'
import axios from 'axios'
export default {
    data(){
        return{
            posts: {},
            specials: {},
            url: '/media/'
        }
    },
    methods:{

    },
    created(){
        axios.get('/api/manage/post/all').then(response =>{
            this.posts = response.data;
            this.specials = response.data.slice(0, 2);
        });
    },
    components:{
        'search': Search,
    }
}
</script>

