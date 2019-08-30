<template>
    <v-content color="primary">
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
        <v-container fluid id="main-container" grid-list-md>
            <v-layout row wrap justify-center>
                <v-flex xs7 justify-center>
                    <v-card>
                        <v-list two-line>
                            <v-list two-line subheader dense>
                                <v-subheader>Details
                                </v-subheader>
                                <v-list-tile
                                        avatar
                                        @click=""
                                >
                                    <v-list-tile-avatar>
                                        <v-icon class="grey lighten-1 white--text">person</v-icon>
                                    </v-list-tile-avatar>
                                    <v-list-tile-content>
                                        <v-list-tile-title>Active subscribers</v-list-tile-title>
                                        <p class="mb-0">{{details.subscribers}}
                                        </p>
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
                                        <v-list-tile-title>Total subscribers</v-list-tile-title>
                                        <p class="mb-0">{{details.count_sub}}
                                        </p>
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
                                        <v-list-tile-title>Actions with cards</v-list-tile-title>
                                        <p class="mb-0">{{details.sell_card}}
                                        </p>
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
                                        <v-list-tile-title>Cards in use</v-list-tile-title>
                                        <p class="mb-0">{{details.cards}}
                                        </p>
                                    </v-list-tile-content>
                                </v-list-tile>
                                <v-list-tile
                                        avatar
                                        @click=""
                                >
                                    <v-list-tile-avatar>
                                        <v-icon class="grey lighten-1 white--text">score</v-icon>
                                    </v-list-tile-avatar>
                                    <v-list-tile-content>
                                        <v-list-tile-title>Total from continue subscriptions</v-list-tile-title>
                                        <p class="mb-0">{{details.sell_sub}}
                                        </p>
                                    </v-list-tile-content>
                                </v-list-tile>
                                <v-list-tile
                                        avatar
                                        @click=""
                                >
                                    <v-list-tile-avatar>
                                        <v-icon class="grey lighten-1 white--text">archive</v-icon>
                                    </v-list-tile-avatar>
                                    <v-list-tile-content>
                                        <v-list-tile-title>Packages in use</v-list-tile-title>
                                        <p class="mb-0">{{details.sell_pack}}
                                        </p>
                                    </v-list-tile-content>
                                </v-list-tile>
                            </v-list>
                        </v-list>
                    </v-card>
                </v-flex>
                <v-flex xs5 justify-center>
                    <v-form @submit.prevent="showLogs" ref="form">
                        <v-card class="px-3 mb-3">
                            <v-row>
                                <v-col cols="12" lg="6">
                                    <v-menu
                                            ref="menu1"
                                            v-model="menu1"
                                            :close-on-content-click="false"
                                            transition="scale-transition"
                                            offset-y
                                            full-width
                                            max-width="290px"
                                            min-width="290px"
                                    >
                                        <template v-slot:activator="{ on }">
                                            <v-text-field
                                                    v-model="dateLt"
                                                    label="From"
                                                    hint="YYYY-MM-DD format"
                                                    persistent-hint
                                                    prepend-icon="event"
                                                    @blur="dateLt = parseDate(dateLt)"
                                                    v-on="on"
                                                    readonly
                                            ></v-text-field>
                                        </template>
                                        <v-date-picker v-model="dateLt" no-title :max="dateRt" @input="menu1 = false"></v-date-picker>
                                    </v-menu>
                                </v-col>
                                <v-col cols="12" lg="6">
                                    <v-menu
                                            v-model="menu2"
                                            :close-on-content-click="false"
                                            transition="scale-transition"
                                            offset-y
                                            full-width
                                            max-width="290px"
                                            min-width="290px"
                                    >
                                        <template v-slot:activator="{ on }">
                                            <v-text-field
                                                    v-model="dateRt"
                                                    label="To"
                                                    hint="YYYY-MM-DD format"
                                                    persistent-hint
                                                    prepend-icon="event"
                                                    @blur="dateRt = parseDate(dateRt)"
                                                    readonly
                                                    v-on="on"
                                            ></v-text-field>
                                        </template>
                                        <v-date-picker v-model="dateRt" no-title  :min="dateLt" @input="menu2 = false"></v-date-picker>
                                    </v-menu>
                                </v-col>
                            </v-row>
                        </v-card>
                        <v-card class="px-3 mb-3">
                            <v-text-field
                                    label="Email (reseller)"
                                    name="Email"
                                    prepend-icon="person"
                                    :rules="[rules.email]"
                                    v-model="reseller"
                                    class="py-3"
                            ></v-text-field>
                            <v-btn
                                    color="primary"
                                    type="submit"
                            >
                                Show
                            </v-btn>

                        </v-card>
                    </v-form>
                    <v-card class="px-3 mb-3">
                        <v-form ref="subscriberForm" @submit.prevent="showLogsSubscriber">
                            <v-text-field
                                    label="Email (subscriber)"
                                    name="Email"
                                    prepend-icon="person"
                                    :rules="[rules.email]"
                                    v-model="subscriber"
                                    class="py-3"
                            ></v-text-field>
                            <v-btn
                                    color="primary"
                                    type="submit"
                            >
                                Show
                            </v-btn>
                        </v-form>
                    </v-card>
                    <v-subheader>Subscriber logs</v-subheader>
                    <v-card class="mt-3" v-if="$session.get('isSuperuser')">
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
                    <v-data-table
                            :headers="headersLogs"
                            :items="details.subscriber_logs"
                            items-per-page="5"
                            class="elevation-1"
                            :search="searchLogs"
                    >
                        <template slot="items" slot-scope="props">
                            <td class="text-xs-left no-wrap">{{ props.item.date }}</td>
                            <td class="text-xs-left no-wrap">{{ props.item.log }}</td>
                        </template>
                    </v-data-table>
                </v-flex>
            </v-layout>
        </v-container>

    </v-content>

</template>

<script>
    import axios from 'axios';


    export default {
        name: "Reports",
        data: vm => ({
            dateLt: '',
            dateRt: '',
            dateFormatted: vm.formatDate(new Date().toISOString().substr(0, 10)),
            menu1: false,
            menu2: false,
            details:{},
            reseller:'',
            searchLogs: '',
            subscriber:'',
            snackbar: false,
            text: 'Oops... Something went wrong',
            timeout: 5000,
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
            rules: {
                required: value => !!value || 'Required.',
                username: value => (value.length >= 4 && value.length <= 150) || 'Username between the 4 - 150 characters',
                counter: value => value.length >= 8 || 'Min 8 characters',
                email: value => {
                    const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
                    return pattern.test(value) || 'Invalid e-mail.'
                },
            },
        }),
        methods:{
            getData() {
                this.loadingCards = true;
                this.loadingAviableCards = true;
                axios.post(`${this.$hostname}/api/reports/`,{})
                    .then((response) => {
                        if (response.status === 200) {
                            console.log(response.data)
                            this.details = response.data;
                        }
                    }).catch((error) => {
                    this.text = "Connection error";
                    console.log(error)
                    this.snackbar = true;
                });
            },
            showLogs(){
                if (!this.$refs.form.validate()) {
                    this.text = "Fill the data correctly";
                    this.snackbar = true
                }else{
                    axios.post(`${this.$hostname}/api/reports/`,{date:true,dateLt:this.dateLt,dateRt:this.dateRt,reseller:this.reseller})
                        .then((response) => {
                            if (response.status === 200) {
                                console.log(response.data)
                                this.details = response.data;
                                this.text = "Reseller info was displayed";
                                this.snackbar = true;
                            }
                        }).catch((error) => {
                        if(error.response.status === 400){
                            this.text = "Reseller does not exist";
                            console.log(error)
                            this.snackbar = true;
                        }else{
                            this.text = "Connection error";
                            console.log(error)
                            this.snackbar = true;
                        }
                    });
                }

            },
            showLogsSubscriber(){
                if (!this.$refs.subscriberForm.validate()) {
                    this.text = "Fill the data correctly";
                    this.snackbar = true
                }else{
                    axios.post(`${this.$hostname}/api/reports/`,{dateLt:this.dateLt,dateRt:this.dateRt,subscriber:this.subscriber})
                        .then((response) => {
                            if (response.status === 200) {
                                console.log(response.data)
                                this.details = response.data;
                                this.text = "Subscriber logs was displayed";
                                this.snackbar = true;
                            }
                        }).catch((error) => {
                            if(error.response.status === 400){
                                this.text = "Subscriber does not exist";
                                console.log(error)
                                this.snackbar = true;
                            }else{
                                this.text = "Connection error";
                                console.log(error)
                                this.snackbar = true;
                            }

                    });
                }

            },
            formatDate (date) {
                if (!date) return null

                const [year, month, day] = date.split('-')
                return `${month}/${day}/${year}`
            },
            parseDate (date) {
                if (!date) return null

                const [month, day, year] = date.split('/')
                return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
            },
        },
        computed: {

        },
        watch: {
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