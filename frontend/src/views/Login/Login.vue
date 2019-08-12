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
                    <v-card class="elevation-12">
                        <v-toolbar
                                color="primary"
                                dark
                                flat
                        >
                            <v-toolbar-title>Login</v-toolbar-title>
                            <v-spacer></v-spacer>
                        </v-toolbar>
                        <v-card-text>
                            <v-form
                                    ref="form"
                                    class="text-xs-right"
                            >
                                <v-text-field
                                        label="Username"
                                        name="Username"
                                        prepend-icon="person"
                                        :rules="[rules.required, rules.username]"
                                        v-model="username"
                                ></v-text-field>
                                <!--<v-text-field-->
                                        <!--label="Email"-->
                                        <!--name="Email"-->
                                        <!--prepend-icon="person"-->
                                        <!--:rules="[rules.required,rules.email]"-->
                                        <!--v-model="email"-->
                                <!--&gt;</v-text-field>-->

                                <v-text-field
                                        id="password"
                                        label="Password"
                                        name="password"
                                        prepend-icon="lock"
                                        type="password"
                                        v-model="password"
                                        :rules="[rules.required,rules.counter]"
                                ></v-text-field>
                            </v-form>
                        </v-card-text>
                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn color="primary" @click.prevent="submitLoginForm">Login</v-btn>
                        </v-card-actions>
                        <v-card-text class="d-flex justify-content-between mt-2">
                            <router-link class="text-xs-left" to="/register">Register now!</router-link>
                            <a href="" class="text-xs-right">Forgot Password?</a>
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
        name: "Login",
        data() {
            return {
                snackbar: false,
                text: 'Oops... Something went wrong',
                timeout: 5000,
                title: 'Preliminary report',
                username: '',
                email: '',
                password: '',
                rules: {
                    required: value => !!value || 'Required.',
                    username: value => (value.length >= 4 && value.length <= 150) || 'Username between the 4 - 150 characters',
                    counter: value => value.length >= 8 || 'Min 8 characters',
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
                       // email: this.email,
                        password: this.password,
                        username: this.username
                    };
                    // this.$session.start()
                    // this.$session.set('jwt', '5160d824064220354ab3930f2674db3141336830')
                    // axios.defaults.headers.common['Authorization'] = 'Token ' + this.$session.get('jwt');
                    // this.$router.push('/dashboard')

                    axios.post(`${this.$hostname}/auth/token/login/`, data)
                        .then((response) => {
                            console.log(response.data)
                            if (response.status === 200 && response.data.auth_token) {
                                this.$session.start()
                                this.$session.set('jwt', response.data.auth_token)
                                axios.defaults.headers.common['Authorization'] = 'Token ' + this.$session.get('jwt');
                                this.$router.push('/dashboard')
                            }
                        }).catch((error) => {
                        this.text = "Connection error";
                        console.log(error)
                        this.snackbar = true;
                    });
                }

            }
        }
    }
</script>

<style scoped>

</style>