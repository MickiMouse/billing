<template>
    <div row justify-end>
        <v-dialog v-model="dialog" fullscreen hide-overlay transition="dialog-bottom-transition">
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
                    <v-toolbar-title>Settings</v-toolbar-title>
                    <v-spacer></v-spacer>
                    <v-toolbar-items>
                        <v-btn dark flat @click="saveSettings">Save</v-btn>
                        <!--<v-btn color="error" flat @click="dialog = false">Выйти</v-btn>-->
                    </v-toolbar-items>
                </v-toolbar>
                <template v-slot:extension>
                    <v-progress-linear slot="extension" v-show="loading" :indeterminate="true"
                                       class="px-0"
                                       color="secondary" height="4"></v-progress-linear>
                </template>
                <v-form ref="form">
                    <v-list three-line subheader>
                        <v-subheader>Payment</v-subheader>
                        <v-list-tile avatar>
                            <v-list-tile-content>
                                <v-select
                                        :items="kind"
                                        label="Choose"
                                        solo
                                        :rules="[rules.required]"
                                        v-model="kind_payment"
                                ></v-select>
                            </v-list-tile-content>
                        </v-list-tile>

                    </v-list>
                    <v-divider></v-divider>
                    <v-list three-line subheader>
                        <v-subheader>Payment period</v-subheader>
                        <v-list-tile avatar>
                            <v-list-tile-content>
                                <v-select
                                        :items="period"
                                        label="Choose"
                                        solo
                                        :rules="[rules.required]"
                                        v-model="kind_period"
                                ></v-select>
                            </v-list-tile-content>
                        </v-list-tile>
                        <v-list-tile avatar>
                            <v-list-tile-content>
                                <v-text-field
                                        label="Quantity (of payment period)"
                                        v-model="numberOfPeriod"
                                        type="number" required
                                        :rules="[rules.counter, rules.number]"
                                ></v-text-field>
                            </v-list-tile-content>
                        </v-list-tile>
                    </v-list>

                </v-form>
                <v-divider></v-divider>
                <v-list three-line subheader>
                    <v-subheader>Bouquets</v-subheader>
                    <v-list-tile avatar>
                        <v-list-tile-content  class="no-flex">
                            <v-text-field
                                    label="Bouquets"
                                    type="number"
                                    :rules="[rules.counter, rules.bouquetsCounter]"
                                    v-model="numOfBouquets"
                            ></v-text-field>
                        </v-list-tile-content>
                        <v-list-tile-avatar>
                            <v-btn
                                    color="pink"
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
            </v-card>
        </v-dialog>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        data: () => ({
            dialog: false,
            snackbar:false,
            text: 'Oops... Something went wrong',
            timeout: 5000,
            loading: true,
            kind: [{'text': 'Virtual balance', 'value': 'VIRTUAL'}, {
                'text': 'Prepayment',
                'value': 'PREPAYMENT'
            }],
            period: [{'text': 'Days', 'value': 'DAYS'}, {'text': 'Weeks', 'value': 'WEEKS'}, {
                'text': 'Months',
                'value': 'MONTHS'
            }],
            kind_payment:'',
            kind_period:'',
            numberOfPeriod: 1,
            rules: {
                required: value => !!value || 'Required.',
                counter: value => value <= 100 || 'Max 100',
                bouquetsCounter: value => (value <= 128 && value >= 1) || 'Min 1 Max 128',
                number: value => {
                    const pattern = /^\d+$/;
                    return pattern.test(value) || 'Invalid number.'
                },
            },
            numOfBouquets: 1,
        }),
        methods:{
            getData() {
                // this.loadingSettings = true;
                this.loading = true;
                axios.get(`${this.$hostname}/api/settings/`)
                    .then((response) => {
                        if (response.status === 200) {
                            this.kind_payment = response.data.kind_payment;
                            this.kind_period = response.data.kind_period;
                            this.numberOfPeriod = response.data.quantity;
                            console.log(response.data)
                            this.loading = false;
                            this.$store.commit('set',{type: 'isPREPAYMENT', items: this.kind_payment === 'PREPAYMENT'});
                        }
                    }).catch((error) => {
                    this.text = "Connection error";
                    console.log(error)
                    this.snackbar = true;
                });
            },
            saveSettings(){
                if (!this.$refs.form.validate()) {
                    this.text = "Fill the form correctly";
                    this.snackbar = true;
                }else{
                    this.loading = true;
                    axios.put(`${this.$hostname}/api/change-settings/`, {kind_payment: this.kind_payment,kind_period: this.kind_period, quantity: this.numberOfPeriod})
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
                    })
                }
            },
            updateBouquets(){}
        },
        beforeMount(){
            axios.defaults.headers.common['Authorization'] = 'Token ' + this.$session.get('jwt');
            this.getData();
        }
    }
</script>

<style scoped>
    .no-flex{
        flex: initial;
    }
</style>