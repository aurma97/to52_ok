<template>
    <div class="container">
         <nav class="breadcrumb has-succeeds-separator" aria-label="breadcrumbs">     
            <div v-if="!isAddType">
                <ul v-if="isShowType">
                    <li><router-link to="/">Accueil</router-link></li>
                    <li @click="isShowType = false"><a>Gestion des types d'équipements</a></li>
                    <li class="is-active"><a href="#" aria-current="page">Modification de {{type.title}}</a></li>
                </ul>
                <ul v-if="!isShowType">
                    <li><router-link to="/">Accueil</router-link></li>
                    <li class="is-active"><a href="#">Gestion des types d'équipements</a></li>
                </ul>
            </div>
            <ul v-if="isAddType">
                <li><router-link to="/">Accueil</router-link></li>
                <li><a href="#">Gestion des types d'équipements</a></li>
                <li class="is-active"><a href="#">Ajout d'un type</a></li>
            </ul>
        </nav>


        <!-- Ajout d'un type -->

        <template v-if="isAddType">
            <section>
                <hr>
                <div class="modal-card" style="width: auto">
                    <div>
                        <section class="modal-card-body">
                            <b-field label="Nom">
                                <b-input
                                    type="text"
                                    v-model="newType.title"
                                    placeholder="Nom du type"
                                    required>
                                </b-input>
                            </b-field>
                        </section>
                        <footer class="modal-card-foot">
                            <button class="button is-primary" @click="addType">Valider</button>
                            <b-button @click="isAddType = false">Annuler</b-button>
                        </footer>
                    </div>
                    <br>
                </div>
                    
            </section>
        </template>

        <!-- Modification d'un équipement -->

        <div class="notification" v-if="type && isShowType" >
            <h1 class="title is-2">Modification de " {{type.title}} " </h1>
            
            <div class="columns">
                <div class="column">
                    <b-field label="Nom du type de l'équipement">
                        <b-input v-model="type.title"></b-input>
                    </b-field>
                    <b-field grouped group-multiline>
                        <b-button type="is-primary" @click="updateType(type)">Modifier</b-button>
                        <b-button @click="isShowType = false">Annuler</b-button>
                    </b-field>
                </div>
            </div>
        </div>

        <!-- Chargement lors de la sauvegarde -->

        <b-loading :is-full-page="isFullPage" :active.sync="isLoading" :can-cancel="true"></b-loading>


        <!-- Affichage du tableau des types d'équipements -->

        <section v-if="!isShowType">
            <hr>

            <div class="columns">
                <div class="column is-2">
                    <b-button
                        v-if="isAddType == false"
                        icon-left="plus" @click="isAddType = true">
                        Ajouter un type
                    </b-button>
                </div>
                <div class="column">
                    <!-- Confirmation suppression -->
                    <div class="has-text-right" v-if="isDelete">
                        <span>
                            <button class="button is-danger" @click="deleteType(idEqToDel)">Confirmation suppression</button>
                        </span>
                        &nbsp;
                        <span>
                            <button class="button" @click="isDelete = false">Annuler</button>
                        </span>
                    </div>
                </div>
            </div>
            
            <hr>
             <b-field label="Filtre par type d'équipement" v-if="isShowType">
                <b-input v-model="search" ></b-input>                               
            </b-field>
            <b-field grouped group-multiline v-if="isAddType == false">
                <b-select v-model="defaultSortDirection">
                    <option value="asc">Tri: Croissant</option>
                    <option value="desc">Tri: Décroissant</option>
                </b-select>
                <b-select v-model="perPage" :disabled="!isPaginated">
                    <option value="5">5 par page</option>
                    <option value="10">10 par page</option>
                    <option value="15">15 par page</option>
                    <option value="20">20 par page</option>
                </b-select>
                <div class="control is-flex">
                    <b-switch v-model="isPaginated">Pagination</b-switch>
                </div>
            </b-field>

            <b-table
                v-if="isAddType == false"
                :data="isEmpty ? [] : filterTypes"
                :paginated="isPaginated"
                :per-page="perPage"
                ref="table"
                :current-page.sync="currentPage"
                :pagination-simple="isPaginationSimple"
                :default-sort-direction="defaultSortDirection"
                default-sort="name"
                aria-next-label="Page suivante"
                aria-previous-label="Page précedente"
                aria-page-label="Page"
                aria-current-label="Page actuelle">

                <template slot-scope="props">
                    <b-table-column field="title" label="Libellé" sortable>
                        {{ props.row.title }}
                    </b-table-column>
                    <b-table-column sortable centered>
                        <b-field grouped group-multiline>
                            <div class="control is-flex">
                                <button class="button is-warning" @click="getType(props.row.id); isShowType = true"><i class="fas fa-edit"></i></button>
                            </div>
                            <div>
                                <button class="button is-danger" @click="callDelete(props.row.id)"><i class="fas fa-trash"></i></button>
                            </div>
                        </b-field>
                    </b-table-column>
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
                            <p>Rien par ici.</p>
                        </div>
                    </section>
                </template>
            </b-table>
        </section>
    </div>
</template>

<script>
export default {
    data() {
        return {
            data:[],
            idEqToDel:'',
            error: false, 
            isPaginated: true,
            isPaginationSimple: false,
            defaultSortDirection: 'asc',
            currentPage: 1,
            perPage: 5,
            defaultOpenedDetails: [1],
            showDetailIcon: true,
            isDelete: false,
            isAddType: false,
            isShowType: false,
            date: new Date(),
            isLoading: false,
            isFullPage: true,
            errors:'',
            newType:{
                title:'',
            }, 
            type:[],
            search:'',
            isEmpty: false,
        }
    },
    computed: {
        // types(){
        //     return this.$store.state.typeEquipment.types
        // },
        filterTypes(){
            if (!this.$store.state.typeEquipment.types){
                this.isEmpty = true
            }
            return this.$store.state.typeEquipment.types.filter((types)=>{
                if(types.title)
                return types.title.match(this.search)
            })
        }
        // type(){
        //     return this.$store.state.typeEquipment.type
        // }
    },
    methods: {
        addType(){
            this.$store.dispatch('typeEquipment/addType', this.newType)
            this.newType = { title:''}
            this.errors = this.$store.dispatch('typeEquipment/getErrors')
    
            if(this.errors == 400 | this.errors == 500){
                this.$notification.open({
                    duration: 500,
                    message: `Un problème est survenu lors de l'ajout, veuillez reessayer`,
                    position: 'is-bottom-right',
                    type: 'is-danger',
                    hasIcon: true
                })
            }
            else{
                this.isLoading = true
                setTimeout(() => {
                    this.$store.dispatch('typeEquipment/getTypes');
                    //location.reload()
                    this.$el.textContent
                    this.isLoading = false
                    this.isShowType = false
                    this.isAddType = false
                    this.$notification.open({
                        duration: 5000,
                        message: `Enregistrement effectué avec succès`,
                        position: 'is-bottom-right',
                        type: 'is-success',
                        hasIcon: true
                    })
                }, 500)   
            }
        },
        getType(payload){
            this.type = this.filterTypes.find(fruit => fruit.id === payload)
        },
        callDelete(id){
            this.idEqToDel = id
            this.isDelete = true
        },
        deleteType(payload){
            this.$store.dispatch('typeEquipment/deleteType', payload)
            this.isDelete = false
            this.errors = this.$store.dispatch('typeEquipment/getErrors')
            //console.log(this.errors)
            if(this.errors != 400 | this.errors !=500){
                setTimeout(() => {
                    this.$store.dispatch('typeEquipment/getTypes');       
                    //location.reload()
                    this.$el.textContent
                    this.isDelete = false
                    this.isLoading = false
                    this.isShowType = false
                    this.isAddType = false
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
        updateType(payload){
            this.$store.dispatch('typeEquipment/updateType', payload)
            this.errors = this.$store.dispatch('typeEquipment/getErrors')
            if(this.errors == 0){
                this.$notification.open({
                    duration: 20000,
                    message: `Un problème est survenu lors de la mise à jour, veuillez reessayer`,
                    position: 'is-bottom-right',
                    type: 'is-danger',
                    hasIcon: true
                })
            }
            else
            {
                //this.isLoading = true
                //setTimeout(() => {
                    this.$store.dispatch('typeEquipment/getTypes');
                    //location.reload()
                    this.$el.textContent
                    this.isLoading = false
                    this.isShowType = false
                    this.$notification.open({
                        duration: 5000,
                        message: `Mise à jour effectuée avec succès`,
                        position: 'is-bottom-right',
                        type: 'is-success',
                        hasIcon: true
                    })
                //}, 500)
            }
        }
        ,
        //Pour la liste déroulante de description
        toggle(row) {
            this.$refs.table.toggleDetails(row)
        }
    },
    created() {
        this.$store.dispatch('typeEquipment/getTypes');
    }
}
</script>
