<template>
    <section class="container">
        <hr>
        <hr>
        <nav class="breadcrumb has-succeeds-separator" aria-label="breadcrumbs">     
            <div>
                <ul v-if="isEditAccount">
                    <li><router-link to="/">Accueil</router-link></li>
                    <li @click="isEditAccount = false"><a>Gestion de mon compte</a></li>
                    <li class="is-active"><a href="#" aria-current="page">Modification de mon compte</a></li>
                </ul>
                <ul v-if="!isEditAccount">
                    <li><router-link to="/">Accueil</router-link></li>
                    <li class="is-active"><a href="#">Gestion de mon compte</a></li>
                </ul>
            </div>
        </nav>

        <!-- Affichage des informations sur le compte -->
        <p class="subtitle is-5  has-text-danger" v-if="error.length != 0">
            Problème de connexion avec le serveur                
        </p>

        <section v-if="!isEditAccount">
            <span class="title is-5" v-if="user.last_name"><strong>Nom(s) :</strong> {{user.last_name}}</span>
            <hr>
            <span class="title is-5" v-if="user.first_name"><strong>Prénom(s) :</strong> {{user.first_name}}</span>
            <hr>
            <span class="title is-5"><strong>Nom d'utilisateur : </strong>{{user.username}}</span>
            <hr>
            <button class="button is-link" @click="isEditAccount = true">Modifier</button>
        </section>
        <section class="notification" v-if="isEditAccount">
            <form>
                <b-field label="Nom d'utilisateur *"
                    :type="{'is-danger': errors.has('username')}"
                    :message="[{'Votre nom d\'utilisateur n\'est pas conforme': errors.first('username')}]">
                    <b-input 
                        v-model="username" 
                        name="username" 
                        v-validate="'required'" disabled />
                </b-field>
                <p class="subtitle is-6 has-text-danger" v-if="error.username">
                    {{error.username[0]}}
                </p>

                <b-field label="Nom(s) *"
                    :type="{'is-danger': errors.has('last_name')}"
                    :message="[{'Votre nom n\'est pas conforme': errors.first('last_name')}]">
                    <b-input 
                        v-model="last_name" 
                        name="last_name" 
                        v-validate="'required'" />
                </b-field>

                <b-field label="Prénom(s) *"
                    :type="{'is-danger': errors.has('first_name')}"
                    :message="[{'Votre prénom n\'est pas conforme': errors.first('first_name')}]">
                    <b-input 
                        v-model="first_name" 
                        name="first_name" 
                        v-validate="'required'" />
                </b-field>

                <label><strong>Email *</strong></label>
                <b-field
                    :type="{'is-danger': errors.has('email')}"
                    :message="[{
                        'Votre email n\'est pas conforme' : errors.first('email')
                    }]">
                    <br>
                    <b-input 
                        type = "email"
                        name = "email"
                        v-model="email"
                        v-validate="'required'"
                        expanded>
                    </b-input>
                </b-field>
                <p class="subtitle is-6 has-text-danger" v-if="error.email">
                    {{error.email[0]}}
                </p>

                <b-field label="Mot de passe"
                    :type="{'is-danger': errors.has('password')}"
                    :message="[{'Le mot de passe doit avoir au moins 8 caractères': errors.first('password')}]">
                    <b-input 
                        type="password" 
                        v-model="password" 
                        name="password" 
                        v-validate="'required|min:8'"
                        password-reveal>
                    </b-input>
                </b-field>
                <p class="subtitle is-6 has-text-danger" v-if="error.password">
                    {{error.password[0]}}
                </p>

                <b-field label="Confirmation mot de passe *"
                    :type="{'is-danger': errors.has('confirmation-password')}"
                    :message="[{
                        'La confirmation du mot de passe est requise' : errors.first('confirmation-password', 'required'),
                        'Les mots de passe ne correspondent pas' : errors.firstByRule('confirmation-password', 'is')
                    }]">
                    <b-input 
                        type="password" 
                        v-model="confirmation" 
                        name="confirmation-password"
                        v-validate="{ required: true, is: password }" />
                </b-field>
                
                 <footer class="modal-card-foot">
                    <b-button @click="isEditAccount = false">Annuler</b-button>
                    <button class="button is-primary" @click.prevent="updateAccount">Valider</button>
                </footer>
            </form>
        </section>
        
    </section>
</template>

<script>
/* eslint-disable */ 
import axios from 'axios'

export default {
    data(){
        return{
            isEditAccount: false,
            id: null,
            username: null,
            password: null,
            first_name: null,
            last_name: null,
            is_staff: true,
            confirmation: null,
            email: null,
            error: [],
        }
    },
    computed: {
        user(){
            var user = this.$store.state.authentication.user
            this.id = user.id
            this.username = user.username
            this.first_name = user.first_name
            this.last_name = user.last_name
            this.email = user.email
            this.is_staff = user.is_staff
            return user
        }
    },
    methods: {
        updateAccount(){
            this.$validator.validateAll().then((result) => {
                if (result) {
                    this.$toast.open({
                        message: 'Le formulaire est valide!',
                        type: 'is-success',
                        position: 'is-bottom'
                    })
                    //console.log(this.username+this.password+this.email)

                    var id = this.id
                    var username = this.username
                    var password = this.password
                    var first_name = this.first_name
                    var last_name = this.last_name
                    var is_staff = this.is_staff
                    var email = this.email
                    axios.put(`/api/manage/account/update/${id}`, {username, email, password, first_name, last_name, is_staff})
                    .then(response =>{
                        if (response.status){
                            this.isEditAccount = false
                            console.log(response.status)
                            setTimeout(() => {
                                this.$store.dispatch('authentication/getUser');
                                this.isEditAccount = false
                                this.$notification.open({
                                    duration: 5000,
                                    message: `Modification effectuée avec succès`,
                                    position: 'is-bottom-right',
                                    type: 'is-success',
                                    hasIcon: true
                                })
                            }, 500)
                            
                        }
                    })
                    .catch(error => {
                        this.error = error.response.data
                        this.$notification.open({
                            duration: 5000,
                            message: `Un problème est survenu avec le serveur`,
                            position: 'is-bottom-right',
                            type: 'is-danger',
                            hasIcon: true
                        })
                    })

                    return;
                }
                this.$toast.open({
                    message: 'Formulaire non valide',
                    type: 'is-danger',
                    position: 'is-bottom'
                })
            });
        }
    },
    created(){
        this.$store.dispatch('authentication/getUser')
    },
    updated(){
        this.$store.dispatch('authentication/getUser')
    }
}
</script>

