<template>
    <v-content color="primary">
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
        <v-container fluid id="main-container" grid-list-md>
            <v-layout row wrap justify-center class="d-inline-block w-100">
                <v-data-table
                        :headers="headers"
                        :items="packages"
                        :items-per-page="5"
                        class="elevation-1"
                        :loading="loading"
                >
                    <template slot="items" slot-scope="props">
                        <td class="text-xs-left">{{ props.item.pk }}</td>
                        <td class="text-xs-left">{{ props.item.header }}</td>
                        <td class="text-xs-left">{{ props.item.age_limit }}</td>
                        <td class="text-xs-left">{{ props.item.tariff }}</td>
                        <!--<td class="text-xs-left">{{ props.item.price }}</td>-->
                        <td class="text-xs-left">
                            <v-tooltip bottom>
                                <template v-slot:activator="{ on }">
                                    <v-btn v-on="on" color="info" fab small dark
                                           :to="`/packages/${props.item.pk}/details/`" >
                                        <v-icon>info</v-icon>
                                    </v-btn>
                                </template>
                                <span>Detail</span>
                            </v-tooltip>
                        </td>
                    </template>
                </v-data-table>
            </v-layout>
            <v-fab-transition>
                <v-btn
                        color="primary"
                        dark
                        fixed
                        bottom
                        right
                        fab
                        v-on="on"
                >
                    <v-icon>add</v-icon>
                </v-btn>
            </v-fab-transition>
        </v-container>
    </v-content>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "Packages",
        data () {
            return {
                headers: [
                    {
                        text: 'Package ID',
                        align: 'left',
                        value: 'pk',
                    },
                    { text: 'Header', value: 'header' },
                    { text: 'Age limit', value: 'age_limit' },
                    { text: 'Tariff', value: 'tariff' },
                    // { text: 'Price', value: 'price' },
                    { text: 'Action', value: 'action', sortable:false },
                ],
                packages: [],
                loading: true,
                snackbar: false,
                text: 'Oops... Something went wrong',
                timeout: 5000,
            }
        },
        methods:{
            getData() {
                axios.get(`${this.$hostname}/api/packages/`)
                    .then((response) => {
                        console.log(response.data)
                        if (response.status === 200) {
                            this.packages = response.data;
                            this.loading = false;
                        }
                    }).catch((error) => {
                    this.text = "Connection error";
                    console.log(error)
                    this.snackbar = true;
                });
            },
        },
        beforeCreate() {
            if (!this.$session.exists()) {
                this.$router.push('/')
            }
        },
        mounted(){
            this.getData();
        },
    }
</script>

<style scoped>

</style>