<template>
    <div v-if="show">
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
        <top-panel-menu/>
        <v-toolbar color="primary" dark extended extension-height="4" app>


            <v-toolbar-side-icon
                    @click.stop="$store.dispatch('switchMenu')"/>

            <v-toolbar-title class="headline text-uppercase">
                <!--<span>SMM</span>-->
                <span class="font-weight-light">Ripple</span>
                <span class="font-weight-thin">{{this.$route.meta.title}}</span>
            </v-toolbar-title>
            <!--<v-flex xs4>-->
                <!--<top-panel-search/>-->
            <!--</v-flex>-->
            <v-spacer/>
            <v-btn text
                   flat
                   color="secondary"
                   @click="logout"
            >Logout
            </v-btn>
            <template v-slot:extension>
                <v-progress-linear slot="extension" v-model="loadingPercent" v-show="loading" :indeterminate="false"
                                   class="px-0"
                                   color="secondary" height="4"></v-progress-linear>
            </template>

        </v-toolbar>
    </div>
</template>

<script>
    import axios from 'axios'
    import TopPanelMenu from "@/components/topPanel/topPanelMenu";
    import TopPanelSearch from "@/components/topPanel/topPanelSearch";

    export default {
        name: "topPanel",
        components: {TopPanelSearch, TopPanelMenu},
        data() {
            return {
                drawer: false,
                loadingPercent: 0,
                loadTime: 0,
                interval: null,
                loading: true,
                snackbar: false,
                text: 'Oops... Something went wrong',
                timeout: 5000,
            }
        },
        created() {
            let perfData = window.performance.timing;
            let estimatedTime = Math.abs(perfData.loadEventEnd - perfData.navigationStart);
            this.loadTime = parseInt((estimatedTime / 1000) % 60) * 100;
            this.doProgress();
        },
        watch: {
            loadingPercent(val) {
                if (val >= 100) {
                    this.loading = false;
                    clearInterval(this.interval);
                }
            },
        },
        methods: {
            doProgress() {
                let step = this.loadTime / 100;
                this.interval = setInterval(() => {
                    this.loadingPercent++
                }, step);
            },
            logout() {
                axios.post(`${this.$hostname}/api/token/logout/`)
                    .then((response) => {
                        console.log(response.data)
                        if (response.status === 200) {
                            this.text = "Successful";
                            this.snackbar = true;
                            this.$session.destroy();
                            this.$router.push('/');
                            axios.defaults.headers.common['Authorization'] = '';
                        }
                    }).catch((error) => {
                    this.text = "Connection error";
                    console.log(error)
                    this.snackbar = true;
                    this.$session.destroy();
                    this.$router.push('/');
                    axios.defaults.headers.common['Authorization'] = '';
                });
            }
        },
        computed: {
            show: function () {
                return  this.$route.name !== 'login' &&  this.$route.name !== 'register';
            }
        },
        mounted(){
            axios.defaults.headers.common['Authorization'] = 'Token ' + this.$session.get('jwt');
        }
    }
</script>

<style lang="scss">
    .v-toolbar {
        z-index: 500 !important;
    }
</style>