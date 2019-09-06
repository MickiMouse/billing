<template>
    <v-content color="primary">
        <v-container fluid id="main-container" grid-list-md fill-height>
            <v-snackbar
                    v-model="snackbar"
                    :timeout="timeout"
                    top
            >
                {{ text }}
                <v-btn
                        flat
                        @click="snackbar = false"
                >
                    Close
                </v-btn>
            </v-snackbar>
            <v-layout
                    justify-center
                    wrap
            >
                <v-flex sm8 xs12>
                    <v-card
                            class="mx-auto"
                            :loading="loading"
                    >
                        <v-list two-line subheader dense>
                            <v-subheader>Details
                                <v-dialog v-model="deletePackageDialog" persistent max-width="290">
                                    <template v-slot:activator="{ on }">
                                        <v-btn color="error" v-on="on" small icon ripple class="ml-auto mr-0">
                                            <v-icon small>delete</v-icon>
                                        </v-btn>
                                    </template>
                                    <v-card>
                                        <v-card-title class="headline">Lorem ipsum dolor sit.</v-card-title>
                                        <v-card-text>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eius maiores odit quo sunt tenetur vitae?</v-card-text>
                                        <v-card-actions>
                                            <v-spacer></v-spacer>
                                            <v-btn small color="error" @click="deletePackageDialog = false">Close</v-btn>
                                            <v-btn outline small color="error" @click="deletePackage">Delete</v-btn>
                                        </v-card-actions>
                                    </v-card>
                                </v-dialog>
                                <!--<v-btn color="error" @click="deleteSubscriber" small icon ripple class="ml-auto mr-0">-->
                                <!--<v-icon small>delete</v-icon>-->
                                <!--</v-btn>-->
                            </v-subheader>
                            <v-list-tile
                                    avatar
                                    @click=""
                            >
                                <v-list-tile-avatar>
                                    <v-icon class="grey lighten-1 white--text">archive</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>Header</v-list-tile-title>
                                    <v-list-tile-sub-title>{{details.header}}
                                    </v-list-tile-sub-title>
                                </v-list-tile-content>
                            </v-list-tile>
                            <v-list-tile
                                    avatar
                                    @click=""
                            >
                                <v-list-tile-avatar>
                                    <v-icon class="grey lighten-1 white--text">account_balance_wallet</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>Tariff</v-list-tile-title>
                                    <v-list-tile-sub-title>{{details.tariff + $store.getters.currency}}</v-list-tile-sub-title>
                                </v-list-tile-content>
                                <v-list-tile-action>
                                    <v-dialog v-model="dialog" persistent max-width="600px">
                                        <template v-slot:activator="{ on }">
                                            <v-btn icon ripple v-on="on">
                                                <v-icon color="grey lighten-1">edit</v-icon>
                                            </v-btn>
                                        </template>
                                        <v-card>
                                            <v-card-text>
                                                <v-container grid-list-md>
                                                    <v-layout wrap>

                                                        <v-flex xs12>
                                                            <v-form
                                                                    ref="tariffForm">
                                                                <v-text-field
                                                                        label="Tariff"
                                                                        type="number" required
                                                                        :rules="[rules.counterTariff, rules.number]"
                                                                        v-model="newBalance"></v-text-field>
                                                            </v-form>
                                                        </v-flex>

                                                    </v-layout>
                                                </v-container>
                                            </v-card-text>
                                            <v-card-actions>
                                                <v-spacer></v-spacer>
                                                <v-btn color="primary" text @click="dialog = false">Close</v-btn>
                                                <v-btn color="primary" text @click="changeBalance">Save</v-btn>
                                            </v-card-actions>
                                        </v-card>
                                    </v-dialog>
                                </v-list-tile-action>
                            </v-list-tile>

                            <v-list-tile
                                    avatar
                                    @click=""
                            >
                                <v-list-tile-avatar>
                                    <v-icon class="grey lighten-1 white--text">tv_off</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>Age limit</v-list-tile-title>
                                    <v-list-tile-sub-title>{{details.age_limit}}</v-list-tile-sub-title>
                                </v-list-tile-content>
                            </v-list-tile>
                            <v-list-tile
                                    avatar
                                    @click=""
                                    v-if="details.cards"
                            >
                                <v-list-tile-avatar>
                                    <v-icon class="grey lighten-1 white--text">card_membership</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>Total cards</v-list-tile-title>
                                    <v-list-tile-sub-title>{{details.cards.length}}</v-list-tile-sub-title>
                                </v-list-tile-content>
                            </v-list-tile>
                        </v-list>
                    </v-card>
                </v-flex>

                <v-flex sm4 xs12>
                    <v-card class="mb-3">
                        <v-card-title>
                            <v-text-field
                                    v-model="search"
                                    append-icon="search"
                                    label="Search"
                                    single-line
                                    hide-details
                            ></v-text-field>
                        </v-card-title>
                    </v-card>
                    <v-card class="my-3">
                        <v-subheader>Bouquets</v-subheader>
                        <v-data-table
                                :headers="headers"
                                :items="bouquets"
                                items-per-page="5"
                                class="elevation-1"
                                :loading="loadingbouquets"
                                :search="search"
                        >
                            <template slot="items" slot-scope="props">
                                <td class="text-xs-left no-wrap">{{ props.item.name }}</td>
                                <td class="text-xs-left no-wrap">{{ props.item.age_limit  }}</td>
                                <td class="text-xs-left no-wrap">
                                    <!--<v-tooltip bottom>-->
                                        <!--<template v-slot:activator="{ on }">-->
                                            <!--<v-btn v-on="on" :to="`/subscribers/${props.item.pk}/details/`" color="info"-->
                                                   <!--ripple icon small dark>-->
                                                <!--<v-icon small>info</v-icon>-->
                                            <!--</v-btn>-->
                                        <!--</template>-->
                                        <!--<span>Detail</span>-->
                                    <!--</v-tooltip>-->
                                    <v-tooltip bottom v-if="$session.get('isSuperuser')">
                                        <template v-slot:activator="{ on }">
                                            <v-btn v-on="on" color="error" @click="removeBouquet(props.item.number)" ripple
                                                   icon small dark>
                                                <v-icon small>close</v-icon>
                                            </v-btn>
                                        </template>
                                        <span>Remove</span>
                                    </v-tooltip>
                                    <h5 v-else>-</h5>
                                </td>
                            </template>
                        </v-data-table>
                    </v-card>
                   <v-card class="my-3">



                       <v-data-table
                               :headers="headers"
                               :items="availableBouquets"
                               items-per-page="5"
                               class="elevation-1"
                               :loading="loadingAvailableBouquets"
                               :search="search"
                               v-if="$session.get('isSuperuser')"
                       >
                           <template slot="items" slot-scope="props">
                               <td class="text-xs-left no-wrap">{{ props.item.name }}</td>
                               <td class="text-xs-left no-wrap">{{ props.item.age_limit  }}</td>
                               <td class="text-xs-left no-wrap">
                                   <v-tooltip bottom>
                                       <template v-slot:activator="{ on }">
                                           <v-btn v-on="on" @click="addBouquet(props.item.number)" color="success" ripple icon small
                                                  dark>
                                               <v-icon small>add</v-icon>
                                           </v-btn>
                                       </template>
                                       <span>Add</span>
                                   </v-tooltip>
                               </td>
                           </template>
                       </v-data-table>
                   </v-card>
                </v-flex>
            </v-layout>
        </v-container>
    </v-content>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "bouquetsDetails",
        data() {
            return {
                snack: false,
                snackColor: '',
                snackText: '',
                loading: true,
                loadingbouquets: true,
                loadingAvailableBouquets: true,
                snackbar: false,
                dialog: false,
                search: '',
                text: 'Oops... Something went wrong',
                timeout: 5000,
                details: {},
                deletePackageDialog: false,
                newBalance:'',
                headers: [
                    {
                        text: 'Header',
                        align: 'left',
                        //  sortable: false,
                        value: 'name',
                    },
                    {
                        text: 'Age limit',
                        align: 'left',
                        //  sortable: false,
                        value: 'age_limit',
                    },
                    {text: 'Action', value: 'action', sortable: false},
                    // {text: 'Calories', value: 'calories'},
                ],
                bouquets: [],
                availableBouquets: [],
                rules: {
                    counter: value => value <= 128 || 'Max 128',
                    counterTariff: value => value <= 2147483647 || 'Max 2147483647',
                    number: value => {
                        const pattern = /^\d+$/;
                        return pattern.test(value) || 'Invalid number.'
                    },
                },
            }
        },
        computed: {},
        methods: {
            getData() {
                this.loadingbouquets = true;
                axios.get(`${this.$hostname}/api/packages/${this.$route.params.id}/`)
                    .then((response) => {
                        if (response.status === 200) {
                            console.log(response.data)
                            this.details = response.data;
                            this.bouquets = this.details.bouquets;
                            this.newBalance = this.details.tariff;
                            this.loadingbouquets = false;
                            console.log(response.data, this.bouquets)
                        }
                    }).catch((error) => {
                    this.text = "Connection error";
                    console.log(error)
                    this.snackbar = true;
                });
                this.loadingAvailableBouquets = true;
                axios.get(`${this.$hostname}/api/bouquets/${this.$route.params.id}/`)
                    .then((response) => {
                        if (response.status === 200) {
                            this.availableBouquets = response.data;
                            this.loadingAvailableBouquets = false;
                            console.log(response.data)
                        }
                    }).catch((error) => {
                    this.text = "Connection error";
                    console.log(error)
                    this.snackbar = true;
                });
            },
            addBouquet(pk) {
                axios.put(`${this.$hostname}/api/packages/edit/bouquets/${this.$route.params.id}/`, {bouquet: pk})
                    .then((response) => {
                        if (response.status === 200) {
                            console.log(response.data);
                            this.getData();
                        }
                    }).catch((error) => {
                    this.text = "Connection error";
                    console.log(error)
                    this.snackbar = true;
                });
            },
            removeBouquet(pk) {
                axios.put(`${this.$hostname}/api/packages/delete/bouquets/${this.$route.params.id}/`, {bouquet: pk})
                    .then((response) => {
                        if (response.status === 200) {
                            console.log(response.data);
                            this.getData();
                        }
                    }).catch((error) => {
                    this.text = "Connection error";
                    console.log(error)
                    this.snackbar = true;
                });
            },
            deletePackage() {
                axios.delete(`${this.$hostname}/api/packages/delete/${this.$route.params.id}/`)
                    .then((response) => {
                        if (response.status === 204) {
                            console.log(response.data);
                            this.$router.push('/packages')
                        }
                    }).catch((error) => {
                    this.text = "Connection error";
                    console.log(error)
                    this.snackbar = true;
                });
            },
            changeBalance() {
                if (!this.$refs.tariffForm.validate()) {
                    this.text = "Fill the form correctly";
                    this.snackbar = true;
                } else {
                    this.loading = true;
                    const putBody = {
                        tariff: this.newBalance
                    };
                    axios.put(`${this.$hostname}/api/packages/edit/tariff/${this.$route.params.id}/`, putBody)
                        .then((response) => {
                            if (response.status === 200) {
                                this.details.tariff = response.data.tariff;
                                this.newBalance = this.details.tariff;
                                this.loading = false;
                                this.dialog = false;
                                this.text = "Tariff changed!";
                                this.snackbar = true;
                            }
                        }).catch((error) => {
                        if (error.response.status === 400) {
                            this.text = "Balance too low";
                            this.snackbar = true;
                        } else {
                            this.text = "Connection error";
                            console.log(error)
                            this.snackbar = true;
                        }
                    });
                }
            },
        },
        beforeCreate() {
            if (!this.$session.exists()) {
                this.$router.push('/')
            }
        },
        mounted() {
            this.getData();

        }
    }
</script>

<style scoped>

</style>