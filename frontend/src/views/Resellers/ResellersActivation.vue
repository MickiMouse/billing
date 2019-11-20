<template>
    <v-content color="primary">
        <v-container fluid id="main-container" grid-list-md>
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

            <v-layout row wrap justify-center class="d-inline-block w-100">
                <v-card>
                    <v-card-title>
                        {{t('Resellers')}}
                        <v-spacer></v-spacer>
                        <v-text-field
                                v-model="search"
                                append-icon="search"
                                :label="t('Search')"
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
                            :rows-per-page-text="t('Rows per page')"
                            :rows-per-page-items='[10,25, 50, {text: $translate.locale["All"], value: -1}]'
                    >
                        <template slot="items" slot-scope="props">
                            <td class="text-xs-left no-wrap">{{ props.item.username}}
                            </td>
                            <td class="text-xs-left no-wrap">{{ props.item.email }}</td>
                            <td class="text-xs-left">
                                <v-tooltip bottom v-if="$session.get('isSuperuser')">
                                    <template v-slot:activator="{ on }">
                                        <v-btn v-on="on" @click="confirmReseller(props.item.pk)"
                                               color="success darken-1" icon ripple small dark>
                                            <v-icon small>add</v-icon>
                                        </v-btn>
                                    </template>
                                    <span>{{('Add')}}</span>
                                </v-tooltip>
                                <v-tooltip bottom>
                                    <template v-slot:activator="{ on }">
                                        <v-btn v-on="on" @click="deleteSubscriber(props.item.pk)" color="error"
                                               small icon ripple dark>
                                            <v-icon small>delete</v-icon>
                                        </v-btn>
                                    </template>
                                    <span>{{t('Delete')}}</span>
                                </v-tooltip>
                            </td>
                        </template>
                        <template slot="pageText" slot-scope="item">
                            {{t('Elements')}} {{item.pageStart}} - {{item.pageStop}}, {{t('total')}}: {{item.itemsLength}}
                        </template>
                        <template slot="no-data">
                            <v-subheader>{{t('No data available')}}</v-subheader>
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
        name: "ResellersActivation",
        data() {
            return {
                dialog: false,
                headers: [
                    {
                        text: this.$translate.locale['Username'],
                        align: 'left',
                        //  sortable: false,
                        value: 'username',
                    },
                    {text: this.$translate.locale['Email'], value: 'email'},
                    {text: this.$translate.locale['Action'], value: 'action', sortable: false},
                ],
                subscribers: [],
                loading: true,
                snackbar: false,
                search: '',
                text: 'Oops... Something went wrong',
                timeout: 5000,
                rules: {
                    required: value => !!value || this.$translate.locale['Required.'],
                    email: value => {
                        const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
                        return pattern.test(value) || this.$translate.locale['Invalid e-mail.']
                    },
                }
            }
        },
        methods: {
            getData() {
                axios.get(`${this.$hostname}/api/resellersTable/`)
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
            deleteSubscriber(pk) {

                axios.delete(`${this.$hostname}/api/resellers/delete/${pk}/`)
                    .then((response) => {
                        if (response.status === 204) {
                            this.text = "Successful";
                            this.snackbar = true;
                            this.getData();
                        }
                    }).catch((error) => {
                    this.text = "Connection error";
                    console.log(error)
                    this.snackbar = true;
                });
            },
            confirmReseller(pk) {

                axios.put(`${this.$hostname}/api/resellersConfirm/${pk}/`)
                    .then((response) => {
                        if (response.status === 200) {
                            this.text = "Successful";
                            this.getData();
                            this.snackbar = true;
                        }
                    }).catch((error) => {
                    this.text = "Connection error";
                    console.log(error)
                    this.snackbar = true;
                });
            },
        },
        beforeCreate() {
            if (!this.$session.exists()) {
                this.$router.push('/')
            }
            if (!this.$session.get('isSuperuser')) {
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
