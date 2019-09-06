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
                        <v-form ref="form" @submit.prevent="">
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
                                            <v-card-text>Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet,
                                                consectetur adipisicing elit. Quam, similique.
                                            </v-card-text>
                                            <v-card-actions>
                                                <v-spacer></v-spacer>
                                                <v-btn small color="error" @click="deleteDialog = false">Close</v-btn>
                                                <v-btn outline small color="error" @click="deleteSubscriber">Delete
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
                                        <v-list-tile-title>Username</v-list-tile-title>
                                        <p class="mb-0">{{details.username}}
                                        </p>
                                    </v-list-tile-content>
                                </v-list-tile>
                                <v-list-tile
                                        avatar
                                        @click=""
                                        v-if="!details.is_superuser"
                                >
                                    <v-list-tile-avatar>
                                        <v-icon class="grey lighten-1 white--text">branding_watermark</v-icon>
                                    </v-list-tile-avatar>
                                    <v-list-tile-content>
                                        <v-text-field
                                                label="Cards prefix"
                                                type="number"
                                                :rules="[rules.rrrCounter,rules.number,rules.required,rules.checkAdminZeros]"
                                                v-model="details.rrr"></v-text-field>
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
                                        <v-list-tile-title>Email</v-list-tile-title>
                                        <p class="mb-0">{{details.email}}</p>
                                    </v-list-tile-content>
                                </v-list-tile>
                                <v-list-tile
                                        avatar
                                        @click=""
                                >
                                    <v-list-tile-avatar>
                                        <v-icon class="grey lighten-1 white--text">person</v-icon>
                                    </v-list-tile-avatar>
                                    <v-list-tile-content>
                                        <v-text-field
                                                label="First name"
                                                type="text"
                                                v-model="details.first_name"></v-text-field>
                                    </v-list-tile-content>
                                    <v-list-tile-content>
                                        <v-text-field
                                                label="Last name"
                                                type="text"
                                                v-model="details.last_name"></v-text-field>
                                    </v-list-tile-content>
                                </v-list-tile>
                                <v-list-tile
                                        avatar
                                        @click=""
                                >
                                    <v-list-tile-avatar>
                                        <v-icon class="grey lighten-1 white--text">check</v-icon>
                                    </v-list-tile-avatar>
                                    <v-list-tile-content>
                                        <v-list-tile-title>Status verification</v-list-tile-title>
                                        <p class="mb-0">{{details.is_activated}}
                                        </p>
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
                                                label="Balance"
                                                type="number"
                                                :rules="[rules.counter,rules.number,rules.required]"
                                                v-model="details.balance"></v-text-field>
                                    </v-list-tile-content>
                                    <v-list-tile-content>
                                        <v-text-field
                                                label="Credit"
                                                type="number"
                                                :rules="[rules.counter,rules.numberReverse,rules.required]"
                                                v-model="details.credit"></v-text-field>
                                    </v-list-tile-content>
                                </v-list-tile>
                                <v-list-tile
                                        avatar
                                        @click=""
                                >
                                    <v-list-tile-avatar>
                                        <v-icon class="grey lighten-1 white--text">card_membership</v-icon>
                                    </v-list-tile-avatar>
                                    <v-list-tile-content>
                                        <v-text-field
                                                label="Card price (materials)"
                                                type="number"
                                                :rules="[rules.counter,rules.number,rules.required]"
                                                v-model="details.price_card"></v-text-field>
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
                                                label="Phone"
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
                                                label="Address"
                                                type="text"
                                                v-model="details.address"></v-text-field>
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
                                                label="Zone"
                                                type="text"
                                                v-model="details.zone"></v-text-field>
                                    </v-list-tile-content>
                                </v-list-tile>
                                <v-list-tile
                                        avatar
                                        @click=""
                                >
                                    <v-list-tile-avatar>
                                        <v-icon class="grey lighten-1 white--text">comment</v-icon>
                                    </v-list-tile-avatar>
                                    <v-list-tile-content>
                                        <v-text-field
                                                label="Comment"
                                                type="text"
                                                v-model="details.comment"></v-text-field>
                                    </v-list-tile-content>
                                </v-list-tile>
                                <v-list-tile>
                                    <v-btn small color="primary" class="ml-auto" @click="saveResellerInformation">Save
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
        name: "ResellersEdit",
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
                    rrrCounter: value => (value <= 999 && value >= 0 && value.length <= 3) || 'Min 0 Max 999',
                    checkAdminZeros: value => ((value !== '000' && value !== '00' && value !== '0') || this.details.is_superuser) || 'Only admins can have prefix "000"',
                    number: value => {
                        const pattern = /^\d+$/;
                        return pattern.test(value) || 'Invalid number.'
                    },
                    numberReverse: value => {
                        const pattern = /^-\d+$/;
                        return (pattern.test(value) || value <= 0) || 'Invalid number.'
                    },
                    required: value => (!!value || value === 0) || 'Required.',
                    email: value => {
                        const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
                        return pattern.test(value) || 'Invalid e-mail.'
                    },
                },
            }
        },
        methods: {
            getData() {
                this.loadingCards = true;
                axios.get(`${this.$hostname}/api/resellers/${this.$route.params.id}/`)
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
            },
            deleteSubscriber() {

                axios.delete(`${this.$hostname}/api/resellers/delete/${this.$route.params.id}/`)
                    .then((response) => {
                        if (response.status === 204) {
                            console.log(response.data);
                            this.$router.push('/resellers')
                        }
                    }).catch((error) => {
                    this.text = "Connection error";
                    console.log(error)
                    this.snackbar = true;
                });
            },
            saveResellerInformation() {
                if (!this.$refs.form.validate()) {
                    this.text = "Fill the form correctly";
                    this.snackbar = true;
                } else {
                    this.loading = true;
                    const resellerData = {
                        username: this.details.username,
                        rrr: this.rrr,
                        first_name: this.details.first_name,
                        last_name: this.details.last_name,
                        address: this.details.address,
                        telephone: this.details.telephone,
                        zone: this.details.zone,
                        balance: this.details.balance,
                        credit: this.details.credit,
                        price_card: this.details.price_card,
                        comment: this.details.comment
                    };
                    axios.put(`${this.$hostname}/api/resellers/edit/${this.$route.params.id}/`, resellerData)
                        .then((response) => {
                            if (response.status === 200) {
                                this.getData();
                                this.text = "Settings changed!";
                                this.snackbar = true;
                                this.dialog = false;
                                this.loading = false;
                                setTimeout(() => {
                                    this.$router.push(`/resellers/${this.$route.params.id}/details`)
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
        computed: {
            rrr() {
                if (this.details.rrr < 10 && this.details.rrr.length < 2) {
                    return '00' + this.details.rrr
                } else if (this.details.rrr < 100 && this.details.rrr.length < 3) {
                    return '0' + this.details.rrr
                } else {
                    return this.details.rrr.toString()
                }
            }
        },
        beforeCreate() {
            if (!this.$session.exists()) {
                this.$router.push('/')
            }
            if(!this.$session.get('isSuperuser')){
                this.$router.push('/cards')
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