<template>
    <div>
        <hr>
        <hr>
        <div class="container">
            <div class="columns">
                <div class="column">
                    <div class="columns">
                        <div class="column is-2">
                            <strong>{{total}} Annonce(s)</strong>
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
            </div>
            <hr>
        </div>
    
        <section class="container">
            <b-pagination
                :total="total"
                :current="current"
                rounded
                :simple="false"
                :per-page="filter.limit"
                @change="pageChange">
            </b-pagination>
        </section>
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
            url: '',
            total: '',
            current: 1,
            order: 'is-centered',
            size: '',
            isSimple: false,
            isRounded: false,
            filter:{
                limit: 5,
                offset: 5,
            }
        }
    },
    methods:{
        pageChange(page){
            this.current = page
            this.filter.offset = ((this.current - 1) * this.filter.limit)
            axios.get(`/api/manage/post/paginated?page=${page}`).then(response => {
                this.posts = response.data.results
            })
        }
    },
    created(){
        axios.get('/api/manage/post/paginated').then(response =>{
            this.posts = response.data.results;
            this.total = response.data.count;
            
            //this.specials = response.data.slice(0, 2);
        });

        this.$store.dispatch('authentication/getUser');
    },
    components:{
        'search': Search,
    }
}
</script>

