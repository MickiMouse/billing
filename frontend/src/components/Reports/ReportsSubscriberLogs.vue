<template>
    <v-flex>
        <v-card>
            <v-card-text>
                <v-autocomplete
                        :label='t("Subscribers")'
                        :items="names"
                        v-model="email"
                ></v-autocomplete>
                <v-btn color="primary ml-auto" @click.prevent="getLogs" text>{{t('Send')}}</v-btn>
            </v-card-text>
        </v-card>
        <v-card class="mt-3">
            <v-card-title>
                <v-text-field
                        v-model="searchLogs"
                        append-icon="search"
                        :label='t("Search")'
                        single-line
                        hide-details
                ></v-text-field>
            </v-card-title>
        </v-card>
        <v-card class="my-3">
            <v-subheader>{{t('Logs')}}</v-subheader>
            <v-data-table
                    :rows-per-page-text="t('Rows per page')"

                    :headers="headersLogs"
                    :items="logs"
                    items-per-page="5"
                    class="elevation-1"
                    :search="searchLogs"
                    :loading="loading"
                    :rows-per-page-items='[10,25, 50, {text: $translate.locale["All"], value: -1}]'
            >
                <template slot="items" slot-scope="props">
                    <td class="text-xs-left no-wrap">{{ props.item.date }}</td>
                    <td class="text-xs-left no-wrap">{{ props.item.log }}</td>
                </template>
                <template slot="pageText" slot-scope="item">
                    {{t('Elements')}} {{item.pageStart}} - {{item.pageStop}}, {{t('total')}}: {{item.itemsLength}}
                </template>
                <template slot="no-data">
                    <v-subheader>{{t('No data available')}}</v-subheader>
                </template>
            </v-data-table>
        </v-card>
    </v-flex>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "ReportsSubscriberLogs",
        props: {
            dateLt: String,
            dateRt: String
        },
        data() {
            return {
                loading: true,
                details: {},
                email: '',
                logs: [],
                names: [],
                searchLogs: '',
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
            }
        },
        methods: {
            getData() {
                axios.get(`${this.$hostname}/api/subscribers/`)
                    .then((response) => {
                        console.log(response.data)
                        if (response.status === 200) {
                            this.details = response.data;
                            this.names = this.details.map((item, i) => {
                                return item.email
                            });
                            console.log(this.names)
                            this.loading = false;
                        }
                    }).catch((error) => {
                    this.text = "Connection error";
                    console.log(error)
                    this.snackbar = true;
                });
            },
            getLogs() {
                this.loading = true;
                axios.post(`${this.$hostname}/api/report-logs/`, {
                    dateLt: this.dateLt,
                    dateRt: this.dateRt,
                    email: this.email
                })
                    .then((response) => {
                        if (response.status === 200) {
                            console.log(response.data)
                            this.logs = response.data;
                            this.loading = false;
                        }
                    }).catch((error) => {
                    if (error.response.status === 400) {
                        this.text = "Incorrect data";
                        console.log(error)
                        this.snackbar = true;
                    } else {
                        this.text = "Connection error";
                        console.log(error)
                        this.snackbar = true;
                    }
                });
            },
        },
        computed: {},
        mounted() {
            this.getData();

        }
    }
</script>

<style scoped>

</style>
