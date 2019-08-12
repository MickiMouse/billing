<template>
    <v-content color="primary">
        <v-container fluid id="main-container" grid-list-md>
            <v-layout row wrap justify-center>
                <v-flex md4 justify-center>
                    <div>
                        <h1>Resellers</h1>
                    </div>
                </v-flex>
            </v-layout>
        </v-container>

    </v-content>


</template>

<script>
    export default {
        name: "Resellers",
        beforeCreate() {
            if (!this.$session.exists()) {
                this.$router.push('/')
            }
        },
    }
</script>

<style scoped>

</style>