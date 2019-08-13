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
            <v-layout row wrap justify-center class="d-inline-block w-100">
                <v-card>
                    <v-card-title>
                        Packages
                        <v-spacer></v-spacer>
                        <v-text-field
                                v-model="search"
                                append-icon="search"
                                label="Search"
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
                    >
                        <template slot="items" slot-scope="props">
                            <td class="text-xs-left">{{ props.item.pk }}</td>
                            <td class="text-xs-left">{{ props.item.header }}</td>
                            <td class="text-xs-left">{{ props.item.age_limit }}</td>
                            <td class="text-xs-left">{{ props.item.tariff }}</td>
                            <!--<td class="text-xs-left">{{ props.item.price }}</td>-->
                            <td class="text-xs-left">
                                <v-tooltip bottom>
                                    <template v-slot:activator="{ on }">
                                        <v-btn v-on="on" color="info" ripple icon small dark
                                               :to="`/packages/${props.item.pk}/details/`" >
                                            <v-icon small>info</v-icon>
                                        </v-btn>
                                    </template>
                                    <span>Detail</span>
                                </v-tooltip>
                            </td>
                        </template>
                    </v-data-table>
                </v-card>

            </v-layout>
            <v-dialog v-model="dialog" persistent max-width="600px">
                <template v-slot:activator="{ on }">
                    <v-fab-transition>
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
                        <span class="headline">Package</span>
                    </v-card-title>
                    <v-card-text>
                        <v-container grid-list-md>
                            <v-form
                                    ref="form"
                            >
                                <v-layout wrap>

                                    <v-flex xs12 sm6>
                                        <v-text-field label="Header*" v-model="header"
                                                      :rules="[rules.required,]"></v-text-field>
                                    </v-flex>
                                    <v-flex xs12 sm6>
                                        <v-text-field
                                                label="Tariff*"
                                                v-model="tariff"
                                                :rules="[rules.required,rules.number,rules.counter]"
                                        ></v-text-field>
                                    </v-flex>

                                </v-layout>
                            </v-form>
                        </v-container>
                        <small>*indicates required field</small>
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="primary" text @click="dialog = false">Close</v-btn>
                        <v-btn color="primary" text @click="submitPackageForm">Save</v-btn>
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
                        text: 'Package ID',
                        align: 'left',
                        value: 'pk',
                    },
                    { text: 'Header', value: 'header' },
                    { text: 'Age limit', value: 'age_limit' },
                    { text: 'Tariff', value: 'tariff' },
                    // { text: 'Price', value: 'price' },
                    { text: 'Action', value: 'action', sortable:false },
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
                    required: value => !!value || 'Required.',
                    counter: value => value <= 2147483647 || 'Max 2147483647',
                    number: value => {
                        const pattern = /^\d+$/;
                        return pattern.test(value) || 'Invalid number.'
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