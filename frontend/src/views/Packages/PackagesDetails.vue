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
            >
                <v-flex md8>
                    <v-card
                            class="mx-auto"
                            :loading="loading"
                    >
                        <v-list two-line subheader dense>
                            <v-subheader>Details
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
                                    <v-list-tile-sub-title>{{details.tariff}}</v-list-tile-sub-title>
                                </v-list-tile-content>
                                <!--<v-list-tile-action>-->
                                    <!--<v-dialog v-model="dialog" persistent max-width="600px">-->
                                        <!--<template v-slot:activator="{ on }">-->
                                            <!--<v-btn icon ripple v-on="on">-->
                                                <!--<v-icon color="grey lighten-1">edit</v-icon>-->
                                            <!--</v-btn>-->
                                        <!--</template>-->
                                        <!--<v-card>-->
                                            <!--<v-card-text>-->
                                                <!--<v-container grid-list-md>-->
                                                    <!--<v-layout wrap>-->

                                                        <!--<v-flex xs12>-->
                                                            <!--<v-form-->
                                                                    <!--ref="form">-->
                                                                <!--<v-text-field-->
                                                                        <!--label="Balance"-->
                                                                        <!--type="number" required-->
                                                                        <!--:rules="[rules.counter, rules.number]"-->
                                                                        <!--v-model="newBalance"></v-text-field>-->
                                                            <!--</v-form>-->
                                                        <!--</v-flex>-->

                                                    <!--</v-layout>-->
                                                <!--</v-container>-->
                                            <!--</v-card-text>-->
                                            <!--<v-card-actions>-->
                                                <!--<v-spacer></v-spacer>-->
                                                <!--<v-btn color="primary" text @click="dialog = false">Close</v-btn>-->
                                                <!--<v-btn color="primary" text @click="changeBalance">Save</v-btn>-->
                                            <!--</v-card-actions>-->
                                        <!--</v-card>-->
                                    <!--</v-dialog>-->
                                <!--</v-list-tile-action>-->
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
                                    <v-list-tile-title>Card</v-list-tile-title>
                                    <v-list-tile-sub-title>{{details.cards.label}}</v-list-tile-sub-title>
                                </v-list-tile-content>
                                <v-list-tile-avatar>
                                    <v-tooltip bottom>
                                        <template v-slot:activator="{ on }">
                                            <v-btn v-on="on" :to="`/cards/${details.cards.pk}/details/`" color="info" fab small dark>
                                                <v-icon>info</v-icon>
                                            </v-btn>
                                        </template>
                                        <span>Detail</span>
                                    </v-tooltip>
                                </v-list-tile-avatar>
                            </v-list-tile>
                            <!--<v-list-tile-->
                                    <!--avatar-->
                                    <!--@click=""-->
                            <!--&gt;-->
                                <!--<v-list-tile-avatar>-->
                                    <!--<v-icon class="grey lighten-1 white&#45;&#45;text">people</v-icon>-->
                                <!--</v-list-tile-avatar>-->
                                <!--<v-list-tile-content>-->
                                    <!--<v-list-tile-title>Reseller</v-list-tile-title>-->
                                    <!--<v-list-tile-sub-title>{{details.reseller.email}}</v-list-tile-sub-title>-->
                                <!--</v-list-tile-content>-->
                                <!--<v-list-tile-avatar>-->
                                    <!--<v-tooltip bottom>-->
                                        <!--<template v-slot:activator="{ on }">-->
                                            <!--<v-btn v-on="on" :to="`/resellers/${details.reseller.pk}/details/`" color="info" fab small dark>-->
                                                <!--<v-icon>info</v-icon>-->
                                            <!--</v-btn>-->
                                        <!--</template>-->
                                        <!--<span>Detail</span>-->
                                    <!--</v-tooltip>-->
                                <!--</v-list-tile-avatar>-->
                            <!--</v-list-tile>-->
                        </v-list>
                    </v-card>
                </v-flex>
                <v-flex md4>
                    <v-data-table
                            :headers="headers"
                            :items="bouquets"
                            items-per-page="5"
                            class="elevation-1"
                            :loading="loadingPackages"
                    >
                        <template slot="items" slot-scope="props">
                            <td class="text-xs-left no-wrap">{{ props.item.name }}</td>
                            <td class="text-xs-left no-wrap">
                                <v-tooltip bottom>
                                    <template v-slot:activator="{ on }">
                                        <v-btn v-on="on" :to="`/subscribers/${props.item.pk}/details/`" color="info" fab small dark>
                                            <v-icon>info</v-icon>
                                        </v-btn>
                                    </template>
                                    <span>Detail</span>
                                </v-tooltip>
                                <v-tooltip bottom>
                                    <template v-slot:activator="{ on }">
                                        <v-btn v-on="on" color="error" @click="removeCard(props.item.pk)" fab small dark>
                                            <v-icon>close</v-icon>
                                        </v-btn>
                                    </template>
                                    <span>Remove</span>
                                </v-tooltip>
                            </td>
                        </template>
                    </v-data-table>
                    <!--<v-data-table-->
                            <!--:headers="headers"-->
                            <!--:items="aviablePackages"-->
                            <!--items-per-page="5"-->
                            <!--class="elevation-1 mt-3"-->
                            <!--:loading="loadingAviablePackages"-->
                    <!--&gt;-->
                        <!--<template slot="items" slot-scope="props">-->
                            <!--<td class="text-xs-left no-wrap">{{ props.item.header }}</td>-->
                            <!--<td class="text-xs-left no-wrap">-->
                                <!--<v-tooltip bottom>-->
                                    <!--<template v-slot:activator="{ on }">-->
                                        <!--<v-btn v-on="on" :to="`/subscribers/${props.item.pk}/details/`" color="info" fab small dark>-->
                                            <!--<v-icon>info</v-icon>-->
                                        <!--</v-btn>-->
                                    <!--</template>-->
                                    <!--<span>Detail</span>-->
                                <!--</v-tooltip>-->
                                <!--<v-tooltip bottom>-->
                                    <!--<template v-slot:activator="{ on }">-->
                                        <!--<v-btn v-on="on" @click="addPackage(props.item.pk)" color="success" fab small dark>-->
                                            <!--<v-icon>add</v-icon>-->
                                        <!--</v-btn>-->
                                    <!--</template>-->
                                    <!--<span>Add</span>-->
                                <!--</v-tooltip>-->
                            <!--</td>-->
                        <!--</template>-->
                    <!--</v-data-table>-->
                </v-flex>
            </v-layout>
        </v-container>
    </v-content>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "PackagesDetails",
        data() {
            return {
                snack: false,
                snackColor: '',
                snackText: '',
                loading: true,
                loadingPackages: true,
                loadingAviablePackages: true,
                snackbar: false,
                dialog: false,
                text: 'Oops... Something went wrong',
                timeout: 5000,
                newBalance: '',
                details: {
                },

                headers: [
                    {
                        text: 'Header',
                        align: 'left',
                        //  sortable: false,
                        value: 'name',
                    },
                    {text: 'Action', value: 'action', sortable: false},
                    // {text: 'Calories', value: 'calories'},
                ],
                bouquets:[],
                aviablePackages:[],
                rules: {
                    counter: value => value <= 2147483647 || 'Max 2147483647',
                    number: value => {
                        const pattern = /^\d+$/;
                        return pattern.test(value) || 'Invalid number.'
                    },
                },
            }
        },
        computed:{

        },
        methods: {
            save() {
                this.snack = true
                this.snackColor = 'success'
                this.snackText = 'Data saved'
            },
            cancel() {
                this.snack = true
                this.snackColor = 'error'
                this.snackText = 'Canceled'
            },
            getData() {
                this.loadingPackages = true;
                axios.get(`${this.$hostname}/api/packages/${this.$route.params.id}/`)
                    .then((response) => {
                        if (response.status === 200) {
                            console.log(response.data)
                            this.details = response.data;
                            this.bouquets = this.details.bouquets;
                            this.newBalance = this.details.balance;
                            this.loadingPackages = false;
                            console.log(response.data,this.bouquets)
                        }
                    }).catch((error) => {
                    this.text = "Connection error";
                    console.log(error)
                    this.snackbar = true;
                });
                this.loadingAviablePackages = true;
                axios.get(`${this.$hostname}/api/packages-filter/${this.$route.params.id}/`)
                    .then((response) => {
                        if (response.status === 200) {
                            this.aviablePackages = response.data;
                            this.loadingAviablePackages = false;
                            console.log(response.data)
                        }
                    }).catch((error) => {
                    this.text = "Connection error";
                    console.log(error)
                    this.snackbar = true;
                });
            },
            changeBalance() {
                if (!this.$refs.form.validate()) {
                    this.text = "Fill the form correctly";
                    this.snackbar = true;
                } else {
                    this.loading = true;
                    const putBody = {
                        balance: this.newBalance
                    };
                    axios.put(`${this.$hostname}/api/subscribers/edit/balance/${this.$route.params.id}/`, putBody)
                        .then((response) => {
                            if (response.status === 200) {
                                this.details.balance = response.data.balance;
                                this.newBalance = this.details.balance;
                                this.loading = false;
                                this.dialog = false;
                                this.text = "Balance changed!";
                                this.snackbar = true;
                            }
                        }).catch((error) => {
                        this.text = "Connection error";
                        console.log(error)
                        this.snackbar = true;
                    });
                }
            },
            addPackage(pk){
                axios.put(`${this.$hostname}/api/packages/edit/package/${this.$route.params.id}/`,{package: pk})
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
            removeCard(pk){
                axios.put(`${this.$hostname}/api/packages/delete/package/${this.$route.params.id}/`,{package: pk})
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
            deleteSubscriber(){
                axios.delete(`${this.$hostname}/api/subscribers/delete/${this.$route.params.id}/`)
                    .then((response) => {
                        if (response.status === 200) {
                            console.log(response.data);
                            this.$router.push('/subscribers')
                        }
                    }).catch((error) => {
                    this.text = "Connection error";
                    console.log(error)
                    this.snackbar = true;
                });
            }
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