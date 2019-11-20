<template>
    <div row justify-end>
        <v-dialog v-model="dialog" fullscreen hide-overlay transition="dialog-bottom-transition">
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
            <template v-slot:activator="{ on }">
                <v-btn
                        color="white"
                        fab
                        flat
                        dark
                        v-on="on">
                    <v-icon light>settings</v-icon>
                </v-btn>
            </template>
            <v-card>
                <v-toolbar dark color="primary" extended extension-height="4">
                    <v-btn icon dark @click="dialog = false">
                        <v-icon>close</v-icon>
                    </v-btn>
                    <v-toolbar-title>{{t('Settings')}}</v-toolbar-title>
                    <v-spacer></v-spacer>
                    <v-toolbar-items>
                        <v-btn dark flat @click="saveSettings">{{t('Save')}}</v-btn>
                        <!--<v-btn color="error" flat @click="dialog = false">Выйти</v-btn>-->
                    </v-toolbar-items>
                </v-toolbar>
                <template v-slot:extension>
                    <v-progress-linear slot="extension" v-show="loading" :indeterminate="true"
                                       class="px-0"
                                       color="secondary" height="4"></v-progress-linear>
                </template>
                <v-list three-line subheader v-if="selector">
                    <v-subheader>{{t('Language')}}</v-subheader>
                    <v-list-tile avatar>
                        <v-list-tile-content>
                            <v-select
                                    :items="[
                {'text': 'English', 'value': 'english'},
                {'text': 'Arabian', 'value': 'arabian'}
            ]"
                                    :label="t('Choose')"
                                    solo
                                    :rules="[rules.required]"
                                    v-model="language"
                            >
                                <template slot='selection' slot-scope='{ item }'>
                                    {{ t(item.text) }}
                                </template>
                                <template slot='item' slot-scope='{ item }'>
                                    {{ t(item.text) }}
                                </template>
                            </v-select>
                        </v-list-tile-content>
                    </v-list-tile>
                    <v-list-tile avatar>
                        <v-list-tile-content>
                            <v-text-field
                                    :label="t('Currency')"
                                    type="text"
                                    :rules="[rules.currency,rules.required]"
                                    v-model="currency"></v-text-field>
                        </v-list-tile-content>
                    </v-list-tile>

                </v-list>
                <v-divider></v-divider>
                <v-form ref="form">
                    <v-list three-line subheader>
                        <v-subheader>{{t('Payment')}}</v-subheader>
                        <v-list-tile avatar>
                            <v-list-tile-content>
                                <v-select
                                        :items="kind"
                                        :label="t('Choose')"
                                        solo
                                        :rules="[rules.required]"
                                        v-model="kind_payment"
                                >
                                    <template slot='selection' slot-scope='{ item }'>
                                        {{ t(item.text) }}
                                    </template>
                                    <template slot='item' slot-scope='{ item }'>
                                        {{ t(item.text) }}
                                    </template>
                                </v-select>
                            </v-list-tile-content>
                        </v-list-tile>
                        <v-list-tile avatar>
                            <v-list-tile-content>
                                <v-text-field
                                        :label="t('Currency')"
                                        type="text"
                                        :rules="[rules.currency,rules.required]"
                                        v-model="currency"></v-text-field>
                            </v-list-tile-content>
                        </v-list-tile>

                    </v-list>
                    <v-divider></v-divider>
                    <v-list three-line subheader>
                        <v-subheader>{{t('Payment period')}}</v-subheader>
                        <v-list-tile avatar>
                            <v-list-tile-content>
                                <v-select
                                        :items="period"
                                        :label="t('Choose')"
                                        solo
                                        :rules="[rules.required]"
                                        v-model="kind_period"
                                >
                                    <template slot='selection' slot-scope='{ item }'>
                                        {{ t(item.text) }}
                                    </template>
                                    <template slot='item' slot-scope='{ item }'>
                                        {{ t(item.text) }}
                                    </template>
                                </v-select>
                            </v-list-tile-content>
                        </v-list-tile>
                        <v-list-tile avatar>
                            <v-list-tile-content>
                                <v-text-field
                                        :label="t('Quantity (of payment period)')"
                                        v-model="numberOfPeriod"
                                        type="number" required
                                        :rules="[rules.counter, rules.number]"
                                ></v-text-field>
                            </v-list-tile-content>
                        </v-list-tile>
                    </v-list>


                    <v-divider></v-divider>
                    <v-subheader>{{t('Server preferences:')}}</v-subheader>
                    <v-layout
                            wrap
                            px-3
                    >
                        <v-flex sm3 pr-3>
                            <v-text-field
                                    :label="t('Cards prefix')"
                                    type="number"
                                    :rules="[rules.rrrCounter,rules.number,rules.required]"
                                    v-model="sssss"></v-text-field>
                        </v-flex>
                        <v-flex sm3 pr-3>
                            <v-text-field
                                    :label="t('Max cards')"
                                    type="number"
                                    :rules="[rules.cardCounter,rules.number,rules.required]"
                                    v-model="max_cards"></v-text-field>
                        </v-flex>
                        <v-flex sm3 pr-3>
                            <v-text-field
                                    :label="t('Server ip')"
                                    type="text"
                                    :rules="[rules.ipAddress,rules.required]"
                                    v-model="server_ip"></v-text-field>
                        </v-flex>
                        <v-flex sm3 pr-3>
                            <v-text-field
                                    :label="t('Server port')"
                                    type="number"
                                    :rules="[rules.portCounter,rules.number,rules.required]"
                                    v-model="server_port"></v-text-field>
                        </v-flex>
                    </v-layout>
                </v-form>
                <v-divider></v-divider>
                <v-list three-line subheader>
                    <v-subheader>{{t('Bouquets')}}</v-subheader>
                    <v-list-tile avatar>
                        <v-list-tile-content class="no-flex">
                            <v-form ref="formBouquets">
                                <v-text-field
                                        :label="t('Bouquets')"
                                        type="number"
                                        :rules="[rules.bouquetsCounter]"
                                        v-model="numOfBouquets"
                                ></v-text-field>
                            </v-form>
                        </v-list-tile-content>
                        <v-list-tile-avatar>
                            <v-btn
                                    color="primary"
                                    dark
                                    small
                                    ripple
                                    icon
                                    class="mr-auto"
                                    @click="updateBouquets"
                            >
                                <v-icon small>autorenew</v-icon>
                            </v-btn>
                        </v-list-tile-avatar>
                    </v-list-tile>
                </v-list>
                <v-list three-line subheader>
                    <v-subheader>{{t('Synchronization')}}</v-subheader>
                    <v-list-tile avatar>
                        <v-list-tile-content class="no-flex">
                            <v-form ref="formBouquets">
                                <v-text-field
                                        :label="t('Periods quantity')"
                                        type="number"
                                        :rules="[rules.counterUpdatePeriods]"
                                        v-model="counterUpdatePeriods"
                                ></v-text-field>
                            </v-form>
                        </v-list-tile-content>
                    </v-list-tile>
                </v-list>
                <v-subheader>{{t('Synchronization at:')}}</v-subheader>
                <v-layout
                        wrap
                        px-3
                >
                    <v-flex sm3 pr-3 v-for="(period,key) in serverPeriods" :key="key">
                        <h3 class="subheading">{{period.value}}</h3>
                    </v-flex>
                </v-layout>
                <v-subheader>{{t('New synchronization periods:')}}</v-subheader>
                <v-form class="w-100 px-3" ref="formPeriods" @submit.prevent="synchronize()">
                    <v-layout
                            wrap
                    >
                        <v-flex sm3 pr-3 v-for="(period,key) in counterUpdatePeriodsArray" :key="key">
                            <v-menu
                                    :id="'menu'+key"
                                    v-model="updatePeriodsArray[key].isOpen"
                                    :close-on-content-click="false"
                                    :nudge-right="40"
                                    :return-value.sync="updatePeriodsArray[key].value"
                                    transition="scale-transition"
                                    offset-y
                                    full-width
                                    max-width="290px"
                                    min-width="290px"
                            >
                                <template v-slot:activator="{ on }">
                                    <v-text-field
                                            v-model="updatePeriodsArrayHack[key].value"
                                            :label="t('Period') + ' ' + (key+1)"
                                            prepend-icon="access_time"
                                            readonly
                                            v-on="on"
                                    ></v-text-field>
                                </template>
                                <v-time-picker
                                        format="24hr"
                                        v-if="updatePeriodsArray[key].isOpen"
                                        v-model="updatePeriodsArray[key].value"
                                        full-width
                                        @click:minute="updatePeriodsArrayHack[key].value = updatePeriodsArray[key].value"
                                ></v-time-picker>
                            </v-menu>
                        </v-flex>
                    </v-layout>
                </v-form>

            </v-card>
        </v-dialog>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        data: () => ({
            dialog: false,
            snackbar: false,
            text: 'Oops... Something went wrong',
            timeout: 5000,
            loading: true,
            selector:false,
            language: localStorage.currentLanguage,
            kind: [
                {'text': 'Virtual balance', 'value': 'VIRTUAL'},
                {'text': 'Prepayment', 'value': 'PREPAYMENT'}
            ],
            currency: '',
            period: [
                {'text': 'Days', 'value': 'DAYS'},
                {'text': 'Weeks', 'value': 'WEEKS'},
                {'text': 'Months', 'value': 'MONTHS'}
                ],
            updatePeriodsArray: [{}, {}, {}, {}, {}, {}, {}, {}],
            updatePeriodsArrayHack: [{}, {}, {}, {}, {}, {}, {}, {}],
            counterUpdatePeriods: 1,
            serverPeriods: [],
            kind_payment: '',
            kind_period: '',
            numberOfPeriod: 1,
            max_cards: 0,
            server_ip: '',
            server_port: '',
            rules: {
                required: value => !!value || this.$translate.locale['Required.'],
                counter: value => value <= 100 || this.$translate.locale['Max 100'],
                currency: value => value.length <= 100 || this.$translate.locale["Max 100 characters"],
                counterUpdatePeriods: value => (value <= 8 && value >= 1) || this.$translate.locale['Min 1 Max 8'],
                bouquetsCounter: value => (value <= 128 && value >= 1) || this.$translate.locale['Min 1 Max 128'],
                number: value => {
                    const pattern = /^\d+$/;
                    return pattern.test(value) || this.$translate.locale['Invalid number.']
                },
                rrrCounter: value => (value <= 99999 && value >= 0 && value.length <= 5) || this.$translate.locale['Min 0 Max 99999'],
                cardCounter: value => (value <= 100000 && value >= 0) || this.$translate.locale['Min 0 Max 100000'],
                ipAddress: value => {
                    const pattern = /^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/;
                    return pattern.test(value) || this.$translate.locale['Invalid id address']
                },
                portCounter: value => (value <= 65535 && value >= 0) || this.$translate.locale['Min 0 Max 65535'],
            },
            sssss: '00000',
            numOfBouquets: 1,
        }),
        computed: {
            counterUpdatePeriodsArray() {
                if (this.counterUpdatePeriods < 1) {
                    return new Array(1)
                } else if (this.counterUpdatePeriods > 8) {
                    return new Array(8)
                } else {
                    return new Array(Number.parseInt(this.counterUpdatePeriods))
                }
            },
            ssssWithZeros() {
                if (this.sssss < 10 && this.sssss.length < 2) {
                    return '0000' + this.sssss
                } else if (this.sssss < 100 && this.sssss.length < 3) {
                    return '000' + this.sssss
                } else if (this.sssss < 1000 && this.sssss.length < 4) {
                    return '00' + this.sssss
                } else if (this.sssss < 10000 && this.sssss.length < 5) {
                    return '0' + this.sssss
                } else {
                    return this.sssss.toString()
                }
            }
        },
        methods: {

            getData() {
                // this.loadingSettings = true;
                this.loading = true;
                axios.get(`${this.$hostname}/api/settings/`)
                    .then((response) => {
                        if (response.status === 200) {
                            this.kind_payment = response.data.kind_payment;
                            this.currency = response.data.currency;
                            this.kind_period = response.data.kind_period;
                            this.numberOfPeriod = response.data.quantity;
                            this.sssss = response.data.sssss;
                            this.max_cards = response.data.max_cards;
                            this.server_ip = response.data.server_ip;
                            this.server_port = response.data.server_port;
                            console.log(response.data)
                            this.serverPeriods = response.data.periods;
                            this.loading = false;
                            this.$store.commit('set', {
                                type: 'isPREPAYMENT',
                                items: this.kind_payment === 'PREPAYMENT'
                            });
                            this.$store.commit('set', {
                                type: 'currency',
                                items: this.currency
                            });
                        }
                    }).catch((error) => {
                    this.text = "Connection error";
                    this.snackbar = true;
                });
            },
            saveSettings() {
                if (!this.$refs.form.validate()) {
                    this.text = "Fill the form correctly";
                    this.snackbar = true;
                } else {
                    this.loading = true;
                    axios.put(`${this.$hostname}/api/change-settings/`, {
                        kind_payment: this.kind_payment,
                        currency: this.currency,
                        kind_period: this.kind_period,
                        quantity: this.numberOfPeriod,
                        sssss: this.ssssWithZeros,
                        max_cards: this.max_cards,
                        server_ip: this.server_ip,
                        server_port: this.server_port,
                    })
                        .then((response) => {
                            if (response.status === 200) {
                                this.getData();
                                this.text = "Settings changed!";
                                this.snackbar = true;
                                this.dialog = false;
                                this.loading = false;
                                this.$router.push('/dashboard');
                            }
                        }).catch((error) => {
                        this.text = "Connection error";
                        console.log(error)
                        this.snackbar = true;
                        this.dialog = false;
                    });
                    this.synchronize();
                }
            },
            updateBouquets() {
                if (!this.$refs.formBouquets.validate()) {
                    this.text = "Fill the number of bouquets correctly";
                    this.snackbar = true;
                } else {
                    axios.get(`${this.$hostname}/api/download/${this.numOfBouquets}/`)
                        .then((response) => {
                            if (response.status === 200) {
                                this.getData();
                                this.text = "Bouquets updated!";
                                this.snackbar = true;
                                this.dialog = false;
                                this.$router.push('/dashboard');
                            }
                        }).catch((error) => {
                        this.text = "Connection error";
                        console.log(error)
                        this.snackbar = true;
                    })
                }
            },
            synchronize() {
                if (!this.$refs.formPeriods.validate()) {
                    this.text = "Fill the periods correctly";
                    this.snackbar = true;
                } else {
                    axios.post(`${this.$hostname}/api/synchronize/`, {periods: this.updatePeriodsArrayHack})
                        .then((response) => {
                            if (response.status === 200) {
                                this.getData();
                                this.text = "Periods updated!";
                                this.snackbar = true;
                                this.dialog = false;
                                this.$router.push('/dashboard');
                            }
                        }).catch((error) => {
                        this.text = "Connection error";
                        console.log(error)
                        this.snackbar = true;
                    })
                }
            }
        },
        beforeMount() {
            axios.defaults.headers.common['Authorization'] = 'Token ' + this.$session.get('jwt');
            this.getData();
            this.language = localStorage.currentLanguage;


        },
        mounted(){
            window.$languages = JSON.parse(document.getElementById('config').innerHTML);
            this.selector = window.$languages.selector;
        },
        watch: {
            language: {
                handler(newValue) {
                    console.log(newValue)
                    window.$currentLanguage = newValue;
                    localStorage.currentLanguage = newValue;
                    this.$translate.setLang(window.$currentLanguage);
                    this.$vuetify.rtl = window.$languages.locale[window.$currentLanguage].rtl

                },
                immediate: true,
            }
        },
    }
</script>

<style scoped>
    .no-flex {
        flex: initial;
    }
</style>
