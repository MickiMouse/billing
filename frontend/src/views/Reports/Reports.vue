<template>
    <v-content color="primary">
        <v-container fluid id="main-container" grid-list-md>
            <v-layout row wrap justify-center>
                <v-flex md4 justify-center>
                    <div>
                        <h1>Reports</h1>
                        <h2> Response: {{ info }}</h2>
                    </div>
                </v-flex>
            </v-layout>
        </v-container>

    </v-content>

</template>

<script>
    import axios from 'axios';
    export default {
        name: "Reports",
        data() {
            return {
                info: null
            };
        },
        mounted() {
            var config = {
                headers: {'Access-Control-Allow-Origin': '*'}

            };
            axios
                .get('https://9208c4fc.ngrok.io/api/test/',config)
                .then(response => (this.info = response));
        }
    }
</script>

<style scoped>

</style>