<template>
    <section>
        <section>
            <br>
             <b-message title="Bienvenue sur votre site de gestionne d'annonces" type="container is-info" aria-close-label="Close message">
                Nous espérons que vous trouverez votre compte
            </b-message>
            <br>
            <div class="columns">
                <div class="column is-1"></div>
                <div class="column is-2">
                    <h1 class="title is-4">Critères de recherche</h1>
                    <b-field label="Recherche par titre" type="is-fullwidth">
                        <b-input placeholder="Une montre connectée ?" v-model="search" ></b-input>                               
                    </b-field>
                    
                    <b-field label="Annonces par page" type="is-fullwidth">
                        <b-select v-model="perPage">
                            <option value="5">5 par page</option>
                            <option value="10">10 par page</option>
                            <option value="15">15 par page</option>
                            <option value="20">20 par page</option>
                        </b-select>
                    </b-field>
                    <b-field label="Filtre par catégorie" type="is-fullwidth">
                        <multiselect 
                            v-model="value" 
                            :options="options" 
                            :multiple="true" 
                            :close-on-select="false" 
                            :clear-on-select="false" 
                            :preserve-search="true" 
                            placeholder="Ajouter une catégorie" 
                            label="title" 
                            track-by="title" 
                            :preselect-first="true">
                            <template 
                                slot="selection" 
                                slot-scope="{ values, search, isOpen }">
                                <span 
                                    class="multiselect__single" 
                                    v-if="values.length &amp;&amp; !isOpen">
                                    {{ values.length }} selectionné(s)
                                </span>
                            </template>
                        </multiselect>
                    </b-field>

                    <b-field v-if="value">
                        <pre><code v-for="val in value">[x] {{ val.title }}<br></code></pre>
                    </b-field>

                    <b-field label="Recherche par prix" type="is-fullwidth">
                        <div class="columns">
                            <div class="column">
                                <b-input placeholder="Min" v-model="priceMin" ></b-input>                               
                            </div>
                            <div class="column">
                                <b-input placeholder="Max" v-model="priceMax" ></b-input>  
                            </div>
                        </div>                             
                    </b-field>
                    <!-- <pre>
                        {{filterPostsByPrice}}
                    </pre> -->
                </div>
                <div class="column">
                    <h1 class="title is-4">Liste des annonces</h1>
                    <b-table
                        type="container"
                        :data="isEmpty ? [] : filterPosts"
                        :paginated="isPaginated"
                        :per-page="perPage"
                        :opened-detailed="defaultOpenedDetails"
                        ref="table"
                        detailed
                        detail-key="id"
                        @details-open="(row, index) => $toast.open(`Expanded ${row.title}`)"
                        :show-detail-icon="showDetailIcon"
                        :current-page.sync="currentPage"
                        default-sort="name"
                        aria-next-label="Page suivante"
                        aria-previous-label="Page précedente"
                        aria-page-label="Page"
                        aria-current-label="Page actuelle">

                        <template slot-scope="props">
                            <b-table-column field="name" label="Titre" sortable>
                                <template v-if="showDetailIcon">
                                    <strong class="has-text-link">{{ props.row.title }}</strong>
                                </template>
                                <template v-else>
                                    <a @click="toggle(props.row)">
                                        <strong class="notification is-link">{{ props.row.title }}</strong>
                                    </a>
                                </template>
                            </b-table-column>

                            <b-table-column field="price" label="Prix" sortable>
                                <span class="tag is-success">
                                    {{ props.row.price }} €
                                </span>
                            </b-table-column>

                            <b-table-column field="an_type.title" label="Type" sortable>
                                {{ props.row.an_type.title }}
                            </b-table-column>

                            <b-table-column field="category.title" label="Categorie" sortable>
                                {{ props.row.category.title }}
                            </b-table-column>

                            <b-table-column field="date_purchase" label="Date publication" sortable centered>
                                <span class="tag is-success">
                                    {{ new Date(props.row.created_at).toLocaleDateString() }}
                                </span>
                            </b-table-column>

                            <b-table-column sortable centered>
                                <b-field grouped group-multiline>
                                    <div class="control is-flex">
                                        <router-link :to="'/annonce/'+ props.row.id"><i :title="'Consulter \''+props.row.title+'\''" class="fas fa-search"></i></router-link>
                                    </div>
                                </b-field>
                            </b-table-column>
                        </template>

                        <template slot="detail" slot-scope="props">
                            <article class="media">
                                <div class="media-content">
                                    <div class="content">
                                        <p>
                                            <span class="title is-5">{{ props.row.title }}</span>
                                            <br>
                                            <strong>Description: </strong>{{props.row.content}}
                                            <br>
                                            <strong>Adresse: </strong>{{props.row.num_street}} {{props.row.street}} {{props.row.city}} {{props.row.postalcode}} {{props.row.country}}
                                        </p>
                                        <p v-if="props.row.image_one">
                                            <strong>Illustrations:</strong>
                                            <br>
                                            <div class="columns">
                                                <div class="column" v-if="props.row.image_one">
                                                    <img :src="props.row.image_one" width="300" height="200">
                                                </div>
                                                <div class="column" v-if="props.row.image_two">
                                                    <img :src="props.row.image_two" width="300" height="200">
                                                </div>
                                                <div class="column" v-if="props.row.image_three">
                                                    <img :src="props.row.image_three" width="300" height="200">
                                                </div>
                                            </div>
                                        </p>
                                    </div>
                                </div>
                            </article>
                        </template>

                        <!-- isEmpty -->
                        <template slot="empty">
                            <section class="section">
                                <div class="content has-text-grey has-text-centered">
                                    <p>
                                        <b-icon
                                            icon="emoticon-sad"
                                            size="is-large">
                                        </b-icon>
                                    </p>
                                    <p>Rien par ici.</p>
                                </div>
                            </section>
                        </template>
                    </b-table>
                  
                </div>
                <div class="column is-2">
                    <h1 class="title is-4">A la une</h1>
                    <div v-for="special in specials">
                        <div class="card">
                            <div class="card-image">
                                <figure class="image is-4by3">
                                    <img :src="special.image_one" alt="Placeholder image">
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
                <div class="column is-1"></div>
            </div>
        </section>
    </section>
</template>

<script>
import axios from 'axios'
import Multiselect from 'vue-multiselect'
export default {
    components:{
        Multiselect
    },
    data(){
        return{
            posts: [],
            specials: [],
            isPaginated: true,
            isPaginationSimple: false,
            currentPage: 1,
            perPage: 5,
            defaultOpenedDetails: [1],
            showDetailIcon: true,
            search:'',
            isEmpty: false,
            options: [
            ],
            value: [],
            priceMin:'',
            priceMax:''
        }
    },
    methods:{
        //Pour la liste déroulante de description
        toggle(row) {
            this.$refs.table.toggleDetails(row)
        }
    },
    computed: {
        filterPosts(){
            return this.posts.filter((post)=>{
                if(post.title){
                    return post.title.match(this.search)
                }
            })
        },
        // filterPostsByPrice(){
        //     return this.posts.find(elt => {
        //         (elt.price == this.priceMin) || (elt.price == this.priceMax)
        //     })
        // } 
    },
    created(){
        axios.get('/api/manage/post/all').then(response =>{
            this.posts = response.data;
            this.specials = response.data.slice(0,1)
        });
        axios.get('/api/manage/category').then(response =>{
            console.log(response.data)
            this.options = response.data
        })

        this.$store.dispatch('authentication/getUser');
    },
}
</script>

