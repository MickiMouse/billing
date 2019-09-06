<template>
    <v-content color="primary">
        <v-container fluid id="main-container" grid-list-md>
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

            <v-layout row wrap justify-center class="d-inline-block w-100">
                <v-card>
                    <v-card-title>
                        Resellers
                        <v-spacer></v-spacer>
                        <v-text-field
                                v-model="search"
                                append-icon="search"
                                label="Search"
                                single-line
                                hide-details
                        ></v-text-field>
                    </v-card-title>
                    <v-data-table
                            :headers="headers"
                            :items="subscribers"
                            :items-per-page="5"
                            class="elevation-1"
                            :loading="loading"
                            :search="search"
                    >
                        <template slot="items" slot-scope="props">
                            <td class="text-xs-left no-wrap">{{ props.item.username}}
                            </td>
                            <td class="text-xs-left no-wrap">{{ props.item.email }}</td>
                            <td class="text-xs-left no-wrap">{{ props.item.balance + $store.getters.currency}}</td>
                            <td class="text-xs-left">
                                <v-tooltip bottom>
                                    <template v-slot:activator="{ on }">
                                        <v-btn v-on="on" :to="`/resellers/${props.item.pk}/details/`" color="info"
                                               small icon ripple dark>
                                            <v-icon small>info</v-icon>
                                        </v-btn>
                                    </template>
                                    <span>Detail</span>
                                </v-tooltip>
                                <v-tooltip bottom v-if="$session.get('isSuperuser')">
                                    <template v-slot:activator="{ on }">
                                        <v-btn v-on="on" :to="`/resellers/${props.item.pk}/edit/`" color="success" icon ripple small dark>
                                            <v-icon small>edit</v-icon>
                                        </v-btn>
                                    </template>
                                    <span>Edit</span>
                                </v-tooltip>
                            </td>
                        </template>

                    </v-data-table>
                </v-card>
            </v-layout>
        </v-container>
    </v-content>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "Resellers",
        data() {
            return {
                dialog: false,
                headers: [
                    {
                        text: 'Username',
                        align: 'left',
                        //  sortable: false,
                        value: 'username',
                    },
                    {text: 'Email', value: 'email'},
                    {text: 'Balance', value: 'balance'},
                    {text: 'Action', value: 'action', sortable: false},
                ],
                subscribers: [],
                loading: true,
                snackbar: false,
                search: '',
                text: 'Oops... Something went wrong',
                timeout: 5000,
                rules: {
                    required: value => !!value || 'Required.',
                    email: value => {
                        const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
                        return pattern.test(value) || 'Invalid e-mail.'
                    },
                }
            }
        },
        methods: {
            getData() {
                axios.get(`${this.$hostname}/api/resellers/`)
                    .then((response) => {
                        console.log(response.data)
                        if (response.status === 200) {
                            this.subscribers = response.data;
                            console.log(this.subscribers)
                            this.loading = false;
                        }
                    }).catch((error) => {
                    this.text = "Connection error";
                    console.log(error)
                    this.snackbar = true;
                });
            },
            addressCheck() {
                this.errorMessages = this.address && !this.name
                    ? 'Hey! I\'m required'
                    : ''

                return true
            },
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
        },
    }
</script>

<style scoped>

</style>