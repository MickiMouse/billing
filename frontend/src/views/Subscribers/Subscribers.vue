<template>
    <v-content color="primary">
        <v-container fluid id="main-container" grid-list-md>
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
            <v-layout row wrap justify-center class="d-inline-block w-100">
                <v-data-table
                        :headers="headers"
                        :items="subscribers"
                        :items-per-page="5"
                        class="elevation-1"
                        :loading="loading"
                >
                    <template slot="items" slot-scope="props">
                        <td class="text-xs-left no-wrap">{{ props.item.last_name + " "+
                            props.item.first_name.charAt(0).toUpperCase() + '.' }}
                        </td>
                        <td class="text-xs-left no-wrap">{{ props.item.email }}</td>
                        <td class="text-xs-left no-wrap">{{ props.item.balance }}</td>
                        <td class="text-xs-left no-wrap">{{ props.item.cards.length }}</td>
                        <td class="text-xs-left">
                            <v-tooltip bottom>
                                <template v-slot:activator="{ on }">
                                    <v-btn v-on="on" :to="`/subscribers/${props.item.pk}/details/`" color="info"
                                           small icon ripple dark>
                                        <v-icon small>info</v-icon>
                                    </v-btn>
                                </template>
                                <span>Detail</span>
                            </v-tooltip>
                            <!--<v-tooltip bottom>-->
                            <!--<template v-slot:activator="{ on }">-->
                            <!--<v-btn v-on="on" color="primary" fab small dark>-->
                            <!--<v-icon>edit</v-icon>-->
                            <!--</v-btn>-->
                            <!--</template>-->
                            <!--<span>Edit</span>-->
                            <!--</v-tooltip>-->
                        </td>
                    </template>
                </v-data-table>
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
                        <span class="headline">User Profile</span>
                    </v-card-title>
                    <v-card-text>
                        <v-container grid-list-md>
                            <v-form
                                    ref="form"
                            >
                                <v-layout wrap>

                                    <v-flex xs12 sm6>
                                        <v-text-field label="First name*" v-model="firstName"
                                                      :rules="[rules.required,]"></v-text-field>
                                    </v-flex>
                                    <v-flex xs12 sm6>
                                        <v-text-field
                                                label="Last name*"
                                                v-model="lastName"
                                                :rules="[rules.required,]"
                                        ></v-text-field>
                                    </v-flex>
                                    <v-flex xs12>
                                        <v-text-field label="Email*"
                                                      v-model="email"
                                                      :rules="[rules.required,rules.email]"
                                        ></v-text-field>
                                    </v-flex>
                                    <v-flex xs12>
                                        <v-text-field
                                                ref="address"
                                                v-model="address"
                                                :rules="[
              rules.required,
              () => !!address && address.length <= 50 || 'Address must be less than 50 characters',
              addressCheck
            ]"
                                                label="Address Line"
                                                placeholder="Address"
                                                counter="50"
                                        ></v-text-field>
                                    </v-flex>
                                    <v-flex xs12>
                                        <v-text-field label="Phone*"
                                                      v-model="phone"
                                                      :rules="[rules.required,]"></v-text-field>
                                    </v-flex>

                                </v-layout>
                            </v-form>
                        </v-container>
                        <small>*indicates required field</small>
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="primary" text @click="dialog = false">Close</v-btn>
                        <v-btn color="primary" text @click="submitSubsriberForm">Save</v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>

        </v-container>
    </v-content>
</template>

<script>
    import axios from 'axios';

    // const apiUrl = 'http://192.168.0.8:8000';
    export default {
        name: "Subscribers",
        data() {
            return {
                dialog: false,
                headers: [
                    {
                        text: 'Full name',
                        align: 'left',
                        //  sortable: false,
                        value: 'last_name',
                    },
                    {text: 'Email', value: 'email'},
                    {text: 'Balance', value: 'balance'},
                    {text: 'Cards', value: 'cards'},
                    {text: 'Action', value: 'action', sortable: false},
                ],
                firstName: '',
                lastName: '',
                email: '',
                phone: '',
                address: '',
                subscribers: [],
                loading: true,
                snackbar: false,
                text: 'Oops... Something went wrong',
                timeout: 5000,
                rules: {
                    required: value => !!value || 'Required.',
                    email: value => {
                        const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
                        return pattern.test(value) || 'Invalid e-mail.'
                    },
                }
            }
        },
        methods: {
            getData() {
                axios.get(`${this.$hostname}/api/subscribers/`)
                    .then((response) => {
                        console.log(response.data)
                        if (response.status === 200) {
                            this.subscribers = response.data;
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
            submitSubsriberForm() {
                if (!this.$refs.form.validate()) {
                    this.text = "Fill the form correctly";
                    this.snackbar = true
                } else {
                    const data = {
                        crossdomain: true,
                        first_name: this.firstName,
                        last_name: this.lastName,
                        email: this.email,
                        telephone: this.phone,
                        address: this.address
                    };
                    axios.post(`${this.$hostname}/api/subscribers/create/`, data)
                        .then((response) => {
                            console.log(response.data)
                            if (response.status === 201) {
                                this.submitted = true;
                                this.dialog = false;
                                this.getData();
                                this.firstName = '';
                                this.lastName = '';
                                this.email = '';
                                this.phone = '';
                                this.address = '';
                                this.text = "Subscriber created!";
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
        mounted() {
            this.getData();
        },

    }
</script>

<style scoped>


</style>