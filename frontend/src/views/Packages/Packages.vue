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
            <v-layout row wrap justify-center class="d-inline-block w-100 mb-5">
                <v-card>
                    <v-card-title>
                        {{t('Packages')}}
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
                            :items="packages"
                            :items-per-page="5"
                            class="elevation-1"
                            :loading="loading"
                            :search="search"
                            :rows-per-page-text="t('Rows per page')"
                            :rows-per-page-items='[10,25, 50, {text: $translate.locale["All"], value: -1}]'
                    >
                        <template slot="items" slot-scope="props">
                            <td class="text-xs-left">{{ props.item.pk }}</td>
                            <td class="text-xs-left">{{ props.item.header }}</td>
                            <td class="text-xs-left">{{ props.item.age_limit }}</td>
                            <td class="text-xs-left">{{ props.item.tariff + $store.getters.currency}}</td>
                            <!--<td class="text-xs-left">{{ props.item.price }}</td>-->
                            <td class="text-xs-left">
                                <v-tooltip bottom>
                                    <template v-slot:activator="{ on }">
                                        <v-btn v-on="on" color="info" ripple icon small dark
                                               :to="`/packages/${props.item.pk}/details/`" >
                                            <v-icon small>info</v-icon>
                                        </v-btn>
                                    </template>
                                    <span>{{t('Detail')}}</span>
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
            <v-dialog v-model="dialog" max-width="600px">
                <template v-slot:activator="{ on }">
                    <v-fab-transition v-if="$session.get('isSuperuser')">
                        <v-btn
                                color="primary"
                                dark
                                fixed
                                bottom
                                right
                                fab
                                v-on="on"
                        >
                            <v-icon>add</v-icon>
                        </v-btn>
                    </v-fab-transition>
                </template>

                <v-card>
                    <v-card-title>
                        <span class="headline">{{t('Package')}}</span>
                    </v-card-title>
                    <v-card-text>
                        <v-container grid-list-md>
                            <v-form
                                    ref="form"
                            >
                                <v-layout wrap>

                                    <v-flex xs12 sm6>
                                        <v-text-field :label="t('Header')+'*'" v-model="header"
                                                      :rules="[rules.required,]"></v-text-field>
                                    </v-flex>
                                    <v-flex xs12 sm6>
                                        <v-text-field
                                                :label="t('Tariff') + '*'"
                                                v-model="tariff"
                                                :rules="[rules.required,rules.number,rules.counter]"
                                        ></v-text-field>
                                    </v-flex>

                                </v-layout>
                            </v-form>
                        </v-container>
                        <small>{{t('*indicates required field')}}</small>
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="primary" text @click="dialog = false">{{t('Close')}}</v-btn>
                        <v-btn color="primary" text @click="submitPackageForm">{{t('Save')}}</v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
        </v-container>
    </v-content>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "Packages",
        data () {
            return {
                headers: [
                    {
                        text: this.$translate.locale['Package ID'],
                        align: 'left',
                        value: 'pk',
                    },
                    { text: this.$translate.locale['Header'], value: 'header' },
                    { text: this.$translate.locale['Age limit'], value: 'age_limit' },
                    { text: this.$translate.locale['Tariff'], value: 'tariff' },
                    // { text: 'Price', value: 'price' },
                    { text: this.$translate.locale['Action'], value: 'action', sortable:false },
                ],
                packages: [],
                loading: true,
                snackbar: false,
                dialog:false,
                search:'',
                text: 'Oops... Something went wrong',
                timeout: 5000,
                header:'',
                tariff:'',
                rules: {
                    required: value => !!value || this.$translate.locale['Required.'],
                    counter: value => value <= 2147483647 || this.$translate.locale['Max 2147483647'],
                    number: value => {
                        const pattern = /^\d+$/;
                        return pattern.test(value) || this.$translate.locale['Invalid number.']
                    },
                }
            }
        },
        methods:{
            getData() {
                axios.get(`${this.$hostname}/api/packages/`)
                    .then((response) => {
                        console.log(response.data)
                        if (response.status === 200) {
                            this.packages = response.data;
                            this.loading = false;
                        }
                    }).catch((error) => {
                    this.text = "Connection error";
                    console.log(error)
                    this.snackbar = true;
                });
            },
            submitPackageForm() {
                if (!this.$refs.form.validate()) {
                    this.text = "Fill the form correctly";
                    this.snackbar = true
                } else {
                    const data = {
                        crossdomain: true,
                        header: this.header,
                        tariff: this.tariff,
                    };
                    axios.post(`${this.$hostname}/api/packages/create/`, data)
                        .then((response) => {
                            console.log(response.data)
                            if (response.status === 201) {
                                this.submitted = true;
                                this.dialog = false;
                                this.getData();
                                this.header = '';
                                this.tariff = '';
                                this.text = "Package created!";
                                this.snackbar = true;
                            }
                        }).catch((error) => {
                        this.text = "Connection error";
                        this.snackbar = true;
                    });
                }

            }
        },
        beforeCreate() {
            if (!this.$session.exists()) {
                this.$router.push('/')
            }
        },
        mounted(){
            this.getData();
        },
    }
</script>

<style scoped>

</style>
