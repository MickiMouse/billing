<template>
    <v-flex>
        <v-card>
            <v-card-text>
                <v-autocomplete
                        label="Subscribers"
                        :items="names"
                        v-model="email"
                ></v-autocomplete>
                <v-btn color="primary ml-auto" @click.prevent="getLogs" text>Send</v-btn>
            </v-card-text>
        </v-card>
        <v-card class="mt-3">
            <v-card-title>
                <v-text-field
                        v-model="searchLogs"
                        append-icon="search"
                        label="Search"
                        single-line
                        hide-details
                ></v-text-field>
            </v-card-title>
        </v-card>
        <v-card class="my-3">
            <v-subheader>Logs</v-subheader>
            <v-data-table
                    :headers="headersLogs"
                    :items="logs"
                    items-per-page="5"
                    class="elevation-1"
                    :search="searchLogs"
                    :loading="loading"
            >
                <template slot="items" slot-scope="props">
                    <td class="text-xs-left no-wrap">{{ props.item.date }}</td>
                    <td class="text-xs-left no-wrap">{{ props.item.log }}</td>
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
                    {text: 'Date', value: 'date'},
                    {
                        text: 'Header',
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