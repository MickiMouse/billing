<template>
    <v-content>
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
        <v-container
                fluid
                fill-height
        >
            <v-layout
                    align-center
                    justify-center
            >
                <v-flex
                        xs12
                        sm8
                        md4
                >
                    <v-card class="elevation-12" v-if="!submitted">
                        <v-toolbar
                                color="primary"
                                dark
                                flat
                        >
                            <v-toolbar-title>Sign-up</v-toolbar-title>
                            <v-spacer></v-spacer>
                        </v-toolbar>
                        <v-card-text>
                            <v-form
                                    ref="form"
                            >
                                <v-text-field
                                        label="Username"
                                        name="Username"
                                        prepend-icon="person"
                                        :rules="[rules.required, rules.username]"
                                        v-model="username"
                                ></v-text-field>
                                <v-text-field
                                        label="Email"
                                        name="Email"
                                        prepend-icon="email"
                                        :rules="[rules.required, rules.email]"
                                        v-model="email"
                                ></v-text-field>

                                <v-text-field
                                        id="password"
                                        label="Password"
                                        name="password"
                                        prepend-icon="lock"
                                        type="password"
                                        v-model="password"
                                        :rules="[rules.required,rules.counter]"
                                ></v-text-field>
                                <v-text-field
                                        id="password"
                                        label="Repeat password"
                                        name="password"
                                        prepend-icon="lock"
                                        type="password"
                                        v-model="repeatedPassword"
                                        :rules="[rules.required,rules.repeatPassword]"
                                ></v-text-field>
                            </v-form>
                        </v-card-text>
                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn color="primary" @click.prevent="submitLoginForm">Register</v-btn>
                        </v-card-actions>
                        <v-card-text class="d-flex justify-content-center mt-2">
                            <p class="text-xs-center">Already heave an account?
                                <router-link to="/login">Login</router-link>
                            </p>
                        </v-card-text>
                    </v-card>
                    <v-card class="elevation-12" v-else>
                        <v-toolbar
                                color="primary"
                                dark
                                flat
                        >
                            <v-toolbar-title>Sign-up</v-toolbar-title>
                            <v-spacer></v-spacer>
                        </v-toolbar>
                        <v-card-text>
                            <p>Please check your email {{email}} to verify your account</p>
                        </v-card-text>
                        <v-card-text class="d-flex justify-content-center mt-2">
                            <p class="text-xs-center">Already heave an account?
                                <router-link to="/login">Login</router-link>
                            </p>
                        </v-card-text>
                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>
    </v-content>
</template>

<script>
    import axios from "axios";


    export default {
        name: "Register",
        data() {
            return {
                snackbar: false,
                text: 'Oops... Something went wrong',
                timeout: 5000,
                title: 'Preliminary report',
                username:'',
                email: '',
                password: '',
                repeatedPassword: '',
                submitted: false,
                rules: {
                    required: value => !!value || 'Required.',
                    username: value => (value.length >= 4 && value.length <= 150 ) || 'Username between the 4 - 150 characters',
                    counter: value => value.length >= 8 || 'Min 8 characters',
                    repeatPassword: value => value === this.password || 'Passwords do not match',
                    email: value => {
                        const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
                        return pattern.test(value) || 'Invalid e-mail.'
                    },
                },
            }
        },
        methods: {
            submitLoginForm() {
                if (!this.$refs.form.validate()) {
                    this.text = "Fill the form correctly";
                    this.snackbar = true
                } else {
                    const data = {
                        crossdomain: true,
                        username: this.username,
                        email: this.email,
                        password: this.password,
                        password2: this.repeatedPassword,
                    };
                    axios.post(`${this.$hostname}/api/register/reseller/`, data)
                        .then((response) => {
                            console.log(response.data)
                            if (response.status === 201) {
                                this.submitted = true;
                            }
                        }).catch((error) => {
                        this.text = "Connection error";
                        this.snackbar = true;
                    });
                }

            }
        }
    }
</script>

<style scoped>

</style>