<template>
    <div>
        <top-panel-menu/>
        <v-toolbar color="secondary" extended extension-height="4" app>


                <v-flex xs4 align-center d-flex>
                    <v-flex xs1>
                        <v-toolbar-side-icon
                                @click.stop="$store.dispatch('switchMenu')"/>
                    </v-flex>

                    <v-toolbar-title class="headline text-uppercase">
                        <!--<span>SMM</span>-->
                        <span class="font-weight-light">Ripple</span>
                        <span class="font-weight-thin">{{this.$route.meta.title}}</span>
                    </v-toolbar-title>
                </v-flex>
                <v-flex xs4>
                    <top-panel-search/>
                </v-flex>

            <template v-slot:extension>
                <v-progress-linear slot="extension" v-model="loadingPercent" v-show="loading" :indeterminate="false"
                                   class="px-0"
                                   color="secondary" height="4"></v-progress-linear>
            </template>

        </v-toolbar>
    </div>
</template>

<script>
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
            }
        }
    }
</script>

<style scoped>

</style>