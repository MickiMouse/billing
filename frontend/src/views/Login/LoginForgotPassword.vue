<template>
    <v-content>
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
                    <v-card class="elevation-12" v-if="!submitted && !stage2">
                        <v-toolbar
                                color="primary"
                                dark
                                flat
                        >
                            <v-toolbar-title>{{t('Login')}}</v-toolbar-title>
                            <v-spacer></v-spacer>
                        </v-toolbar>
                        <v-form
                                ref="form"
                                class="text-xs-right"
                                @submit.prevent="submitLoginForm"
                        >
                            <v-card-text>

                                <v-text-field
                                        :label="t('Email')"
                                        name="Email"
                                        prepend-icon="person"
                                        :rules="[rules.required,rules.email]"
                                        v-model="email"
                                ></v-text-field>

                            </v-card-text>
                            <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn color="primary" type="submit">{{t('Submit')}}</v-btn>
                            </v-card-actions>
                            <v-card-text class="d-flex justify-content-between mt-2">
                                <router-link class="text-xs-left" to="/register">{{t('Register now!')}}</router-link>
                                <router-link class="text-xs-right" to="/login">{{t('Login')}}</router-link>
                            </v-card-text>
                        </v-form>
                    </v-card>
                    <v-card class="elevation-12" v-else-if="submitted && !stage2">
                        <v-toolbar
                                color="primary"
                                dark
                                flat
                        >
                            <v-toolbar-title>{{t('Login')}}</v-toolbar-title>
                            <v-spacer></v-spacer>
                        </v-toolbar>
                        <v-card-text>
                            <p>{{t('Please check your email')}} {{email}} {{t('to verify your account')}}</p>
                        </v-card-text>
                    </v-card>
                    <v-card class="elevation-12" v-else>
                        <v-toolbar
                                color="primary"
                                dark
                                flat
                        >
                            <v-toolbar-title>{{t('Login')}}</v-toolbar-title>
                            <v-spacer></v-spacer>
                        </v-toolbar>
                        <v-form
                                ref="form2"
                                class="text-xs-right"
                                @submit.prevent="submitLoginFormStage2"
                        >
                            <v-card-text>

                                <v-text-field
                                        id="password"
                                        :label="t('Password')"
                                        name="password"
                                        prepend-icon="lock"
                                        type="password"
                                        v-model="password"
                                        :rules="[rules.required,rules.counter]"
                                ></v-text-field>
                                <v-text-field
                                        id="password"
                                        :label="('Repeat password')"
                                        name="password"
                                        prepend-icon="lock"
                                        type="password"
                                        v-model="repeatedPassword"
                                        :rules="[rules.required,rules.repeatPassword]"
                                ></v-text-field>

                            </v-card-text>
                            <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn color="primary" type="submit">{{t('Submit')}}</v-btn>
                            </v-card-actions>
                        </v-form>
                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>
    </v-content>
</template>

<script>
    import axios from "axios";

    export default {
        name: "LoginForgotPassword",
        data() {
            return {
                snackbar: false,
                text: 'Oops... Something went wrong',
                timeout: 5000,
                title: 'Preliminary report',
                username: '',
                email: '',
                password: '',
                repeatedPassword: '',
                submitted: false,
                stage2: false,
                rules: {
                    required: value => !!value || this.$translate.locale['Required.'],
                    username: value => (value.length >= 4 && value.length <= 150) || this.$translate.locale['Username between the 4 - 150 characters'],
                    counter: value => value.length >= 8 || this.$translate.locale['Min 8 characters'],
                    repeatPassword: value => value === this.password || this.$translate.locale['Passwords do not match'],
                    email: value => {
                        const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
                        return pattern.test(value) || this.$translate.locale['Invalid e-mail.']
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
                    if (this.$route.params.token) {
                        this.stage2 = true;
                    } else {
                        axios.post(`${this.$hostname}/api/password-reset/`, {email: this.email})
                            .then((response) => {
                                if (response.status === 200) {
                                    this.submitted = true;
                                }
                            }).catch((error) => {
                            this.submitted = false;
                            this.text = "Connection error";
                            console.log(error)
                            this.snackbar = true;
                        });
                    }
                }

            },
            submitLoginFormStage2() {
                if (!this.$refs.form2.validate()) {
                    this.text = "Fill the form correctly";
                    this.snackbar = true
                } else {
                    if (this.$route.params.token) {
                        axios.put(`${this.$hostname}/api/password/${this.$route.params.token}/`, {
                            password: this.password,
                            password2: this.repeatedPassword
                        })
                            .then((response) => {
                                if (response.status === 200) {
                                    this.text = "Successful";
                                    this.snackbar = true;
                                    this.$router.push('/login')
                                }
                            }).catch((error) => {
                            this.text = "Connection error";
                            console.log(error)
                            this.snackbar = true;
                        });
                    } else {
                        this.text = "Connection error";
                        console.log(error)
                        this.snackbar = true;
                    }
                }

            }
        },
        mounted() {
            if (this.$route.params.token) {
                this.submitted = true;
                this.stage2 = true;
            }
        }
    }
</script>

<style scoped>

</style>
