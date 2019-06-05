<template>
    <section class="hero is-large is-bold">
        <div class="hero-body">
            <div class="container">
                <p class="title">
                    Inscription
                </p>
                <p class="subtitle">
                    Veuillez remplir le formulaire ci-dessous pour vous connecter
                </p>
                <p class="subtitle is-5  has-text-danger" v-if="error.length != 0">
                    Problème de connexion avec le serveur                
                </p>
            </div>
            <br>
            <div class="container">
                <div class="columns">
                    <div class="column">
                        <form>
                            <b-field label="Nom d'utilisateur *"
                                :type="{'is-danger': errors.has('username')}"
                                :message="[{'Votre nom d\'utilisateur n\'est pas conforme': errors.first('username')}]">
                                <b-input 
                                    v-model="username" 
                                    name="username" 
                                    v-validate="'required'" />
                            </b-field>
                            <p class="subtitle is-6 has-text-danger" v-if="error.username">
                                {{error.username[0]}}
                            </p>

                            <label><strong>Email *</strong></label>
                            <b-field
                                :type="{'is-danger': errors.has('email')}"
                                :message="[{
                                    'Votre email n\'est pas conforme' : errors.first('email')
                                }]">
                                <br>
                                <b-input 
                                    type = "text"
                                    name = "email"
                                    v-model="email"
                                    v-validate="'required'"
                                    expanded>
                                </b-input>
                                 <p class="control">
                                    <span class="button is-static">@utbm.fr</span>
                                </p>
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
                            
                            <div class="field">
                                <p class="control">
                                    <button class="button is-success is-medium" @click.prevent="register_now">
                                        Inscription
                                    </button>
                                </p>
                            </div>
                        </form>
                    </div>
                    <div class="column">

                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import Forgot from './Forgot.vue'
import axios from 'axios'

export default {
    components: {
        'forgot': Forgot
    },
    data(){
        return {
            username: null,
            password: null,
            confirmation: null,
            email: null,
            error: [],
            emailEnd: "@utbm.fr"
        }
    },
    methods:{
       register_now(){
            this.$validator.validateAll().then((result) => {
                if (result) {
                    this.$toast.open({
                        message: 'Le formulaire est valide!',
                        type: 'is-success',
                        position: 'is-bottom'
                    })
                    //console.log(this.username+this.password+this.email)

                    var username = this.username
                    var password = this.password
                    var email = this.email+this.emailEnd
                    axios.post('/api/manage/account/register', {username, email, password})
                    .then(response =>{
                        if (response.status == 201){
                            this.$store.dispatch('authentication/registerSuccess', username)
                            this.$router.push('/connexion')
                        }
                    })
                    .catch(error => {
                        this.error = error.response.data
                    })
                    

                    return;
                }
                this.$toast.open({
                    message: 'Form is not valid! Please check the fields.',
                    type: 'is-danger',
                    position: 'is-bottom'
                })
            });
       }
    }
}
</script>
