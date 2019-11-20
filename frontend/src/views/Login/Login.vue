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
                    <v-card class="elevation-12">
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
                                        :label="t('Username')"
                                        name="Username"
                                        prepend-icon="person"
                                        :rules="[rules.required, rules.username]"
                                        v-model="username"
                                ></v-text-field>

                                <v-text-field
                                        id="password"
                                        :label="t('Password')"
                                        name="password"
                                        prepend-icon="lock"
                                        type="password"
                                        v-model="password"
                                        :rules="[rules.required,rules.counter]"
                                ></v-text-field>

                            </v-card-text>
                            <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn color="primary" type="submit" :loading="verifyRegisterLoading">{{t('Login')}}</v-btn>
                            </v-card-actions>
                            <v-card-text class="d-flex justify-content-between mt-2">
                                <router-link class="text-xs-left" to="/register">{{t('Register now!')}}</router-link>
                                <router-link class="text-xs-right" to="/forgot">{{t('Forgot Password?')}}</router-link>
                            </v-card-text>
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
                verifyRegisterLoading: false,
                rules: {
                    required: value => !!value || this.$translate.locale['Required.'],
                    username: value => (value.length >= 4 && value.length <= 150) || this.$translate.locale['Username between the 4 - 150 characters'],
                    counter: value => value.length >= 8 || this.$translate.locale['Min 8 characters'],
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
                    const data = {
                        crossdomain: true,
                        // email: this.email,
                        password: this.password,
                        username: this.username
                    };
                    axios.post(`${this.$hostname}/api/token/login/`, data)
                        .then((response) => {
                            console.log(response.data)
                            if (response.status === 200 && response.data.auth_token) {
                                this.$session.start()
                                this.$session.set('jwt', response.data.auth_token)
                                axios.defaults.headers.common['Authorization'] = 'Token ' + this.$session.get('jwt');
                                // this.$store.commit('set',{type: 'isSuperuser', items: response.data.is_superuser});
                                // console.log(this.$store.getters.isSuperuser)
                                this.$session.set('isSuperuser', response.data.is_superuser)
                                // this.$store.dispatch('set',response.data.is_superuser)
                                this.$router.push('/dashboard')
                            }
                        }).catch((error) => {

                        console.log(error)

                    });
                }

            }
        },
        beforeCreate() {
            this.$session.destroy();
            this.$router.push('/');
            axios.defaults.headers.common['Authorization'] = '';
            if (this.$route.params.token) {
                this.verifyRegisterLoading = true;
                axios.get(`${this.$hostname}/api/register_activate/${this.$route.params.token}/`)
                    .then((response) => {
                        if (response.status === 200) {
                            this.verifyRegisterLoading = false;
                            this.name = response.username;
                            this.text = "Registration successful";
                            this.snackbar = true;
                        }
                    }).catch((error) => {
                    this.verifyRegisterLoading = false;
                    this.text = "Connection error";
                    console.log(error)
                    this.snackbar = true;
                });
            }
        }
    }
</script>

<style scoped>

</style>