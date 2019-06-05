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

        <!-- Modification d'une annonce -->
        <div class="notification is-white" v-if="post && showPost" >
            <h1 class="title is-2">Modification de " {{post.title}} " </h1>        
           <hr> 
            <div class="" v-if="!success">
                <div class="">
                    <section class="notification">
                        <div class="columns">
                            <div class="column">
                                <b-field type="is-fullwidth" label="Catégorie *">
                                    <b-checkbox v-model="newCategory"
                                        native-value="yes">
                                        Modifier la catégorie
                                    </b-checkbox>
                                </b-field>
                            </div>
                            <div class="column">
                                <strong>Catégorie actuelle :</strong> <br>{{postOne.category.title}}
                            </div>
                            <div class="column">
                                <b-field label="Nouvelle catégorie" v-if="newCategory">
                                    <b-select placeholder="Selectionner une catégorie" v-model="post.category">
                                        <option :value="cat.pk" v-for="cat in categories">
                                            {{cat.title}}
                                        </option>
                                    </b-select>
                                </b-field>
                            </div>
                        </div>
                    </section>
                    <br>
                    <section class="notification">
                        <div class="columns">
                            <div class="column">
                                <b-field type="is-fullwidth" label="Type d'annonce *">
                                    <b-checkbox v-model="newType"
                                        native-value="yes">
                                        Modifier le type d'annonce
                                    </b-checkbox>
                                </b-field>
                            </div>
                            <div class="column">
                                <strong>Type actuel :</strong> <br> {{postOne.an_type.title}}
                            </div>
                            <div class="column">
                                <section v-if="newType"> 
                                    <label><strong>Nouveau type : </strong></label>
                                    <div>
                                        <label class="radio" v-for="typ in types">
                                            <input type="radio" name="foobar" v-model="post.an_type" v-bind:value="typ.id">
                                            {{typ.title}}
                                        </label>
                                    </div>
                                </section>
                            </div>
                        </div>
                    </section>
                    <br>
                    <div class="columns notification">
                        <div class="column">
                            <section>
                                <b-field 
                                    label="Titre de l'annonce"
                                    :type="{'is-danger': errors.has('title')}"
                                    :message="[{'Un titre est requis': errors.first('title')}]">
                                    <b-input 
                                        type="is-fullwidth" 
                                        v-model="post.title" 
                                        name="title"
                                        placeholder="Exemple: location TV"
                                        v-validate="'required'"></b-input>
                                </b-field>
                            </section>
                        </div>
                        <div class="column">
                            <section>
                                <b-field 
                                    label="Prix *"
                                    :type="{'is-danger': errors.has('price')}"
                                    :message="[{
                                        'Le prix doit être renseigné' : errors.first('price', 'required'),
                                        'Le prix doit être numérique' : errors.firstByRule('price', 'decimal')
                                    }]">
                                    <p class="control has-icons-right">
                                        <input 
                                            v-model="post.price"
                                            name="price" 
                                            v-validate="'required|decimal'"
                                            class="input" 
                                            type="text">
                                        <span class="icon is-small is-right">
                                            <i class="fas fa-euro-sign"></i>
                                        </span>
                                    </p>
                                </b-field>
                            </section>
                        </div>
                    </div>
                    
                    <br>
                </div>
                <div class="notification">
                    <section>
                        <b-field 
                            type="is-fullwidth" 
                            label="Texte de l'annonce *"
                            :type="{'is-danger': errors.has('content')}"
                            :message="[{'Une description doit être fournie': errors.first('content')}]">
                            <b-input 
                                v-model="post.content"
                                name="content" 
                                v-validate="'required'"
                                type="textarea"></b-input>
                        </b-field>
                    </section>
                    <br>
                    <div class="columns">
                        <div class="column">
                            <h3 class="has-text-centered">Votre adresse</h3>
                            <hr>
                            <div class="columns">
                                <div class="column is-3">
                                    <b-field 
                                        label="N° rue"
                                        :type="{'is-danger': errors.has('num_street')}"
                                        :message="[{
                                            'Le N° de la rue ne doit pas être vide' : errors.first('num_street', 'required'),
                                            'Le N° de la rue doit être numérique' : errors.firstByRule('num_street', 'decimal')
                                        }]">
                                        <p class="control has-icons-left">
                                            <input 
                                                v-model="post.num_street" 
                                                class="input" 
                                                name="num_street"
                                                v-validate="'required|decimal'"
                                                type="text">
                                            <span class="icon is-small is-left">
                                                <i class="fas fa-map-pin"></i>
                                            </span>
                                        </p>
                                    </b-field>
                                </div>
                                <div class="column">
                                    <b-field 
                                        label="Nom de rue"
                                        :type="{'is-danger': errors.has('street')}"
                                        :message="[{'Un nom de rue doit être fourni': errors.first('street')}]">
                                        <p class="control has-icons-left">
                                            <input 
                                                v-model="post.street" 
                                                class="input" 
                                                name="street"
                                                v-validate="'required'"
                                                type="text">
                                            <span class="icon is-small is-left">
                                                <i class="fas fa-map-pin"></i>
                                            </span>
                                        </p>
                                    </b-field>
                                </div>
                            </div>
                        </div>
                        <div class="column">
                            <div class="columns">
                                <div class="column">
                                    <b-field 
                                        label="Ville"
                                        :type="{'is-danger': errors.has('city')}"
                                        :message="[{'Une ville doit être renseignée': errors.first('city')}]">
                                        <p class="control has-icons-left">
                                            <input 
                                                v-model="post.city" 
                                                class="input" 
                                                name="city"
                                                v-validate="'required'"
                                                type="text">
                                            <span class="icon is-small is-left">
                                                <i class="fas fa-map-pin"></i>
                                            </span>
                                        </p>
                                    </b-field>
                                </div>
                                <div class="column">
                                    <b-field 
                                        label="Code postal"
                                        :type="{'is-danger': errors.has('postalcode')}"
                                        :message="[{'Un code postal doit être renseigné': errors.first('postalcode')}]">
                                        <p class="control has-icons-left">
                                            <input 
                                                v-model="post.postalcode" 
                                                class="input" 
                                                name="postalcode"
                                                v-validate="'required'"
                                                type="text">
                                            <span class="icon is-small is-left">
                                                <i class="fas fa-map-pin"></i>
                                            </span>
                                        </p>
                                    </b-field>
                                </div>
                            </div>
                            <div class="columns">
                                <div class="column">
                                    <b-field label="Pays">
                                        <p class="control has-icons-left">
                                            <input v-model="post.country" class="input" value="France" type="text" disabled>
                                            <span class="icon is-small is-left">
                                                <i class="fas fa-map-pin"></i>
                                            </span>
                                        </p>
                                    </b-field>
                                </div>
                                <div class="column">
                                    <b-field grouped group-multiline>
                                        <b-field>
                                            <b-button @click="showPost = false">Annuler</b-button>
                                        </b-field>
                                        <b-field>
                                            <b-button type="is-link" @click.prevent="updatePost(post)">Modifier</b-button>
                                        </b-field>
                                    </b-field>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div>
                        
                        <b-field label="Image(s) actuelle(s)" v-if="post.image_one || post.image_two || post.image_three">
                            <div class="columns">
                                <div class="column">
                                    <b-field v-if="post.image_one">
                                        <img :src="post.image_one" width="300" height="300">
                                    </b-field>
                                    <b-field v-if="post.image_two">
                                        <img :src="post.image_two" width="300" height="300">
                                    </b-field>
                                    <b-field v-if="post.image_three">
                                        <img :src="post.image_three" width="300" height="300">
                                    </b-field>
                                </div>
                                <div class="column">
                                    <b-field type="is-fullwidth" label="Modification">
                                        <b-checkbox v-model="newImage"
                                            native-value="yes">
                                            Ajouter / Modifier des images
                                        </b-checkbox>
                                    </b-field>
                                </div>
                            </div>
                        </b-field>
                        <section v-if="newImage">
                            <b-field label="Joindre des images :">
                                <div class="columns">
                                    <div class="column">
                                        <b-field class="file">
                                            <b-upload v-model="post.image_one">
                                                <a class="button is-link is-inverted">
                                                    <i class="fas fa-upload"></i>
                                                    <span>&ensp;Image 1</span>
                                                </a>
                                            </b-upload>
                                            <span class="file-name" v-if="post.image_one">
                                                {{ post.image_one.name }}
                                            </span>
                                        </b-field>
                                    </div>
                                    <div class="column">
                                        <b-field class="file">
                                            <b-upload v-model="post.image_two">
                                                <a class="button is-link is-inverted">
                                                    <i class="fas fa-upload"></i>
                                                    <span>&ensp;Image 2</span>
                                                </a>
                                            </b-upload>
                                            <span class="file-name" v-if="post.image_two">
                                                {{ post.image_two.name }}
                                            </span>
                                        </b-field>
                                    </div>
                                    <div class="column">
                                        <b-field class="file">
                                            <b-upload v-model="post.image_three">
                                                <a class="button is-link is-inverted">
                                                    <i class="fas fa-upload"></i>
                                                    <span>&ensp;Image 3</span>
                                                </a>
                                            </b-upload>
                                            <span class="file-name" v-if="post.image_three">
                                                {{ post.image_three.name }}
                                            </span>
                                        </b-field>
                                    </div>
                                </div>
                            </b-field>
                        </section>
                    </div>
                </div>
            </div>
        </div>
         <!-- Chargement lors de la sauvegarde -->

        <b-loading :is-full-page="isFullPage" :active.sync="isLoading" :can-cancel="true"></b-loading>
        <section v-if="!showPost">
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
                                <button class="button is-warning" @click="getPost(props.row.id); showPost = true"><i class="fas fa-edit"></i></button>
                            </div>
                            <div>
                                <button class="button is-danger" @click="callDelete(props.row.id)"><i class="fas fa-trash"></i></button>
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
        </section>
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
            idPostToDelete: '',
            //To show edit form
            showPost:false,
            postOne:[],
            post: {
                    id: '',
                    title: '',
                    an_type: '',
                    price: '', 
                    content: '',
                    num_street: '',
                    street: '',
                    city: '',
                    postalcode: '', 
                    image_one: null,
                    image_two: null,
                    image_three: null,
                    country: 'France',
                    category: '',
                    author: 2,
                },
            isLoading: false,
            isFullPage: false,
            success: false,
            newCategory: false,
            newType: false,
            newImage: false,
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
        },
        categories(){
            return this.$store.state.post.categories
        },
        types(){
            return this.$store.state.post.types
        }
    },
    methods: {
        showPosts(){
            //console.log(this.myPosts.find(elt => elt.author.id === this.user.id))
            
            console.log(this.myPosts)
        },
        getPost(id){
            this.postOne = this.filterPosts.find(elt => elt.id === id)

            this.post.id = id
            this.post.title = this.postOne.title
            this.post.an_type = this.postOne.an_type.id
            this.post.price = this.postOne.price
            this.post.content = this.postOne.content
            this.post.num_street = this.postOne.num_street
            this.post.street = this.postOne.street
            this.post.city = this.postOne.city
            this.post.postalcode = this.postOne.postalcode
            this.post.image_two = this.postOne.image_two
            this.post.image_one = this.postOne.image_one
            this.post.image_three = this.postOne.image_three      
            this.post.country = this.postOne.country
            this.post.category = this.postOne.category.id
            this.post.author = this.postOne.author.id
            
        },
        updatePost(post){
            this.$validator.validateAll().then((result) => {
                if (result) {
                     if (this.newCategory){
                            post.category = this.postOne.category.id
                        }else if (this.newType){
                            post.an_type = this.postOne.an_type.id
                        }
                        
                        // if (post.image_one){
                        //     post.image_one = post.image_one.substr(post.image_one.lastIndexOf("/")+1)
                        // }

                        const formData = new FormData();

                        formData.append('title', post.title);
                        formData.append('an_type', post.an_type);
                        formData.append('price', post.price);
                        formData.append('content', post.content);
                        formData.append('num_street', post.num_street);
                        formData.append('street', post.street);
                        formData.append('city', post.city);
                        formData.append('postalcode', post.postalcode);
                        if (post.image_one){
                            this.toDataUrl(post.image_one, function(myBase64) {
                                formData.append('image_one', myBase64);
                            });
                        }
                        if (post.image_two){
                            this.toDataUrl(post.image_two, function(myBase64) {
                                formData.append('image_two', myBase64);
                            });
                        }
                        if (post.image_three){
                            this.toDataUrl(post.image_three, function(myBase64) {
                                formData.append('image_three', myBase64);
                            });
                        }
                        formData.append('country', post.country);
                        formData.append('category', post.category);
                        formData.append('author', this.user.id);

                        var id = post.id

                        this.$store.dispatch('post/updatePost', {id, formData})

                        this.errors = this.$store.dispatch('post/getErrors')
                        if(this.errors != 400 | this.erros != 500){
                            setTimeout(() => {
                                this.$store.dispatch('post/myPosts', this.user.id);
                                this.isLoading = false
                                this.showPost = false
                                this.post = []
                                this.$notification.open({
                                    duration: 5000,
                                    message: `Modification effectuée avec succès`,
                                    position: 'is-bottom-right',
                                    type: 'is-success',
                                    hasIcon: true
                                })
                            }, 500)   
                        }
                        else
                        {
                            this.$notification.open({
                                duration: 5000,
                                message: `Modification impossible, l'équipement est utilisé par une réservation`,
                                position: 'is-bottom-right',
                                type: 'is-danger',
                                hasIcon: true
                            })
                        }
                    }
            })
        },
        toDataUrl(url, callback) {
            var xhr = new XMLHttpRequest();
            xhr.onload = function() {
                var reader = new FileReader();
                reader.onloadend = function() {
                    callback(reader.result);
                }
                reader.readAsDataURL(xhr.response);
            };
            xhr.open('GET', url);
            xhr.responseType = 'blob';
            xhr.send();
        },
        deletePost(id){
            this.$store.dispatch('post/deletePost', id)
            this.isDelete = false
            this.errors = this.$store.dispatch('post/getErrors')
            if(this.errors != 400 | this.erros != 500){
                setTimeout(() => {
                    this.$store.dispatch('post/myPosts', this.user.id);
                    this.isDelete = false
                    this.isLoading = false
                    this.$notification.open({
                        duration: 5000,
                        message: `Suppression effectuée avec succès`,
                        position: 'is-bottom-right',
                        type: 'is-success',
                        hasIcon: true
                    })
                }, 500)   
            }
            else
            {
                this.$notification.open({
                    duration: 5000,
                    message: `Suppression impossible, l'équipement est utilisé par une réservation`,
                    position: 'is-bottom-right',
                    type: 'is-danger',
                    hasIcon: true
                })
            }
        },
        //Pour la liste déroulante de description
        toggle(row) {
            this.$refs.table.toggleDetails(row)
        },
        refresh(){
            this.$store.dispatch('authentication/getUser');
            this.$store.dispatch('post/myPosts', this.user.id);
            this.$store.dispatch('post/getPosts');
            this.$store.dispatch('post/getCategories');
        },
        callDelete(id){
            this.isDelete = true
            this.idPostToDelete = id
        }
    },
    created(){
        this.$store.dispatch('authentication/getUser');
        this.$store.dispatch('post/getPosts');
        this.$store.dispatch('post/getCategories');
        this.$store.dispatch('post/getTypes');
        this.$store.dispatch('post/myPosts', this.user.id);
    }
}
</script>
