<template>
    <div class="container" @mouseenter="refresh">
        <hr>
        <hr>
        <nav class="breadcrumb has-succeeds-separator" aria-label="breadcrumbs">     
            <div class="levels">
                <div class="level-left">
                    <ul>
                        <li><router-link to="/">Accueil</router-link></li>
                        <li class="is-active"><a href="#">Mes annonces</a></li>
                    </ul>
                </div>
                <div class="level-right">
                    <div class="has-text-right" v-if="isDelete">
                        <span>
                            <button class="button is-danger" @click="deletePost(idPostToDelete)">Confirmation suppression</button>
                        </span>
                        &nbsp;
                        <span>
                            <button class="button" @click="isDelete = false">Annuler</button>
                        </span>
                    </div>
                </div>
            </div>
        </nav>
        <br>
        <div class="level">
                <div class="level-left">
                    <b-field grouped group-multiline>
                        <b-select v-model="defaultSortDirection">
                            <option value="asc">Tri: ASC</option>
                            <option value="desc">Tri: DESC</option>
                        </b-select>
                        <b-select v-model="perPage">
                            <option value="5">5 par page</option>
                            <option value="10">10 par page</option>
                        </b-select>
                    </b-field>
                </div>
                <div class="level-right">
                    <b-field>
                        <b-input v-model="search" placeholder="Recherche par titre de l'annonce"></b-input>
                    </b-field>
                    <!-- <button @click="showPosts">Show</button> -->
                </div>
        </div>
        <b-table
            :data="filterPosts"
            paginated
            :per-page="perPage"
            :opened-detailed="defaultOpenedDetails"
            ref="table"
            detailed
            detail-key="id"
           
            :current-page.sync="currentPage"
            :default-sort-direction="defaultSortDirection"
            default-sort="name"
            aria-next-label="Page suivante"
            aria-previous-label="Page précedente"
            aria-page-label="Page"
            aria-current-label="Page actuelle">

            <template slot-scope="props" v-if="props.row.author.id == user.id">
                <b-table-column field="name" label="Titre de l'annonce" sortable>
                    <template v-if="showDetailIcon">
                        {{ props.row.title }}
                    </template>
                    <template v-else>
                        <a @click="toggle(props.row)">
                            {{ props.row.title }}
                        </a>
                    </template>
                </b-table-column>

                <b-table-column field="an_type.titl" label="Type" sortable>
                    {{ props.row.an_type.title }}
                </b-table-column>

                <b-table-column field="category.title" label="Categorie" sortable>
                    {{ props.row.category.title }}
                </b-table-column>

                <b-table-column field="date_purchase" label="Date de publication" sortable centered>
                    <span class="tag is-success">
                        {{ new Date(props.row.created_at).toLocaleDateString() }}
                    </span>
                </b-table-column>

                <b-table-column field="last_check" label="Dernière modification" sortable centered>
                    <span class="tag is-warning">
                        {{ new Date(props.row.updated_at).toLocaleDateString() }}
                    </span>
                </b-table-column>

                <b-table-column sortable centered>
                    <b-field grouped group-multiline>
                        <div class="control is-flex">
                            <button class="button is-warning"><i class="fas fa-edit"></i></button>
                        </div>
                        <div>
                            <button class="button is-danger"><i class="fas fa-trash"></i></button>
                        </div>
                    </b-field>
                </b-table-column>
            </template>

            <template slot="detail" slot-scope="props">
                <article class="media">
                    <div class="media-content">
                        <div class="content">
                            <p>
                                <strong>Description : </strong>{{props.row.content}}
                                <br>
                                <strong>Adresse : </strong> {{props.row.num_street}} {{props.row.street}} {{props.row.postalcode}} {{props.row.country}}
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
                        <p>Vous n'avez encore aucune annonce.</p>
                    </div>
                </section>
            </template>
        </b-table>
    </div>
</template>
<script>
import axios from 'axios'
export default {
    data() {
        return {
            defaultSortDirection: 'asc',
            isPaginated: true,
            isPaginationSimple: false,
            currentPage: 1,
            perPage: 5,
            defaultOpenedDetails: [1],
            showDetailIcon: true,
            currentPage: 1,
            perPage: 5,
            search:'',
            isDelete: false,
            idPostToDelete: ''
        }
    },
    computed:{
        user(){
          return this.$store.getters['authentication/user']
        },
        filterPosts(){
            if (!this.myPosts){
                this.isEmpty = true
            }
            return this.myPosts.filter((myPost)=>{
                if(myPost.title){
                    return myPost.title.match(this.search)
                }
            })
        }, 
        myPosts(){
            return this.$store.state.post.myPosts
        }
    },
    methods: {
        showPosts(){
            //console.log(this.myPosts.find(elt => elt.author.id === this.user.id))
            
            console.log(this.myPosts)
        },
        //Pour la liste déroulante de description
        toggle(row) {
            this.$refs.table.toggleDetails(row)
        },
        refresh(){
            this.$store.dispatch('authentication/getUser');
            this.$store.dispatch('post/myPosts', this.user.id);
        },
    },
    created(){
        this.$store.dispatch('authentication/getUser');
        this.$store.dispatch('post/getPosts');
        this.$store.dispatch('post/myPosts', this.user.id);
    }
}
</script>
