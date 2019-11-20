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
                                :label='t("Search")'
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
                            <td class="text-xs-left no-wrap">{{ props.item.balance + $store.getters.currency}}</td>
                            <td class="text-xs-left">
                                <v-tooltip bottom>
                                    <template v-slot:activator="{ on }">
                                        <v-btn v-on="on" :to="`/resellers/${props.item.pk}/details/`" color="info"
                                               small icon ripple dark>
                                            <v-icon small>{{t('info')}}</v-icon>
                                        </v-btn>
                                    </template>
                                    <span>{{t('Detail')}}</span>
                                </v-tooltip>
                                <v-tooltip bottom v-if="$session.get('isSuperuser')">
                                    <template v-slot:activator="{ on }">
                                        <v-btn v-on="on" :to="`/resellers/${props.item.pk}/edit/`" color="success" icon ripple small dark>
                                            <v-icon small>edit</v-icon>
                                        </v-btn>
                                    </template>
                                    <span>{{t('Edit')}}</span>
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
        name: "Resellers",
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
                    {text: this.$translate.locale['Balance'], value: 'balance'},
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
