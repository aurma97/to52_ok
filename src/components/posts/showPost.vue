<template>
    <section class="hero is-ligth is-bold is-medium">
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

    <div>
        <br>
        <div class="container has-text-centered">
            <br>
            <p class="title">
                {{post.title}}
                <hr>
            </p>
        </div>
        <br>
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
                <p class="title">{{new Date(post.created_at).toLocaleDateString()}}</p>
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
            <div class="level-item has-text-centered">
                <div>
                <p class="heading">Prix</p>
                <hr>
                <p class="title">{{post.price}} €</p>
                </div>
            </div>
        </nav>
    </div>
    <br>
    <div class="hero-foot">
        <br>
        <nav class="tabs is-boxed is-fullwidth">
            <div class="container">
                <template>
                    <b-tabs>
                        <b-tab-item label="Description" icon="playlist-check">
                            <div>
                                <span class="has-text-link">
                                    {{post.content}}
                                </span>
                            </div>
                        </b-tab-item>
                        <b-tab-item label="Photos" icon="image">
                            <div>
                                    <img class="image" v-for="(image, i) in post.images" :src="image" :key="i" @click="index = i" v-if="image">
                                    <vue-gallery-slideshow :images="post.images" :index="index" @close="index = null"></vue-gallery-slideshow>
                            </div>
                        </b-tab-item>
                        <b-tab-item label="Localisation" icon="map-marker">
                            <div>
                                <span class="has-text-link">
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
                            <div>
                                <section>
                                    <b-field 
                                        label="Emetteur">
                                        <b-input 
                                            placeholder="Email" 
                                            type="email" 
                                            disabled 
                                            v-model="mail.sender">
                                        </b-input>
                                    </b-field>
                                    <b-field label="Destinataire">
                                        <b-input 
                                            placeholder="Email" 
                                            v-model="mail.receiver"
                                            type="email" disabled >
                                        </b-input>
                                    </b-field>
                                    <b-field 
                                        label="Objet"
                                        :type="{'is-danger': errors.has('object')}"
                                        :message="[{'Un objet est requis': errors.first('object')}]">
                                        <b-input 
                                            placeholder="Votre annonce blablabla du 22/07/1997 à 18h06 m'intéresse" 
                                            v-model="mail.object"
                                            name="object"
                                            v-validate="'required'"
                                            type="text">
                                        </b-input>
                                    </b-field>
                                    <b-field 
                                        label="Contenu"
                                        :type="{'is-danger': errors.has('content')}"
                                        :message="[{'Un contenu est requis': errors.first('content')}]">
                                        <b-input type="textarea"
                                            minlength="10"
                                            name="content"
                                            maxlength="1000"
                                            v-model="mail.content"
                                            v-validate="'required'"
                                            placeholder="Votre message ici"
                                            required>
                                        </b-input>
                                    </b-field>
                                    <b-button type="is-link" @click.prevent="send" outlined>Envoyer</b-button>
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
                author: '',
                email: ''
            },
            mail: {
                sender: '',
                receiver: '',
                object:'',
                content:'',
            },
            index: null
        }
    },
    computed:{
         user(){
          return this.$store.getters['authentication/user']
        },
    },
    methods:{
        send(){
            this.$validator.validateAll().then((result) => {
                if (result) {
                    var Email = { send: function (a) { return new Promise(function (n, e) { a.nocache = Math.floor(1e6 * Math.random() + 1), a.Action = "Send"; var t = JSON.stringify(a); Email.ajaxPost("https://smtpjs.com/v3/smtpjs.aspx?", t, function (e) { n(e) }) }) }, ajaxPost: function (e, n, t) { var a = Email.createCORSRequest("POST", e); a.setRequestHeader("Content-type", "application/x-www-form-urlencoded"), a.onload = function () { var e = a.responseText; null != t && t(e) }, a.send(n) }, ajax: function (e, n) { var t = Email.createCORSRequest("GET", e); t.onload = function () { var e = t.responseText; null != n && n(e) }, t.send() }, createCORSRequest: function (e, n) { var t = new XMLHttpRequest; return "withCredentials" in t ? t.open(e, n, !0) : "undefined" != typeof XDomainRequest ? (t = new XDomainRequest).open(e, n) : t = null, t } };
                    
                    Email.send({
                        Host: "smtp.gmail.com",
                        Username: "lo54.p2019@gmail.com",
                        Password: 990099009900,
                        To: this.mail.receiver,
                        From: this.mail.sender,
                        Subject: this.mail.object,
                        Body: this.mail.content
                    }).then(message => {
                        //Envoi de l'accusé de réception
                        Email.send({
                            Host: "smtp.gmail.com",
                            Username: "lo54.p2019@gmail.com",
                            Password: 990099009900,
                            To: this.mail.sender,
                            From: this.mail.sender,
                            Subject: this.mail.object,
                            Body: this.mail.content + ' \nEmail envoyé à : '+ this.mail.receiver
                        })
                    })
                }
            })
        }
    },
    created(){
        this.$store.dispatch('authentication/getUser');

        axios.get('/api/manage/post/'+this.id).then(response =>{
            //console.log(response.data[0]);
            //console.log(response.data)
            this.post.title = response.data.title
            this.post.an_type = response.data.an_type.title
            this.post.category = response.data.category.title
            this.post.address.num_street = response.data.num_street
            this.post.address.street = response.data.street
            this.post.address.city = response.data.city
            this.post.address.postalcode = response.data.postalcode
            this.post.price = response.data.price
            this.post.content = response.data.content
            this.post.country = response.data.country
            this.post.author = response.data.author.username
            this.post.email = response.data.author.email

            this.mail.sender = this.user.email
            this.mail.receiver = this.post.email
            this.mail.object = 'Votre annonce '+ this.post.title +' sur Annonces UTBM'
        });

        axios.get('/api/manage/post/date/'+this.id).then(response =>{
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
