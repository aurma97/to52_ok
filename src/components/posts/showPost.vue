<template>
    <section class="hero is-link is-bold is-dark is-medium">
    <div class="hero-head">
        <div class="container">
            <br>
            <nav class="breadcrumb has-arrow-separator" aria-label="breadcrumbs">
                <ul>
                   
                    <li><a href="#"><strong>Accueil</strong></a></li>
                    <li><a href="#"><strong>Annonces</strong></a></li>
                    <li class="is-active"><a href="#" aria-current="page">{{post.title}}</a></li>
                </ul>
            </nav>
        </div>
    </div>

    <div class="hero-body">
        <div class="container has-text-centered">
            <hr>
            <p class="title">
                
                {{post.title}}
                <hr>
            </p>
        </div>
        <nav class="level">
            <div class="level-item has-text-centered">
                <div>
                <p class="heading">Auteur</p>
                <hr>
                <p class="title">@{{post.author}}</p>
                </div>
            </div>
            <div class="level-item has-text-centered">
                <div>
                <p class="heading">Posté le</p>
                <hr>
                <p class="title">{{post.created_at}}</p>
                </div>
            </div>
            <div class="level-item has-text-centered">
                <div>
                <p class="heading">Statut</p>
                <hr>
                <p class="title">Ouvert</p>
                </div>
            </div>
            <div class="level-item has-text-centered">
                <div>
                <p class="heading">Catégorie</p>
                <hr>
                <p class="title">Offre</p>
                </div>
            </div>
        </nav>
    </div>
    

    <div class="hero-foot">
        <nav class="tabs is-boxed is-fullwidth">
            <div class="container">
                <template>
                    <b-tabs>
                        <b-tab-item label="Description" icon="playlist-check">
                            <div class="notification">
                                <span class="has-text-primary">
                                    {{post.content}}
                                </span>
                            </div>
                        </b-tab-item>
                        <b-tab-item label="Tarif" icon="cash">
                            <div class="notification">
                                <span class="has-text-primary">
                                    Cout : {{post.price}} €
                                </span>
                            </div>
                        </b-tab-item>
                        <b-tab-item label="Photos" icon="image">
                            <div class="">
                                    <img class="image" v-for="(image, i) in post.images" :src="image" :key="i" @click="index = i">
                                    <vue-gallery-slideshow :images="post.images" :index="index" @close="index = null"></vue-gallery-slideshow>
                            </div>
                        </b-tab-item>
                        <b-tab-item label="Localisation" icon="map-marker">
                            <div class="notification">
                                <span class="has-text-primary">
                                    <strong>Adresse : </strong> {{post.address.num_street}} {{post.address.street}}, {{post.address.postalcode}}, {{post.address.city}}, {{post.address.country}}
                                    <br>
                                </span>
                                <div class="mapouter">
                                    <div class="gmap_canvas">
                                        <iframe width="100%" height="800" :src="'https://maps.google.com/maps?q='+post.address.num_street+'%20'+post.address.street+'%20'+post.address.postalcode+'%20'+post.address.city+'%20'+post.address.country+'&t=&z=13&ie=UTF8&iwloc=&output=embed'">
                                        </iframe>
                                    </div>
                                </div>
                            </div>
                        </b-tab-item>
                        <b-tab-item label="Contacter le vendeur" icon="message-text">
                            <div class="notification is-white">
                                <section>
                                    <b-field label="Votre email">
                                        <b-input placeholder="Email" type="email" disabled></b-input>
                                    </b-field>

                                    <b-field label="Votre téléphone">
                                        <b-input placeholder="Ex: 0600000000"
                                            type="number"
                                            min="10"
                                            max="20">
                                        </b-input>
                                    </b-field>

                                    <b-field label="Objet">
                                        <b-input placeholder="Votre annonce blablabla du 22/07/1997 à 18h06 m'intéresse" type="url"></b-input>
                                    </b-field>

                                    <b-field label="Contenu">
                                        <b-input type="textarea"
                                            minlength="10"
                                            maxlength="100"
                                            placeholder="Maxlength automatically counts characters">
                                        </b-input>
                                    </b-field>
                                    <b-button type="is-link" outlined>Envoyer</b-button>
                                </section>
                            </div>
                        </b-tab-item>
                    </b-tabs>
                </template>
            </div>
        </nav>
    </div>
    </section>
</template>

<script>
import VueGallerySlideshow from 'vue-gallery-slideshow';
import axios from 'axios'
import moment from 'moment'
export default {
    components:{
        VueGallerySlideshow
    },
    data(){
        return {
            id: this.$route.params.id,
            post: {
                title: '',
                an_type: '',
                price: '', 
                content: '',
                created_at:'',
                address: {
                    num_street: '',
                    street: '',
                    city: '',
                    postalcode: '',  
                    country: 'France',
                }, 
                images: {
                    image_one: '',
                    image_two: '',
                    image_three: '',
                },
                category: '',
                author: 'admin',
            },
            index: null
        }
    },
    created(){
        axios.get('/api/post/'+this.id).then(response =>{
            //console.log(response.data[0]);
            this.post.title = response.data[0].title
            this.post.an_type = response.data[0].an_type
            this.post.category = response.data[0].category
            this.post.address.num_street = response.data[0].num_street
            this.post.address.street = response.data[0].street
            this.post.address.city = response.data[0].city
            this.post.address.postalcode = response.data[0].postalcode
            this.post.price = response.data[0].price
            this.post.content = response.data[0].content
            this.post.country = response.data[0].country
        });

        axios.get('/api/post/date/'+this.id).then(response =>{
            this.post.images.image_one = response.data.image_one
            this.post.images.image_two = response.data.image_two
            this.post.images.image_three = response.data.image_three
            this.post.created_at = moment([response.data.created_at])
            this.post.updated_at = response.data.updated_at
        });
    }
}
</script>
<style scoped>
.image {
  width: 400px;
  height: 200px;
  background-size: cover;
  cursor: pointer;
  margin: 10px;
  border-radius: 3px;
  border: 1px solid lightgray;
  object-fit: contain;
  display: inline-block;
}
</style>
