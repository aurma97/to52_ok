<template>
    <section class="hero is-large is-link is-bold">
        <div class="hero-body">
            <div class="container">
                <p class="title">
                    Inscription
                </p>
                <p class="subtitle">
                    Veuillez remplir le formulaire ci-dessous pour vous connecter
                </p>
                <p class="help is-warning" v-if="error">
                    Connexion impossible, Veuillez vérifier votre login ou mot de passe
                </p>
            </div>
            <br>
            <div class="container">
                <div class="columns">
                    <div class="column">
                        <form>
                            <div class="field">
                               <label class="subtitle is-4">Nom d'utilisateur *</label>
                                <p class="control has-icons-left has-icons-right">
                                    <input class="input is-medium" type="text" v-model="register.username" placeholder="Nom d'utilisateur">
                                    <span class="icon is-small is-left">
                                        <i class="fas fa-user"></i>
                                    </span>
                                    <span class="icon is-small is-right">
                                        <i class="fas fa-check"></i>
                                    </span>
                                </p>
                            </div>

                            <div class="field">
                              <label class="subtitle is-4">Email *</label>
                              <div class="field-label"></div>
                                <div class="field-body">
                                  <div class="field is-expanded" >
                                    <div class="field has-addons">
                                      <p class="control is-expanded">
                                        <input class="input is-medium" type="email" placeholder="Votre adresse email">
                                      </p>
                                      <p class="control">
                                        <a class="button is-static is-medium">
                                          @utbm.fr
                                        </a>
                                      </p>
                                    </div>
                                    <p class="help">Do not enter the first zero</p>
                                  </div>
                                </div>
                              </div>
                            <div class="field">
                               <label class="subtitle is-4">Mot de passe *</label>
                                <p class="control has-icons-left">
                                    <input class="input is-medium" type="password" v-model="register.password" placeholder="Mot de passe">
                                    <span class="icon is-small is-left">
                                        <i class="fas fa-lock"></i>
                                    </span>
                                </p>
                            </div>
                            <div class="field">
                              <label class="subtitle is-4">Confirmation *</label>
                                <p class="control has-icons-left">
                                    <input class="input is-medium" type="password" v-model="register.password" placeholder="Confirmation mot de passe">
                                    <span class="icon is-small is-left">
                                        <i class="fas fa-lock"></i>
                                    </span>
                                </p>
                            </div>
                            
                            <div class="field">
                                <p class="control">
                                    <button class="button is-success is-medium" @click.prevent="">
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
        <b-modal :active.sync="isCardModalActive" :width="640" scroll="keep">
            <forgot></forgot>
        </b-modal>
    </section>
</template>

<script>
import Forgot from './Forgot.vue'

export default {
    components: {
        'forgot': Forgot
    },
    data(){
        return {
           register: {
             username: null,
             pasword: null,
             confirmation: null,
             email: null,
           }
        }
    },
    methods:{
       
    }
}
</script>
