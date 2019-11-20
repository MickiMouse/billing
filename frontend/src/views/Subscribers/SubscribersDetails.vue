<template>
    <v-content color="primary">
        <v-container fluid id="main-container" grid-list-md fill-height>
            <v-snackbar
                    v-model="snackbar"
                    :timeout="timeout"
                    top
            >
                {{ t(text) }}
                <v-btn
                        flat
                        @click="snackbar = false"
                >
                    {{t('Close')}}
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
                            <v-subheader>
                                {{t('Details')}}
                                <v-dialog v-model="deleteDialog" max-width="290">
                                    <template v-slot:activator="{ on }">
                                        <v-btn color="error" v-on="on" small icon ripple class="ml-auto mr-0">
                                            <v-icon small>delete</v-icon>
                                        </v-btn>
                                    </template>
                                    <v-card>
                                        <v-card-title class="headline">{{t('Are you sure you want to delete?')}}
                                        </v-card-title>
                                        <v-card-text>
                                            {{t('This action cannot be undone')}}
                                        </v-card-text>
                                        <v-card-actions>
                                            <v-spacer></v-spacer>
                                            <v-btn small color="error" @click="deleteDialog = false">{{t('Close')}}
                                            </v-btn>
                                            <v-btn outline small color="error" @click="deleteSubscriber">
                                                {{t('Delete')}}
                                            </v-btn>
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
                                    <v-list-tile-title>{{t('Name')}}</v-list-tile-title>
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
                                    <v-list-tile-title>{{t('Balance')}}</v-list-tile-title>
                                    <v-list-tile-sub-title>{{details.balance + $store.getters.currency}}
                                    </v-list-tile-sub-title>
                                </v-list-tile-content>
                                <v-list-tile-action>
                                    <v-dialog v-model="dialog" max-width="600px">
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
                                                                        :label="t('Balance')"
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
                                                <v-btn color="primary" text @click="dialog = false">{{t('Close')}}
                                                </v-btn>
                                                <v-btn color="primary" text @click="changeBalance">{{t('Save')}}</v-btn>
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
                                    <v-icon class="grey lighten-1 white--text">card_membership</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>{{t('Cards price')}}</v-list-tile-title>
                                    <v-list-tile-sub-title>{{totalPrice + $store.getters.currency}}
                                    </v-list-tile-sub-title>
                                </v-list-tile-content>
                            </v-list-tile>
                            <v-list-tile
                                    avatar
                                    @click=""
                            >
                                <v-list-tile-avatar>
                                    <v-icon class="grey lighten-1 white--text">mail</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>{{t('Email')}}</v-list-tile-title>
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
                                    <v-list-tile-title>{{t('Phone')}}</v-list-tile-title>
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
                                    <v-list-tile-title>{{t('Address')}}</v-list-tile-title>
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
                                    <v-list-tile-title>{{t('Reseller')}}</v-list-tile-title>
                                    <v-list-tile-sub-title>{{details.reseller.email}}</v-list-tile-sub-title>
                                </v-list-tile-content>
                            </v-list-tile>
                        </v-list>
                    </v-card>
                    <v-card class="mt-3" v-if="$session.get('isSuperuser')">
                        <v-card-title>
                            <v-text-field
                                    v-model="searchLogs"
                                    append-icon="search"
                                    :label="t('Search')"
                                    single-line
                                    hide-details
                            ></v-text-field>
                        </v-card-title>
                    </v-card>
                    <v-card class="my-3" v-if="$session.get('isSuperuser')">
                        <v-subheader>{{t('Logs')}}</v-subheader>
                        <v-data-table
                                :headers="headersLogs"
                                :items="details.logs"
                                items-per-page="5"
                                class="elevation-1"
                                :search="searchLogs"
                                :rows-per-page-text="t('Rows per page')"
                                :rows-per-page-items='[10,25, 50, {text: $translate.locale["All"], value: -1}]'
                        >
                            <template slot="items" slot-scope="props">
                                <td class="text-xs-left no-wrap">{{ props.item.date }}</td>
                                <td class="text-xs-left no-wrap">{{ props.item.log }}</td>
                            </template>
                            <template slot="pageText" slot-scope="item">
                                {{t('Elements')}} {{item.pageStart}} - {{item.pageStop}}, {{t('total')}}:
                                {{item.itemsLength}}
                            </template>
                            <template slot="no-data">
                                <v-subheader>{{t('No data available')}}</v-subheader>
                            </template>
                        </v-data-table>
                    </v-card>
                </v-flex>
                <v-flex sm4 xs12>
                    <v-card class="mb-3">
                        <v-card-title>
                            <v-text-field
                                    v-model="search"
                                    append-icon="search"
                                    :label="t('Search')"
                                    single-line
                                    hide-details
                            ></v-text-field>
                        </v-card-title>
                    </v-card>
                    <v-card class="my-3">
                        <v-subheader>{{t('Cards')}}</v-subheader>
                        <v-data-table
                                :headers="headers"
                                :items="cards"
                                items-per-page="5"
                                class="elevation-1"
                                :loading="loadingCards"
                                :search="search"
                                :rows-per-page-text="t('Rows per page')"
                                :rows-per-page-items='[10,25, 50, {text: $translate.locale["All"], value: -1}]'
                        >
                            <template slot="items" slot-scope="props">
                                <td class="text-xs-left no-wrap">{{ props.item.label }}</td>
                                <td class="text-xs-left no-wrap">{{ props.item.price+ $store.getters.currency}}</td>
                                <td class="text-xs-left no-wrap">
                                    <v-tooltip bottom>
                                        <template v-slot:activator="{ on }">
                                            <v-btn v-on="on" :to="`/cards/${props.item.pk}/details/`" color="info"
                                                   ripple
                                                   icon small dark>
                                                <v-icon small>info</v-icon>
                                            </v-btn>
                                        </template>
                                        <span>{{t('Detail')}}</span>
                                    </v-tooltip>
                                    <v-tooltip bottom>
                                        <template v-slot:activator="{ on }">
                                            <v-btn v-on="on" color="error" @click="removeCard(props.item.pk)" ripple
                                                   icon
                                                   small dark>
                                                <v-icon small>close</v-icon>
                                            </v-btn>
                                        </template>
                                        <span>{{t('Remove')}}</span>
                                    </v-tooltip>
                                </td>
                            </template>
                            <template slot="pageText" slot-scope="item">
                                {{t('Elements')}} {{item.pageStart}} - {{item.pageStop}}, {{t('total')}}:
                                {{item.itemsLength}}
                            </template>
                            <template slot="no-data">
                                <v-subheader>{{t('No data available')}}</v-subheader>
                            </template>
                        </v-data-table>
                    </v-card>
                    <v-card class="my-3">
                        <v-subheader>{{t('Available cards')}}</v-subheader>
                        <v-data-table
                                :headers="headers"
                                :items="aviableCards"
                                items-per-page="5"
                                class="elevation-1"
                                :loading="loadingAviableCards"
                                :search="search"
                                :rows-per-page-text="t('Rows per page')"
                                :rows-per-page-items='[10,25, 50, {text: $translate.locale["All"], value: -1}]'
                        >
                            <template slot="items" slot-scope="props">
                                <td class="text-xs-left no-wrap">{{ props.item.label }}</td>
                                <td class="text-xs-left no-wrap">{{ props.item.price + $store.getters.currency}}</td>
                                <td class="text-xs-left no-wrap">
                                    <v-tooltip bottom>
                                        <template v-slot:activator="{ on }">
                                            <v-btn v-on="on" :to="`/cards/${props.item.pk}/details/`" color="info"
                                                   ripple
                                                   icon small dark>
                                                <v-icon small>info</v-icon>
                                            </v-btn>
                                        </template>
                                        <span>{{t('Detail')}}</span>
                                    </v-tooltip>
                                    <v-tooltip bottom>
                                        <template v-slot:activator="{ on }">
                                            <v-btn v-on="on" @click="addCard(props.item.pk)" color="success" ripple icon
                                                   small dark>
                                                <v-icon small>add</v-icon>
                                            </v-btn>
                                        </template>
                                        <span>{{t('Add')}}</span>
                                    </v-tooltip>
                                </td>
                            </template>
                            <template slot="pageText" slot-scope="item">
                                {{t('Elements')}} {{item.pageStart}} - {{item.pageStop}}, {{t('total')}}:
                                {{item.itemsLength}}
                            </template>
                            <template slot="no-data">
                                <v-subheader>{{t('No data available')}}</v-subheader>
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
                search: '',
                searchLogs: '',
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
                        text: this.$translate.locale['Label'],
                        align: 'left',
                        //  sortable: false,
                        value: 'label',
                    },
                    {
                        text: this.$translate.locale['Price'],
                        align: 'left',
                        //  sortable: false,
                        value: 'price',
                    },
                    {text: this.$translate.locale['Action'], value: 'action', sortable: false},
                    // {text: 'Calories', value: 'calories'},
                ],
                headersLogs: [
                    {text: this.$translate.locale['Date'], value: 'date'},
                    {
                        text: this.$translate.locale['Header'],
                        align: 'left',
                        //  sortable: false,
                        value: 'log',
                    },

                    // {text: 'Calories', value: 'calories'},
                ],
                cards: [],
                aviableCards: [],
                rules: {
                    counter: value => value <= 2147483647 || this.$translate.locale['Max 2147483647'],
                    number: value => {
                        const pattern = /^(?=.+)(?:[1-9]\d*|0)?(?:\.\d+)?$/;
                        return pattern.test(value) || this.$translate.locale['Invalid number.']
                    },
                },
            }
        },
        computed: {
            totalPrice() {
                let total = 0;
                this.details.cards.forEach((item) => {
                    total += item.price
                });
                return total;
            }
        },
        methods: {
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
                        balance: this.newBalance.replace(/,/g, '.')
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
