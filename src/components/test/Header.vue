<template>
    <header>
            <div class="container">
                <nav class="navbar is-bold has-shadow" role="navigation" aria-label="main navigation">
                    <div id="vue-app" class="container">
                        <div class="navbar-brand">
                            <router-link to="/">
                                <img src="../../assets/logo-site.png" width="150" height="200" alt="Menu">
                            </router-link>
                            <div @click="active = !active" class="navbar-burger burger" data-target="navMenu">
                                <span aria-hidden="true"></span>
                                <span aria-hidden="true"></span>
                                <span aria-hidden="true"></span>
                            </div>
                        </div>

                        <div id="navMenu" class="navbar-menu" v-bind:class="{'is-active': active}">
                            <div class="navbar-start">
                                <div class="navbar-item">
                                    <h3 class="title is-5 has-text-link">Notre bon coin</h3>    
                                </div>
                            </div>
                            <div class="navbar-end">
                                <router-link class="navbar-item" to="/nouvelle-annonce" exact v-if="connected">
                                    <span class="message is-link"><i class="fas fa-plus-square"></i>&nbsp;&nbsp;Déposer une annonce</span>
                                </router-link>
                                <!-- <router-link class="navbar-item" to="/mes-favoris" exact v-if="connected">
                                    <i class="fas fa-heart"></i>&nbsp;&nbsp;Mes favoris
                                </router-link>
                                <router-link class="navbar-item" to="/mes-messages" exact v-if="connected">
                                    <i class="fas fa-inbox"></i>&nbsp;&nbsp;Messages
                                </router-link> -->
                                <router-link class="navbar-item" to="/mes-annonces" exact v-if="connected">
                                    <i class="fas fa-info"></i>&nbsp;&nbsp;Mes annonces
                                </router-link>            
                                
                                <router-link class="navbar-item" to="/connexion" exact v-if="!connected">
                                    <i class="fas fa-sign-in-alt"></i>&nbsp;&nbsp;Connexion
                                </router-link>
                                <router-link class="navbar-item" to="/inscription" exact v-if="!connected">
                                    <i class="fas fa-file-alt"></i>&nbsp;&nbsp;Inscription
                                </router-link>
                                <div class="navbar-item has-dropdown is-hoverable" v-if="connected">
                                    <a class="navbar-link">
                                        Bonjour {{user.username}}
                                    </a>
                                    <div class="navbar-dropdown">
                                        <router-link class="navbar-item" to="/mon-compte" exact>
                                            <i class="fas fa-user-circle"></i>&nbsp;&nbsp;Mon compte
                                        </router-link>
                                        <router-link class="navbar-item" to="/aide" exact>
                                            <i class="fas fa-question"></i>&nbsp;&nbsp;Aide
                                        </router-link>
                                        <div class="navbar-divider"></div>
                                        <span class="navbar-item">
                                            <a class="button is-link is-inverted" @click="logout" exact>
                                                <span class="icon">
                                                <i class="fas fa-sign-out-alt "></i>
                                                </span>
                                                <span>Déconnexion</span>
                                            </a>
                                        </span>
                                    </div>
                                </div>
                            </div>     
                        </div>
                    </div>
                </nav>
            </div>
    </header>
</template>

<script>
export default {
    data(){
        return{
            active: false
        }
    },
    computed : {
        connected (){ 
          return this.$store.getters['authentication/isLoggedIn']
        },
        user(){
          return this.$store.getters['authentication/user']
        }
    },
    methods: {
        logout: function () {
            this.$store.dispatch('authentication/logout')
            this.$router.replace('/connexion')
        },
        show(){
            console.log(this.user);
        }
    }
}
</script>
