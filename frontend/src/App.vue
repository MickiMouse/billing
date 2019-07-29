<template>
    <v-app>
        <top-panel></top-panel>
        <router-view>

        </router-view>
    </v-app>
</template>

<script>
    import TopPanel from "@/components/topPanel/topPanel";

    export default {
        name: 'App',
        components: {
            TopPanel,
        },
        data() {
            return {

            }
        },
        computed: {

        },

        methods: {
        }

    }
</script>
<style lang="scss">
    .v-toolbar__extension {
        padding: 0;
    }
</style>