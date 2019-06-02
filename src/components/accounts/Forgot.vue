<template>
            <form action="">
                <div class="modal-card" style="width: auto">
                    <header class="modal-card-head">
                        <p class="modal-card-title">Mot de passe oublié</p>
                    </header>
                    <section class="modal-card-body">
                        <b-field label="Email">
                            <b-input
                                type="email"
                                :value="email"
                                placeholder="Votre email"
                                required>
                            </b-input>
                        </b-field>

                        <b-field label="Nom d'utilisateur">
                            <b-input
                                type="text"
                                :value="username"
                                placeholder="Votre nom d'utilisateur"
                                required>
                            </b-input>
                        </b-field>
                    </section>
                    <footer class="modal-card-foot">
                        <button class="button is-primary">Récuperer le mot de passe</button>
                    </footer>
                </div>
            </form>
</template>

<script>
export default {
    data(){
        return {
            username: '',
            email:''
        }
    }
}
</script>