<template>
    <v-content color="primary">
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
        <v-container fluid id="main-container" grid-list-md>
            <v-layout row wrap>
                <v-flex xs12 justify-center>
                    <v-form @submit.prevent="showLogs" ref="form">
                        <v-card class="px-3 mb-3 pb-3">
                            <v-row class="d-flex">
                                <v-col cols="6" lg="6" class="mr-5">
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
                                                    :label="t('From')"
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
                                <v-col cols="6" lg="6">
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
                                                    :label="t('To')"
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
                    </v-form>
                </v-flex>
                <v-flex xs12>
                    <v-tabs grow @change="tabValue != 'report-logs' ? getData() : ''" v-model="tabValue">
                        <v-tab href="#report-subs">
                            <v-icon left>mdi-account</v-icon>
                            {{t('Subscribers')}}
                        </v-tab>
                        <v-tab href="#report-card">
                            <v-icon left>mdi-lock</v-icon>
                            {{t('Cards')}}
                        </v-tab>
                        <v-tab href="#report-finance">
                            <v-icon left>mdi-access-point</v-icon>
                           {{t('Finance')}}
                        </v-tab>
                        <v-tab href="#report-logs">
                            <v-icon left>mdi-access-point</v-icon>
                            {{t('Logs')}}
                        </v-tab>
                        <v-tab href="#report-cards-reseller">
                            <v-icon left>mdi-access-point</v-icon>
                            {{t('Reseller cards')}}
                        </v-tab>
                        <v-tab-item value="report-subs">
                            <reports-subscribers :data="details.objects" :loading="loading" :total="details.total" :kind="t('subscribers')"/>
                        </v-tab-item>
                        <v-tab-item value="report-card">
                            <reports-subscribers :data="details.objects" :loading="loading" :total="details.total" :kind="t('cards of subscribers')"/>
                        </v-tab-item>
                        <v-tab-item value="report-finance">
                            <reports-subscribers :data="details.objects" :loading="loading" :total="details.total" :kind="t('finance')"/>

                        </v-tab-item>
                        <v-tab-item value="report-logs">
                            <reports-subscriber-logs :dateLt="dateLt" :dateRt="dateRt"/>
                        </v-tab-item>
                        <v-tab-item value="report-cards-reseller">
                            <reports-reseller :data="details.objects" :loading="loading" :total="details.total" :kind="t('cards')"/>

                        </v-tab-item>
                    </v-tabs>
                </v-flex>

            </v-layout>
        </v-container>

    </v-content>

</template>

<script>
    import axios from 'axios';
    import ReportsSubscribers from "../../components/Reports/ReportsSubscribers";
    import ReportsReseller from "../../components/Reports/ReportsReseller";
    import ReportsSubscriberLogs from "../../components/Reports/ReportsSubscriberLogs";


    export default {
        name: "Reports",
        components: {ReportsSubscriberLogs, ReportsReseller, ReportsSubscribers},
        data: vm => ({
            dateLt: '',
            dateRt: '',
            dateFormatted: vm.formatDate(new Date().toISOString().substr(0, 10)),
            tabValue: 'report-subs',
            menu1: false,
            menu2: false,
            details:[],
            reseller:'',
            searchLogs: '',
            subscriber:'',
            loading: true,
            snackbar: false,
            text: 'Oops... Something went wrong',
            timeout: 5000,
            // headersLogs: [
            //     {text: 'Date', value: 'date'},
            //     {
            //         text: 'Header',
            //         align: 'left',
            //         //  sortable: false,
            //         value: 'log',
            //     },
            //
            //     // {text: 'Calories', value: 'calories'},
            // ],
            rules: {
                required: value => !!value || this.$translate.locale['Required.'],
                username: value => (value.length >= 4 && value.length <= 150) ||this.$translate.locale[ 'Username between the 4 - 150 characters'],
                counter: value => value.length >= 8 || this.$translate.locale['Min 8 characters'],
                email: value => {
                    const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
                    return pattern.test(value) || this.$translate.locale['Invalid e-mail.']
                },
            },
        }),
        methods:{
            getData(){
                this.loading = true;
                axios.post(`${this.$hostname}/api/${this.tabValue}/`,{dateLt:this.dateLt,dateRt:this.dateRt,reseller:this.reseller})
                    .then((response) => {
                        if (response.status === 200) {
                            console.log(response.data)
                            this.details = response.data;
                            this.loading = false;
                        }
                    }).catch((error) => {
                    if(error.response.status === 400){
                        this.text = "Incorrect data";
                        console.log(error)
                        this.snackbar = true;
                    }else{
                        this.text = "Connection error";
                        console.log(error)
                        this.snackbar = true;
                    }
                });
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
            dateLt: function () {
                if(this.dateLt && this.dateRt){
                    this.getData();
                }
            },
            dateRt: function () {
                if(this.dateLt && this.dateRt){
                    this.getData();
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

<style scoped>

</style>