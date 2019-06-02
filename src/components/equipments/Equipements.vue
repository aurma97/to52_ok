<template>
    <div class="container" @mouseenter="refresh">
        <hr>
        <hr>
        <b-tabs position="is-centered" class="block">
            <!-- Gestion des équipements -->
            <b-tab-item label="Les équipements">
                <!-- Breadcrumb -->
                <nav class="breadcrumb has-succeeds-separator" aria-label="breadcrumbs">     
                    <div class="level">
                        <div class="level-left">
                            <div v-if="!isComponentModalActive">
                                <ul v-if="showEquipment">
                                    <li><router-link to="/">Accueil</router-link></li>
                                    <li @click="showEquipment = false"><a>Gestion des équipements</a></li>
                                    <li class="is-active"><a href="#" aria-current="page">Modification de {{equipment.name}}</a></li>
                                </ul>
                                <ul v-if="!showEquipment">
                                    <li><router-link to="/">Accueil</router-link></li>
                                    <li class="is-active"><a href="#">Gestion des équipements</a></li>
                                </ul>
                            </div>
                            <ul v-if="isComponentModalActive">
                                <li><router-link to="/">Accueil</router-link></li>
                                <li><a href="#">Gestion des équipements</a></li>
                                <li class="is-active"><a href="#">Ajout d'un équipement</a></li>
                            </ul>
                        </div> 
                        <div class="level-right">
                            <button class="button is-link" @click="refresh">Actualiser</button>
                        </div>
                    </div>
                </nav>

                <!-- Ajout d'un équipement -->

                <template v-if="isComponentModalActive">
                    <section>
                        <hr>
                        <div class="modal-card" style="width: auto">
                            <div>
                                <section class="modal-card-body">
                                    <b-field label="Nom">
                                        <b-input
                                            type="text"
                                            v-model="equipment.name"
                                            placeholder="Nom de l'équipement"
                                            required>
                                        </b-input>
                                    </b-field>
                                    <div class="field">
                                        <label class="label">Date d'acquisition</label>
                                        <div class="control has-icons-right">
                                            <input class="input" type="date" v-model="equipment.date_purchase">
                                            <span class="icon is-small is-right">
                                            <i class="fas fa-calendar"></i>
                                            </span>
                                        </div>
                                    </div>
                                    <div class="field">
                                        <label class="label">Dernière maintenance</label>
                                        <div class="control has-icons-right">
                                            <input class="input" type="date" v-model="equipment.last_check">
                                            <span class="icon is-small is-right">
                                            <i class="fas fa-calendar"></i>
                                            </span>
                                        </div>
                                    </div>
                                    <b-field label="Description">
                                        <b-input
                                            type="textarea"
                                            v-model="equipment.description"
                                            placeholder="Détails sur l'équipement"
                                            required>
                                        </b-input>
                                    </b-field>
                                    <b-field label="Conditions d'utilisation">
                                        <b-input
                                            type="textarea"
                                            v-model="equipment.use_cond"                        
                                            required>
                                        </b-input>
                                    </b-field>
                                    <b-field label="Type d'équipement" type="is-fullwidth">
                                        <b-select placeholder="Select a character" v-model="equipment.type_id">
                                            <option v-for="type in types" :value="type.id">{{type.title}}</option>
                                        </b-select>
                                    </b-field>
                                    <b-field label="Localisation" type="is-fullwidth">
                                        <b-select :placeholder="equipment.location.name" v-model="equipment.location">
                                            <option v-for="location in locations" :value="location.id">{{location.name}}</option>
                                        </b-select>
                                    </b-field>
                                    
                                </section>
                                <footer class="modal-card-foot">
                                    <button class="button is-primary" @click="addEquipment">Valider</button>
                                    <b-button @click="isComponentModalActive = false">Annuler</b-button>
                                </footer>
                            </div>
                            <br>
                        </div>
                            
                    </section>
                </template>

                <!-- Modification d'un équipement -->

                <div class="notification" v-if="equipment && showEquipment" >
                    <h1 class="title is-2">Modification de " {{equipment.name}} " </h1>
                    
                    <div class="columns">
                        <div class="column">
                            <b-field label="Nom de l'équipement">
                                <b-input v-model="equipment.name"></b-input>
                            </b-field>
                            <b-field label="Description">
                                <b-input maxlength="200" v-model="equipment.description" type="textarea"></b-input>
                            </b-field>
                            <b-field label="Conditions d'utilisation">
                                <b-input maxlength="100" v-model="equipment.use_cond" type="textarea"></b-input>
                            </b-field>
                        </div>
                        <div class="column">
                            <b-field label="Type d'équipement" type="is-fullwidth">
                                <b-select v-model="equipment.type_id">
                                    <option :value="equipmentOne.type_id.id" selected>
                                        {{equipmentOne.type_id.title}}
                                    </option>
                                    <option v-for="type in types" v-if="type.title != equipmentOne.type_id.title" :value="type.id">{{type.title}}</option>
                                </b-select>
                            </b-field>
                            <b-field label="Localisation" type="is-fullwidth">
                                <b-select :placeholder="equipment.location.name" v-model="equipment.location">
                                    <option :value="equipmentOne.location.id" selected>
                                        {{equipmentOne.location.name}}
                                    </option>
                                    <option v-for="location in locations" v-if="location.name != equipmentOne.location.name" :value="location.id">{{location.name}}</option>
                                </b-select>
                            </b-field>
                            <div class="field">
                                <label class="label">Date d'acquisition</label>
                                <div class="control has-icons-right">
                                    <input class="input" type="date" v-model="equipment.date_purchase">
                                    <span class="icon is-small is-right">
                                    <i class="fas fa-calendar"></i>
                                    </span>
                                </div>
                            </div>
                            <div class="field">
                                <label class="label">Dernière maintenance</label>
                                <div class="control has-icons-right">
                                    <input class="input" type="date" v-model="equipment.last_check">
                                    <span class="icon is-small is-right">
                                    <i class="fas fa-calendar"></i>
                                    </span>
                                </div>
                            </div>
                            <b-field grouped group-multiline>
                                <b-button type="is-primary" @click="updateEquipment(equipment)">Modifier</b-button>
                                <b-button @click="showEquipment = false">Annuler</b-button>
                            </b-field>
                        </div>
                    </div>
                </div>

                <!-- Chargement lors de la sauvegarde -->

                <b-loading :is-full-page="isFullPage" :active.sync="isLoading" :can-cancel="true"></b-loading>
                
                <!-- Affichage du tableau des équipements -->
                <section v-if="!showEquipment">
                    <hr>

                    <article class="message is-warning" v-if="types.length == 0 || locations.length == 0">
                        <div class="message-body has-text-centered">
                            Veuillez ajouter un <strong>Type d'équipement</strong> et une <strong>localisation</strong> pour pouvoir rajouter un équipement <hr>
                        </div>
                    </article>
                  
                    <div class="columns">
                        <div class="column is-2" v-if="types.length != 0 & locations.length != 0">
                            <b-button
                                v-if="isComponentModalActive == false"
                                icon-left="plus" @click="isComponentModalActive = true">
                                Ajouter un équipement
                            </b-button>
                            
                        </div>
                        <div class="column">
                            <!-- Confirmation suppression -->
                            <div class="has-text-right" v-if="isDelete">
                                <span>
                                    <button class="button is-danger" @click="deleteEquipment(idEqToDel)">Confirmation suppression</button>
                                </span>
                                &nbsp;
                                <span>
                                    <button class="button" @click="isDelete = false">Annuler</button>
                                </span>
                            </div>
                        </div>
                    </div>
                    
                    <hr>
                    <b-field label="Filtre par nom d'équipement" v-if="isComponentModalActive == false">
                        <b-input v-model="search"></b-input>                               
                    </b-field>
                    <b-field grouped group-multiline v-if="isComponentModalActive == false">
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
                        <div class="control">
                            <b-switch v-model="showDetailIcon">Détail des équipements</b-switch>
                        </div>
                    </b-field>

                    <b-table
                        v-if="isComponentModalActive == false"
                        :data="isEmpty ? [] : filterEquipments"
                        :paginated="isPaginated"
                        :per-page="perPage"
                        :opened-detailed="defaultOpenedDetails"
                        ref="table"
                        detailed
                        detail-key="id"
                        @details-open="(row, index) => $toast.open(`Expanded ${row.name}`)"
                        :show-detail-icon="showDetailIcon"
                        :current-page.sync="currentPage"
                        :pagination-simple="isPaginationSimple"
                        :default-sort-direction="defaultSortDirection"
                        default-sort="name"
                        aria-next-label="Page suivante"
                        aria-previous-label="Page précedente"
                        aria-page-label="Page"
                        aria-current-label="Page actuelle">

                        <template slot-scope="props">
                            <b-table-column field="name" label="Libellé" sortable>
                                <template v-if="showDetailIcon">
                                    {{ props.row.name }}
                                </template>
                                <template v-else>
                                    <a @click="toggle(props.row)">
                                        {{ props.row.name }}
                                    </a>
                                </template>
                            </b-table-column>

                            <b-table-column field="type_id.title" label="Type" sortable>
                                {{ props.row.type_id.title }}
                            </b-table-column>

                            <b-table-column field="location.name" label="Position" sortable>
                                {{ props.row.location.name }}
                            </b-table-column>

                            <b-table-column field="date_purchase" label="Date achat" sortable centered>
                                <span class="tag is-success">
                                    {{ new Date(props.row.date_purchase).toLocaleDateString() }}
                                </span>
                            </b-table-column>

                            <b-table-column field="last_check" label="Dernière maintenance" sortable centered>
                                <span class="tag is-warning">
                                    {{ new Date(props.row.last_check).toLocaleDateString() }}
                                </span>
                            </b-table-column>

                            <b-table-column sortable centered>
                                <b-field grouped group-multiline>
                                    <div class="control is-flex">
                                        <button class="button is-warning" @click="getEquipment(props.row.id); showEquipment = true"><i class="fas fa-edit"></i></button>
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
                                            <strong>{{ props.row.name }} - {{ props.row.type_id.title }}</strong>
                                            <br>
                                            {{props.row.description}}
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
                                    <p>Rien par ici.</p>
                                </div>
                            </section>
                        </template>
                    </b-table>
                    
                </section>
            </b-tab-item>
            <!-- Gestion des types d'équipements -->
            <b-tab-item label="Gestion des types d'équipements" >
                <type-equipment></type-equipment>
            </b-tab-item>
            <!-- Gestion des localisations -->
            <b-tab-item label="Gestion des localisations">
                <location></location>
            </b-tab-item>
        </b-tabs>
    </div>
</template>

<script>
import typeEquipment from './typeEquipment.vue'
import Location from './Location.vue'

export default {
    components:{
        'type-equipment': typeEquipment,
        'location': Location
    },
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
            isComponentModalActive: false,
            showEquipment: false,
            date: new Date(),
            equipment:{
                id: '',
                name: '',
                date_purchase: '',
                description: '',
                use_cond: '',
                last_check: '',
                type_id: '',
                location: ''
            },
            equipementOne:[],
            isLoading: false,
            isFullPage: true,
            errors:'',
            search:'',
            isEmpty: false,
        }
    },
    computed:{
        filterEquipments(){
            if (!this.equipments){
                this.isEmpty = true
            }
            return this.equipments.filter((equipment)=>{
                if(equipment.name){
                    return equipment.name.match(this.search)
                }
            })
        }, 
        equipments(){
            return this.$store.state.equipments.equipments
        },
        // equipmentOne(){
        //     return this.$store.state.equipments.equipment
        // },
        types(){
            return this.$store.state.equipments.types
        },
        locations(){
            return this.$store.state.equipments.locations
        }
    },
    methods: {
        refresh(){
            this.$store.dispatch('equipments/getEquipments');
            this.$store.dispatch('equipments/getTypes');
            this.$store.dispatch('equipments/getLocations');
        },

        addEquipment(){
            this.$store.dispatch('equipments/addEquipment', this.equipment)
            this.errors = this.$store.dispatch('equipments/getErrors')
            // var error = this.errors.then( body => console.log( JSON.parse( body ) ) )
            // console.log(error)
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
                this.equipment = []
                setTimeout(() => {
                    this.$store.dispatch('equipments/getEquipments');
                    //location.reload()
                    this.$el.textContent
                    this.isLoading = false
                    this.showEquipment = false
                    this.isComponentModalActive = false
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
        getEquipment(payload){
            //this.$store.dispatch('equipments/getEquipment', payload)

            this.equipmentOne = this.filterEquipments.find(fruit => fruit.id === payload)

            //console.log(this.equipmentOne)

            this.equipment.id = this.equipmentOne.id
            this.equipment.name = this.equipmentOne.name
            this.equipment.date_purchase = this.equipmentOne.date_purchase
            this.equipment.description = this.equipmentOne.description
            this.equipment.use_cond = this.equipmentOne.use_cond
            this.equipment.last_check = this.equipmentOne.last_check
            this.equipment.type_id = this.equipmentOne.type_id.id
            this.equipment.location = this.equipmentOne.location.id
        },
        callDelete(id){
            this.idEqToDel = id
            this.isDelete = true
        },
        deleteEquipment(payload){
            this.$store.dispatch('equipments/deleteEquipment', payload)
            this.isDelete = false
            this.errors = this.$store.dispatch('equipments/getErrors')
            //console.log(this.errors)
            if(this.errors != 400 | this.erros != 500){
                setTimeout(() => {
                    this.$store.dispatch('equipments/getEquipments');
                    //location.reload()
                    this.$el.textContent
                    this.isDelete = false
                    this.isLoading = false
                    this.showEquipment = false
                    this.isComponentModalActive = false
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
        updateEquipment(payload){
            //console.log(payload)
            this.$store.dispatch('equipments/updateEquipment', payload)
            this.errors = this.$store.dispatch('equipments/getErrors')
            if(this.errors == 400 | this.errors == 500){
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
                this.isLoading = true
                setTimeout(() => {
                    this.$store.dispatch('equipments/getEquipments');
                    //location.reload()
                    this.$el.textContent
                    this.isLoading = false
                    this.showEquipment = false
                    this.$notification.open({
                        duration: 5000,
                        message: `Mise à jour effectuée avec succès`,
                        position: 'is-bottom-right',
                        type: 'is-success',
                        hasIcon: true
                    })
                }, 500)
            }
        }
        ,
        //Pour la liste déroulante de description
        toggle(row) {
            this.$refs.table.toggleDetails(row)
        },
    },
    created() {
        this.$store.dispatch('equipments/getEquipments');
        this.$store.dispatch('equipments/getTypes');
        this.$store.dispatch('equipments/getLocations');
    }
}
</script>