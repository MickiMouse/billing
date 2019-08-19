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
                                <v-dialog v-model="deleteDialog" persistent max-width="290">
                                    <template v-slot:activator="{ on }">
                                        <v-btn color="error" v-on="on" small icon ripple class="ml-auto mr-0">
                                            <v-icon small>delete</v-icon>
                                        </v-btn>
                                    </template>
                                    <v-card>
                                        <v-card-title class="headline">Lorem ipsum dolor sit.</v-card-title>
                                        <v-card-text>Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quam, similique.</v-card-text>
                                        <v-card-actions>
                                            <v-spacer></v-spacer>
                                            <v-btn small color="error" @click="deleteDialog = false">Close</v-btn>
                                            <v-btn outline small color="error" @click="deleteSubscriber">Delete</v-btn>
                                        </v-card-actions>
                                    </v-card>
                                </v-dialog>

                            </v-subheader>
                            <v-list-tile
                                    avatar
                                    @click=""
                            >
                                <v-list-tile-avatar>
                                    <v-icon class="grey lighten-1 white--text">person</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>Name</v-list-tile-title>
                                    <v-list-tile-sub-title>{{details.first_name}} {{details.last_name}}
                                    </v-list-tile-sub-title>
                                </v-list-tile-content>
                            </v-list-tile>
                            <v-list-tile
                                    v-if="!$store.getters.isPREPAYMENT"
                                    avatar
                                    @click=""
                            >
                                <v-list-tile-avatar>
                                    <v-icon class="grey lighten-1 white--text">account_balance_wallet</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>Balance</v-list-tile-title>
                                    <v-list-tile-sub-title>{{details.balance}}</v-list-tile-sub-title>
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
                                                                    ref="form">
                                                                <v-text-field
                                                                        label="Balance"
                                                                        type="number" required
                                                                        :rules="[rules.counter, rules.number]"
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
                                    <v-icon class="grey lighten-1 white--text">mail</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>Email</v-list-tile-title>
                                    <v-list-tile-sub-title>{{details.email}}</v-list-tile-sub-title>
                                </v-list-tile-content>
                            </v-list-tile>
                            <v-list-tile
                                    avatar
                                    @click=""
                            >
                                <v-list-tile-avatar>
                                    <v-icon class="grey lighten-1 white--text">phone</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>Phone</v-list-tile-title>
                                    <v-list-tile-sub-title>{{details.telephone}}</v-list-tile-sub-title>
                                </v-list-tile-content>
                            </v-list-tile>
                            <v-list-tile
                                    avatar
                                    @click=""
                            >
                                <v-list-tile-avatar>
                                    <v-icon class="grey lighten-1 white--text">place</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>Address</v-list-tile-title>
                                    <v-list-tile-sub-title>{{details.address}}</v-list-tile-sub-title>
                                </v-list-tile-content>
                            </v-list-tile>
                            <v-list-tile
                                    avatar
                                    @click=""
                            >
                                <v-list-tile-avatar>
                                    <v-icon class="grey lighten-1 white--text">people</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>Reseller</v-list-tile-title>
                                    <v-list-tile-sub-title>{{details.reseller.email}}</v-list-tile-sub-title>
                                </v-list-tile-content>
                            </v-list-tile>
                        </v-list>
                    </v-card>
                </v-flex>
                <v-flex md4>
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
                        <v-subheader>Cards</v-subheader>
                        <v-data-table
                                :headers="headers"
                                :items="cards"
                                items-per-page="5"
                                class="elevation-1"
                                :loading="loadingCards"
                                :search="search"
                        >
                            <template slot="items" slot-scope="props">
                                <td class="text-xs-left no-wrap">{{ props.item.label }}</td>
                                <td class="text-xs-left no-wrap">
                                    <v-tooltip bottom>
                                        <template v-slot:activator="{ on }">
                                            <v-btn v-on="on" :to="`/cards/${props.item.pk}/details/`" color="info" ripple
                                                   icon small dark>
                                                <v-icon small>info</v-icon>
                                            </v-btn>
                                        </template>
                                        <span>Detail</span>
                                    </v-tooltip>
                                    <v-tooltip bottom>
                                        <template v-slot:activator="{ on }">
                                            <v-btn v-on="on" color="error" @click="removeCard(props.item.pk)" ripple icon
                                                   small dark>
                                                <v-icon small>close</v-icon>
                                            </v-btn>
                                        </template>
                                        <span>Remove</span>
                                    </v-tooltip>
                                </td>
                            </template>
                        </v-data-table>
                    </v-card>
                    <v-card class="my-3">
                        <v-subheader>Available cards</v-subheader>
                        <v-data-table
                                :headers="headers"
                                :items="aviableCards"
                                items-per-page="5"
                                class="elevation-1"
                                :loading="loadingAviableCards"
                                :search="search"
                        >
                            <template slot="items" slot-scope="props">
                                <td class="text-xs-left no-wrap">{{ props.item.label }}</td>
                                <td class="text-xs-left no-wrap">
                                    <v-tooltip bottom>
                                        <template v-slot:activator="{ on }">
                                            <v-btn v-on="on" :to="`/cards/${props.item.pk}/details/`" color="info" ripple
                                                   icon small dark>
                                                <v-icon small>info</v-icon>
                                            </v-btn>
                                        </template>
                                        <span>Detail</span>
                                    </v-tooltip>
                                    <v-tooltip bottom>
                                        <template v-slot:activator="{ on }">
                                            <v-btn v-on="on" @click="addCard(props.item.pk)" color="success" ripple icon
                                                   small dark>
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
        name: "SubscribersDetails",
        data() {
            return {
                snack: false,
                snackColor: '',
                snackText: '',
                loading: true,
                loadingCards: true,
                loadingAviableCards: true,
                snackbar: false,
                dialog: false,
                deleteDialog: false,
                search:'',
                text: 'Oops... Something went wrong',
                timeout: 5000,
                newBalance: '',
                details: {
                    address: "",
                    balance: 0,
                    cards: Array(0),
                    email: '',
                    first_name: "",
                    id: 0,
                    last_name: "",
                    reseller: 0,
                    telephone: ""
                },

                headers: [
                    {
                        text: 'Label',
                        align: 'left',
                        //  sortable: false,
                        value: 'label',
                    },
                    {text: 'Action', value: 'action', sortable: false},
                    // {text: 'Calories', value: 'calories'},
                ],
                cards: [],
                aviableCards: [],
                rules: {
                    counter: value => value <= 2147483647 || 'Max 2147483647',
                    number: value => {
                        const pattern = /^\d+$/;
                        return pattern.test(value) || 'Invalid number.'
                    },
                },
            }
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
                this.loadingCards = true;
                axios.get(`${this.$hostname}/api/subscribers/${this.$route.params.id}/`)
                    .then((response) => {
                        if (response.status === 200) {
                            this.details = response.data;
                            this.cards = this.details.cards;
                            this.newBalance = this.details.balance;
                            this.loadingCards = false;
                            console.log(response.data)
                        }
                    }).catch((error) => {
                    this.text = "Connection error";
                    console.log(error)
                    this.snackbar = true;
                });
                this.loadingAviableCards = true;
                axios.get(`${this.$hostname}/api/subscribers/edit/cards/${this.$route.params.id}/`)
                    .then((response) => {
                        if (response.status === 200) {
                            this.aviableCards = response.data;
                            this.loadingAviableCards = false;
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
                        if (error.response.status === 400) {
                            this.text = "Balance too low";
                            this.snackbar = true;
                            this.dialog = false;
                        } else {
                            this.text = "Connection error";
                            console.log(error)
                            this.snackbar = true;
                        }
                    });
                }
            },
            addCard(pk) {
                axios.put(`${this.$hostname}/api/subscribers/edit/cards/${this.$route.params.id}/`, {card: pk})
                    .then((response) => {
                        if (response.status === 200) {
                            console.log(response.data);
                            this.getData();
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
            },
            removeCard(pk) {
                axios.put(`${this.$hostname}/api/subscribers/delete/cards/${this.$route.params.id}/`, {card: pk})
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
            deleteSubscriber() {
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