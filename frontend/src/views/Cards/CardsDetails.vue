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
                                <v-dialog v-if="this.details.status !== 'Active'" v-model="deleteDialog" max-width="290">
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
                                            <v-btn outline small color="error" @click="deleteSubscriber">{{t('Delete')}}</v-btn>
                                        </v-card-actions>
                                    </v-card>
                                </v-dialog>
                            </v-subheader>
                            <v-list-tile
                                    avatar
                                    @click=""
                            >
                                <v-list-tile-avatar>
                                    <v-icon class="grey lighten-1 white--text">folder_special</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>{{t('Label')}}</v-list-tile-title>
                                    <v-list-tile-sub-title>{{details.label}}
                                    </v-list-tile-sub-title>
                                </v-list-tile-content>
                            </v-list-tile>
                            <v-list-tile
                                    avatar
                                    @click=""
                            >
                                <v-list-tile-avatar>
                                    <v-icon class="grey lighten-1 white--text">playlist_add_check</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>{{t('Status')}}</v-list-tile-title>
                                    <v-list-tile-sub-title>{{t(details.status)}}</v-list-tile-sub-title>
                                </v-list-tile-content>
                                <v-list-tile-avatar>
                                    <v-switch
                                            v-model="status"
                                            @change="updateStatus"
                                            :disabled="details.status !== 'Active' && details.status !== 'Suspend'"
                                    ></v-switch>
                                </v-list-tile-avatar>
                            </v-list-tile>
                            <v-list-tile
                                    avatar
                                    @click=""
                            >
                                <v-list-tile-avatar>
                                    <v-icon class="grey lighten-1 white--text">account_balance_wallet</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>{{t('Price')}}</v-list-tile-title>
                                    <v-list-tile-sub-title>{{details.price + $store.getters.currency}}</v-list-tile-sub-title>
                                </v-list-tile-content>
                            </v-list-tile>
                            <v-list-tile
                                    avatar
                                    @click=""
                            >
                                <v-list-tile-avatar>
                                    <v-icon class="grey lighten-1 white--text">event_busy</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>{{t('Expired date')}}</v-list-tile-title>
                                    <v-list-tile-sub-title>{{details.expired_date}}</v-list-tile-sub-title>
                                </v-list-tile-content>
                                <div :class="{'d-none': $vuetify.breakpoint.xs, '': $vuetify.breakpoint.smAndUp}"
                                     class="d-flex align-center justify-center"
                                     v-if="$store.getters.isPREPAYMENT && details.status !== 'Inactive'">
                                    <v-form ref="form">
                                        <v-text-field
                                                :label="t('Periods')"
                                                class="mr-2 ml-auto"
                                                type="number"
                                                :rules="[rules.counter, rules.number]"
                                                v-model="numOfPeriods"
                                        ></v-text-field>


                                    </v-form>
                                    <v-btn
                                            color="pink"
                                            dark
                                            small
                                            ripple
                                            icon
                                            class="ml-auto"
                                            @click="updateCardPeriod"
                                    >
                                        <v-icon small>autorenew</v-icon>
                                    </v-btn>
                                </div>
                            </v-list-tile>
                            <v-list-tile avatar
                                         :class="{'': $vuetify.breakpoint.xs, 'd-none': $vuetify.breakpoint.smAndUp}"
                                         v-if="$store.getters.isPREPAYMENT && details.status !== 'Inactive'">
                                <div class="d-flex align-center justify-center">
                                    <v-form ref="form">
                                        <v-text-field
                                                :label="t('Periods')"
                                                class="mr-2 ml-auto"
                                                type="number"
                                                :rules="[rules.counter, rules.number]"
                                                v-model="numOfPeriods"
                                        ></v-text-field>


                                    </v-form>
                                    <v-btn
                                            color="pink"
                                            dark
                                            small
                                            ripple
                                            icon
                                            class="ml-auto"
                                            @click="updateCardPeriod"
                                    >
                                        <v-icon small>autorenew</v-icon>
                                    </v-btn>
                                </div>
                            </v-list-tile>
                            <v-list-tile
                                    avatar
                                    @click=""
                            >
                                <v-list-tile-avatar>
                                    <v-icon class="grey lighten-1 white--text">event_note</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>{{t('Last change')}}</v-list-tile-title>
                                    <v-list-tile-sub-title>{{details.last_change}}</v-list-tile-sub-title>
                                </v-list-tile-content>
                            </v-list-tile>
                            <v-list-tile
                                    avatar
                                    @click=""
                            >
                                <v-list-tile-avatar>
                                    <v-icon class="grey lighten-1 white--text">insert_invitation</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>{{t('Created at')}}</v-list-tile-title>
                                    <v-list-tile-sub-title>{{details.created_at}}</v-list-tile-sub-title>
                                </v-list-tile-content>
                            </v-list-tile>
                            <v-list-tile
                                    avatar
                                    @click=""
                                    v-if="details.subscriber"
                            >
                                <v-list-tile-avatar>
                                    <v-icon class="grey lighten-1 white--text">person</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>{{t('Subscriber')}}</v-list-tile-title>
                                    <v-list-tile-sub-title>{{details.subscriber.email}}</v-list-tile-sub-title>
                                </v-list-tile-content>
                                <v-list-tile-avatar>
                                    <v-tooltip bottom>
                                        <template v-slot:activator="{ on }">
                                            <v-btn v-on="on" :to="`/subscribers/${details.subscriber.pk}/details/`"
                                                   color="info" ripple icon small dark>
                                                <v-icon small>info</v-icon>
                                            </v-btn>
                                        </template>
                                        <span>{{t('Detail')}}</span>
                                    </v-tooltip>
                                </v-list-tile-avatar>
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
                                <v-list-tile-avatar>
                                    <v-tooltip bottom>
                                        <template v-slot:activator="{ on }">
                                            <v-btn v-on="on" :to="`/resellers/${details.reseller.pk}/details/`"
                                                   color="info" ripple icon small dark>
                                                <v-icon small>info</v-icon>
                                            </v-btn>
                                        </template>
                                        <span>{{t('Detail')}}</span>
                                    </v-tooltip>
                                </v-list-tile-avatar>
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
                                {{t('Elements')}} {{item.pageStart}} - {{item.pageStop}}, {{t('total')}}: {{item.itemsLength}}
                            </template>
                            <template slot="no-data">
                                <v-subheader>{{t('No data available')}}</v-subheader>
                            </template>
                        </v-data-table>
                    </v-card>
                </v-flex>
                <v-flex xs12 sm4>
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
                        <v-subheader>{{t('Packages')}}</v-subheader>
                        <v-data-table
                                :headers="headers"
                                :items="packages"
                                items-per-page="5"
                                class="elevation-1"
                                :loading="loadingPackages"
                                :search="search"
                                :rows-per-page-text="t('Rows per page')"
                                :rows-per-page-items='[10,25, 50, {text: $translate.locale["All"], value: -1}]'
                        >
                            <template slot="items" slot-scope="props">
                                <td class="text-xs-left no-wrap">
                                    {{ props.item.header }}
                                    <v-tooltip bottom v-if="props.item.delayed">
                                        <template v-slot:activator="{ on }">
                                            <v-icon small v-on="on" color="warning">add_alarm</v-icon>
                                        </template>
                                        <span>{{t('This package will be removed on the next transaction.')}} </span>
                                    </v-tooltip>
                                </td>
                                <td class="text-xs-left no-wrap">{{ props.item.tariff + $store.getters.currency}}</td>
                                <td class="text-xs-left no-wrap">
                                    <v-tooltip bottom>
                                        <template v-slot:activator="{ on }">
                                            <v-btn v-on="on" :to="`/packages/${props.item.pk}/details/`" color="info"
                                                   ripple icon small dark>
                                                <v-icon small>info</v-icon>
                                            </v-btn>
                                        </template>
                                        <span>{{t('Detail')}}</span>
                                    </v-tooltip>
                                    <v-tooltip bottom>
                                        <template v-slot:activator="{ on }">
                                            <v-btn v-on="on" color="error" @click="removeCard(props.item.pk)" ripple
                                                   icon small dark>
                                                <v-icon small>close</v-icon>
                                            </v-btn>
                                        </template>
                                        <span>{{t('Remove now')}}</span>
                                    </v-tooltip>
                                    <v-tooltip bottom v-if="!props.item.delayed">
                                        <template v-slot:activator="{ on }">
                                            <v-btn v-on="on" color="error darken-1" @click="removeCardLater(props.item.pk)" ripple
                                                   icon small dark>
                                                <v-icon small>alarm_off</v-icon>
                                            </v-btn>
                                        </template>
                                        <span>{{t('Remove later')}}</span>
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
                    <v-card class="my-3" v-if="this.details.status !== 'Inactive'">
                        <v-subheader>{{t('Available packages')}}</v-subheader>
                        <v-data-table
                                :headers="headers"
                                :items="aviablePackages"
                                items-per-page="5"
                                class="elevation-1"
                                :loading="loadingAviablePackages"
                                :search="search"
                                :rows-per-page-text="t('Rows per page')"
                                :rows-per-page-items='[10,25, 50, {text: $translate.locale["All"], value: -1}]'
                        >
                            <template slot="items" slot-scope="props">
                                <td class="text-xs-left no-wrap">
                                    {{ props.item.header }}
                                    <v-tooltip bottom v-if="props.item.delayed">
                                        <template v-slot:activator="{ on }">
                                            <v-icon small v-on="on" color="warning">add_alarm</v-icon>
                                        </template>
                                        <span>{{t('This package will be added in the next transaction.')}} </span>
                                    </v-tooltip>
                                </td>
                                <td class="text-xs-left no-wrap">{{ props.item.tariff + $store.getters.currency}}</td>
                                <td class="text-xs-left no-wrap">
                                    <v-tooltip bottom>
                                        <template v-slot:activator="{ on }">
                                            <v-btn v-on="on" :to="`/packages/${props.item.pk}/details/`" color="info"
                                                   ripple icon small dark>
                                                <v-icon small>info</v-icon>
                                            </v-btn>
                                        </template>
                                        <span>{{t('Detail')}}</span>
                                    </v-tooltip>
                                    <v-tooltip bottom>
                                        <template v-slot:activator="{ on }">
                                            <v-btn v-on="on" @click="addPackage(props.item.pk)" color="success" ripple
                                                   icon small dark>
                                                <v-icon small>add</v-icon>
                                            </v-btn>
                                        </template>
                                        <span>{{t('Add now')}}</span>
                                    </v-tooltip>
                                    <v-tooltip bottom v-if="!props.item.delayed">
                                        <template v-slot:activator="{ on }">
                                            <v-btn v-on="on" @click="addPackageLater(props.item.pk)"
                                                   color="success darken-1" ripple
                                                   icon small dark>
                                                <v-icon small>add_alarm</v-icon>
                                            </v-btn>
                                        </template>
                                        <span>{{t('Add later')}}</span>
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
                </v-flex>
            </v-layout>
        </v-container>
    </v-content>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "CardsDetails",
        data() {
            return {
                snack: false,
                snackColor: '',
                snackText: '',
                loading: true,
                loadingPackages: true,
                loadingAviablePackages: true,
                snackbar: false,
                dialog: false,
                search: '',
                searchLogs:'',
                text: 'Oops... Something went wrong',
                timeout: 5000,
                newBalance: '',
                numOfPeriods: 1,
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
                        text: this.$translate.locale['Header'],
                        align: 'left',
                        //  sortable: false,
                        value: 'header',
                    },
                    {
                        text: this.$translate.locale['Tariff'],
                        align: 'left',
                        //  sortable: false,
                        value: 'tariff',
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
                packages: [],
                aviablePackages: [],
                rules: {
                    counter: value => (value <= 2147483647 && value >= 1) || this.$translate.locale['Min 1 and Max 2147483647'],
                    number: value => {
                        const pattern = /^\d+$/;
                        return pattern.test(value) || this.$translate.locale['Invalid number.']
                    },
                },
                deleteDialog: false,
            }
        },
        computed: {
            status(){
                return this.details.status === 'Active';
            }
        },
        methods: {
            getData() {
                this.loadingPackages = true;
                axios.get(`${this.$hostname}/api/cards/${this.$route.params.id}/`)
                    .then((response) => {
                        if (response.status === 200) {
                            console.log(response.data)
                            this.details = response.data;
                            this.packages = this.details.packages;
                            this.newBalance = this.details.balance;
                            this.loadingPackages = false;
                            console.log(response.data)
                        }
                    }).catch((error) => {
                    this.text = "Connection error";
                    console.log(error)
                    this.snackbar = true;
                });
                this.loadingAviablePackages = true;
                axios.get(`${this.$hostname}/api/packages-filter/${this.$route.params.id}/`)
                    .then((response) => {
                        if (response.status === 200) {
                            this.aviablePackages = response.data;
                            this.loadingAviablePackages = false;
                            console.log(response.data)
                        }
                    }).catch((error) => {
                    this.text = "Connection error";
                    console.log(error)
                    this.snackbar = true;
                });
            },
            updateStatus() {
                axios.put(`${this.$hostname}/api/cards/edit/status/${this.$route.params.id}/`)
                    .then((response) => {
                        if (response.status === 200) {
                            this.getData();
                            this.text = "Status changed!";
                            this.snackbar = true;
                        }
                    }).catch((error) => {
                    this.details.status = !this.details.status;
                    this.text = "Connection error";
                    console.log(error)
                    this.snackbar = true;
                })
            },
            updateCardPeriod() {
                if (!this.$refs.form.validate()) {
                    this.text = "Fill the form correctly";
                    this.snackbar = true;
                } else {
                    this.loading = true;
                    axios.put(`${this.$hostname}/api/cards/edit/expired/${this.$route.params.id}/`, {period: Number.parseInt(this.numOfPeriods)})
                        .then((response) => {
                            if (response.status === 200) {
                                this.getData();
                                this.text = "Period changed!";
                                this.snackbar = true;
                            }
                        }).catch((error) => {
                        this.text = "Connection error";
                        console.log(error)
                        this.snackbar = true;
                    });
                }
            },
            addPackage(pk) {
                axios.put(`${this.$hostname}/api/cards/edit/package/${this.$route.params.id}/`, {package: pk})
                    .then((response) => {
                        if (response.status === 200) {
                            console.log(response.data);
                            this.getData();
                        }
                    }).catch((error) => {
                    if (error.response.status === 400) {
                        this.details.status = !this.details.status;
                        this.text = "The subscriber does not have enough funds";
                        console.log(error)
                        this.snackbar = true;
                    } else {
                        this.details.status = !this.details.status;
                        this.text = "Connection error";
                        console.log(error)
                        this.snackbar = true;
                    }
                });
            },
            addPackageLater(pk) {
                axios.post(`${this.$hostname}/api/cards/delayed-add/package/${this.$route.params.id}/`, {package: pk})
                    .then((response) => {
                        if (response.status === 200) {
                            console.log(response.data);
                            this.getData();
                        }
                    }).catch((error) => {
                    if (error.response.status === 400) {
                        this.details.status = !this.details.status;
                        this.text = "The subscriber does not have enough funds";
                        console.log(error)
                        this.snackbar = true;
                    } else {
                        this.details.status = !this.details.status;
                        this.text = "Connection error";
                        console.log(error)
                        this.snackbar = true;
                    }
                });
            },
            removeCard(pk) {
                axios.put(`${this.$hostname}/api/cards/delete/package/${this.$route.params.id}/`, {package: pk})
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
            removeCardLater(pk) {
                axios.post(`${this.$hostname}/api/cards/delayed-remove/package/${this.$route.params.id}/`, {package: pk})
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
            // deleteSubscriber() {
            //     axios.delete(`${this.$hostname}/api/cards/delete/${this.$route.params.id}/`)
            //         .then((response) => {
            //             if (response.status === 200) {
            //                 console.log(response.data);
            //                 this.$router.push('/subscribers')
            //             }
            //         }).catch((error) => {
            //         this.text = "Connection error";
            //         console.log(error)
            //         this.snackbar = true;
            //     });
            // },
            deleteSubscriber() {

                axios.delete(`${this.$hostname}/api/cards/delete/${this.$route.params.id}/`)
                    .then((response) => {
                        if (response.status === 204) {
                            console.log(response.data);
                            this.$router.push('/cards')
                        }
                    }).catch((error) => {
                        if(error.response.status === 400){
                            this.text = "3 days passed";
                            console.log(error)
                            this.snackbar = true;
                        }else{
                            this.text = "Connection error";
                            console.log(error)
                            this.snackbar = true;
                        }
                });
            },
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
