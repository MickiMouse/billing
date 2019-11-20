<template>
    <v-app>
        <top-panel/>
        <router-view/>
    </v-app>
</template>

<script>
    import Vue from 'vue'
    import TopPanel from "@/components/topPanel/topPanel";

    export default {
        name: 'App',
        components: {
            TopPanel,
        },
        data() {
            return {}
        },
        computed: {},

        methods: {},
        mounted() {

        }

    }
</script>
<style lang="scss">
    .v-toolbar__extension {
        padding: 0;
    }

    .w-100 {
        width: 100%;
    }

    .v-dialog__content--active {
        z-index: 550 !important;
    }

    .v-btn--router {
        .material-icons {
            display: inline-flex !important;
            position: relative !important;
        }
    }
</style>
