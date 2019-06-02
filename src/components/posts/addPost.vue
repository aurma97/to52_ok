<template>
    <div class="container">
        <hr>
        <br>
        <nav class="breadcrumb has-succeeds-separator" aria-label="breadcrumbs">
            <ul>
                <li><a href="#">Accueil</a></li>
                <li class="is-active"><a href="#">Déposer une annonce</a></li>
            </ul>
        </nav>
        <hr>
        <div class="container is-info" v-if="success">
          <p class="title has-text-centered">
            Votre annonce a été publiée !
          </p>
          <p>
            <div class="notification is-link has-text-centered">
                <b-button type="is-info"
                    inverted>
                    Accueil
                </b-button>
                &ensp;
                <b-button @click="reset" type="is-info"
                    inverted
                    outlined>
                    Déposer une autre annonce
                </b-button>
                &ensp;
                <b-button type="is-info"
                    inverted
                    outlined>
                    Mes annonces
                </b-button>
            </div>
            </p>
            <hr>
        </div>
        
        <div class="columns" v-if="!success">
            <div class="column is-3">
                <section>
                    <b-field type="is-fullwidth" label="Catégorie *">
                        <b-select placeholder="Selectionner une catégorie" v-model="post.category">
                            <option :value="cat.pk" v-for="cat in categories">
                                {{cat.title}}
                            </option>
                        </b-select>
                    </b-field>
                </section>
                <br>
                <section>
                    <b-field type="is-fullwidth" label="Type d'annonce *">
                        <div class="control">
                            <label class="radio" v-for="typ in postType">
                                <input type="radio" name="foobar" v-model="post.an_type" v-bind:value="typ.id">
                                {{typ.title}}
                            </label>
                        </div>
                    </b-field>
                </section>
                <br>
                <section>
                    <b-field label="Titre de l'annonce">
                        <b-input type="is-fullwidth" v-model="post.title" placeholder="Exemple: location TV"></b-input>
                    </b-field>
                </section>
                <br>
                <section>
                     <b-field label="Prix *">
                        <p class="control has-icons-right">
                            <input v-model="post.price" class="input" type="text">
                            <span class="icon is-small is-right">
                                <i class="fas fa-euro-sign"></i>
                            </span>
                        </p>
                    </b-field>
                 </section>
            </div>
            <div class="column">
                 <section>
                     <b-field type="is-fullwidth" label="Texte de l'annonce *">
                        <b-input v-model="post.content" type="textarea"></b-input>
                    </b-field>
                 </section>
                 <br>
                 <div class="columns">
                    <div class="column">
                        <h3 class="has-text-centered">Votre adresse</h3>
                        <hr>
                        <section>
                            <b-field label="Numéro de rue">
                                <p class="control has-icons-left">
                                    <input v-model="post.num_street" class="input" type="text">
                                    <span class="icon is-small is-left">
                                        <i class="fas fa-map-pin"></i>
                                    </span>
                                </p>
                            </b-field>

                            <b-field label="Nom de rue">
                                <p class="control has-icons-left">
                                    <input v-model="post.street" class="input" type="text">
                                    <span class="icon is-small is-left">
                                        <i class="fas fa-map-pin"></i>
                                    </span>
                                </p>
                            </b-field>
                        </section>
                    </div>
                    <div class="column">
                        <b-field label="Ville">
                                <p class="control has-icons-left">
                                    <input v-model="post.city" class="input" type="text">
                                    <span class="icon is-small is-left">
                                        <i class="fas fa-map-pin"></i>
                                    </span>
                                </p>
                            </b-field>

                            <b-field label="Code postal">
                                <p class="control has-icons-left">
                                    <input v-model="post.postalcode" class="input" type="text">
                                    <span class="icon is-small is-left">
                                        <i class="fas fa-map-pin"></i>
                                    </span>
                                </p>
                            </b-field>

                            <b-field label="Pays">
                                <p class="control has-icons-left">
                                    <input v-model="post.country" class="input" value="France" type="text" disabled>
                                    <span class="icon is-small is-left">
                                        <i class="fas fa-map-pin"></i>
                                    </span>
                                </p>
                            </b-field>
                    </div>
                 </div>
                 <div>
                     <section>
                         <b-field label="Joindre des images :">
                            <div class="columns">
                                <div class="column">
                                    <b-field class="file">
                                        <b-upload v-model="post.image_one">
                                            <a class="button is-primary">
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
                                            <a class="button is-primary">
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
                                            <a class="button is-primary">
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
            <div class="column is-2">
                <section>
                    <figure class="image is-128x128">
                        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTqNUNP1_6Jrwu4eiQES_gzdxYZoOQ5CJdNp_5EgmPJChwBk6A4Xw">
                    </figure>
                </section>
                
                <section>
                    <br>
                    <b-button type="is-link is-fullwidth" @click="savePost" >Ajouter</b-button>
                </section>
            </div>
        </div>
        <div v-for="err in errors">
           {{err}} 
        </div>
    </div>
</template>

<script>
import axios from 'axios'
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
let formData = new FormData();
export default {
     data() {
            return {
                categories: [],
                postType: [],
                post : {
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
                errors: [],
                success: false,
            }
    },
    computed: {
        user(){
          return this.$store.getters['authentication/user']
        }
    },
    methods: {
            savePost(){
                const formData = new FormData();

                formData.append('title', this.post.title);
                formData.append('an_type', this.post.an_type);
                formData.append('price', this.post.price);
                formData.append('content', this.post.content);
                formData.append('num_street', this.post.num_street);
                formData.append('street', this.post.street);
                formData.append('city', this.post.city);
                formData.append('postalcode', this.post.postalcode);
                if (this.post.image_one){
                    formData.append('image_one', this.post.image_one);
                }
                if (this.post.image_two){
                    formData.append('image_two', this.post.image_two);
                }
                if (this.post.image_three){
                    formData.append('image_three', this.post.image_three);
                }
                formData.append('country', this.post.country);
                formData.append('category', this.post.category);
                formData.append('author', this.user.id);
                
                axios.post(`/api/manage/post/`, formData)
                .then(response => {
                    this.success = !this.success
                })
                .catch(e => {
                    this.errors.push(e)
                })
            },
            reset(){
                this.post.title = null
                this.post.an_type = null
                this.post.price = null
                this.post.content = null
                this.post.num_street = null
                this.post.street = null
                this.post.city = null
                this.post.postalcode = null
                this.post.image_one = null
                this.post.image_two = null
                this.post.image_three = null
                this.post.category = null
                this.success = !this.success
            }
        },
        created(){
            axios.get('/api/manage/category/').then(response =>{
                this.categories = response.data;
            });

            axios.get('/api/manage/post/type').then(response =>{
                this.postType = response.data;
            });
        }
}
</script>