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
            var xhr = new XMLHttpRequest();
            xhr.open("GET", "http://localhost:8000/api/test/", true);
            xhr.onload = () =>{
                console.log(JSON.parse(xhr.responseText))
               this.info = JSON.parse(xhr.responseText)[0];
            };
            xhr.send();
        }
    }
</script>

<style scoped>

</style>