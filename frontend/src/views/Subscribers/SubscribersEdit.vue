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
                        <v-form ref="form" @submit.prevent="">
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
                                            <v-card-title class="headline">{{t('Are you sure you want to delete?')}}</v-card-title>
                                            <v-card-text>{{t('This action cannot be undone')}}
                                            </v-card-text>
                                            <v-card-actions>
                                                <v-spacer></v-spacer>
                                                <v-btn small color="error" @click="deleteDialog = false">{{t('Close')}}</v-btn>
                                                <v-btn outline small color="error" @click="deleteSubscriber">{{t('Delete')}}
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
                                        <v-text-field
                                                :label="t('First name')"
                                                type="text"
                                                v-model="details.first_name"></v-text-field>
                                    </v-list-tile-content>
                                    <v-list-tile-content>
                                        <v-text-field
                                                :label="t('Last name')"
                                                type="text"
                                                v-model="details.last_name"></v-text-field>
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
                                        <v-text-field
                                                :label="t('Email')"
                                                type="email"
                                                :rules="[rules.email]"
                                                v-model="details.email"></v-text-field>
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
                                        <v-text-field
                                                :label="t('Balance')"
                                                type="number"
                                                :rules="[rules.counter,rules.number,rules.required]"
                                                v-model="details.balance"></v-text-field>
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
                                        <v-text-field
                                                :label="t('Phone')"
                                                type="number"
                                                v-model="details.telephone"></v-text-field>
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
                                        <v-text-field
                                                :label="t('Address')"
                                                type="text"
                                                v-model="details.address"></v-text-field>
                                    </v-list-tile-content>
                                </v-list-tile>
                                <v-list-tile>
                                    <v-btn small color="primary" class="ml-auto" @click="saveResellerInformation">
                                        {{t('Save')}}
                                    </v-btn>
                                </v-list-tile>
                            </v-list>
                        </v-form>

                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>
    </v-content>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "SubscribersEdit",
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
                text: 'Oops... Something went wrong',
                timeout: 5000,
                newBalance: '',
                details: {
                    address: "",
                    balance: 0,
                    cards: Array(0),
                    email: '',
                },

                headers: [
                    {
                        text:  this.$translate.locale['Label'],
                        align: 'left',
                        //  sortable: false,
                        value: 'label',
                    },
                    {text:  this.$translate.locale['Action'], value: 'action', sortable: false},
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
                    numberReverse: value => {
                        const pattern = /^-\d+$/;
                        return (pattern.test(value) || value <= 0) || this.$translate.locale['Invalid number.']
                    },
                    required: value => (!!value || value === 0) || this.$translate.locale['Required.'],
                    email: value => {
                        const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
                        return pattern.test(value) || this.$translate.locale['Invalid e-mail.']
                    },
                },
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
                            this.details.is_activated = this.details.is_activated ? 'Active' : 'Inactive';
                            console.log(this.details)
                        }
                    }).catch((error) => {
                    this.text = "Connection error";
                    console.log(error)
                    this.snackbar = true;
                });
                // this.loadingAviableCards = true;
                // axios.get(`${this.$hostname}/api/subscribers/edit/cards/${this.$route.params.id}/`)
                //     .then((response) => {
                //         if (response.status === 200) {
                //             this.aviableCards = response.data;
                //             this.loadingAviableCards = false;
                //             console.log(response.data)
                //         }
                //     }).catch((error) => {
                //     this.text = "Connection error";
                //     console.log(error)
                //     this.snackbar = true;
                // });
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
            },
            saveResellerInformation(pk) {
                if (!this.$refs.form.validate()) {
                    this.text = "Fill the form correctly";
                    this.snackbar = true;
                } else {
                    this.loading = true;
                    const resellerData = {
                        first_name: this.details.first_name,
                        last_name: this.details.last_name,
                        address: this.details.address,
                        telephone: this.details.telephone,
                        balance: this.details.balance.replace(/,/g, '.'),
                        email: this.details.email,
                    };
                    axios.put(`${this.$hostname}/api/subscribers/edit/${this.$route.params.id}/`, resellerData)
                        .then((response) => {
                            if (response.status === 200) {
                                this.getData();
                                this.text = "Settings changed!";
                                this.snackbar = true;
                                this.dialog = false;
                                this.loading = false;
                                setTimeout(() => {
                                    this.$router.push(`/subscribers/${this.$route.params.id}/details`)
                                }, 1500)
                            }
                        }).catch((error) => {
                        this.text = "Connection error";
                        console.log(error)
                        this.snackbar = true;
                        this.dialog = false;
                    })
                }
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

<style>
    .v-list--two-line.v-list--dense .v-list__tile {
        height: 72px !important;
    }
</style>