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
              <v-card>
                  <v-card-title>
                      Cards
                      <v-spacer></v-spacer>
                      <v-text-field
                              v-model="search"
                              append-icon="search"
                              label="Search"
                              single-line
                              hide-details
                      ></v-text-field>
                  </v-card-title>
                  <v-data-table
                          :headers="headers"
                          :items="cards"
                          :items-per-page="5"
                          class="elevation-1"
                          :loading="loading"
                          :search="search"
                  >
                      <template slot="items" slot-scope="props">
                          <td class="text-xs-left">{{ props.item.pk }}</td>
                          <td class="text-xs-left">{{ props.item.label }}</td>
                          <td class="text-xs-left">{{ props.item.created_at }}</td>
                          <td class="text-xs-left">{{ props.item.last_change }}</td>
                          <td class="text-xs-left">{{ props.item.expired_date }}</td>
                          <td class="text-xs-left">{{ props.item.status }}</td>
                          <!--<td class="text-xs-left">{{ props.item.price }}</td>-->
                          <td class="text-xs-left">
                              <v-tooltip bottom>
                                  <template v-slot:activator="{ on }">
                                      <v-btn v-on="on" color="info" ripple icon small dark
                                             :to="`/cards/${props.item.pk}/details/`" >
                                          <v-icon small>info</v-icon>
                                      </v-btn>
                                  </template>
                                  <span>Detail</span>
                              </v-tooltip>
                          </td>
                      </template>
                  </v-data-table>
              </v-card>
            </v-layout>
            <v-fab-transition v-if="this.$session.get('isSuperuser')">
                <v-btn
                        color="primary"
                        dark
                        fixed
                        bottom
                        right
                        fab
                        @click="createCard"
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
        name: "Cards",
        data () {
            return {
                headers: [
                    {
                        text: 'Card ID',
                        align: 'left',
                        value: 'pk',
                    },
                    { text: 'Card Label', value: 'label' },
                    { text: 'Issued', value: 'created_at' },
                    { text: 'Edited', value: 'last_change' },
                    { text: 'Expired', value: 'expired_date' },
                    { text: 'Status', value: 'status' },
                    // { text: 'Price', value: 'price' },
                    { text: 'Action', value: 'action', sortable:false },
                ],
                cards: [],
                loading: true,
                snackbar: false,
                search:'',
                text: 'Oops... Something went wrong',
                timeout: 5000,
            }
        },
        methods:{
            getData() {
                axios.get(`${this.$hostname}/api/cards/`)
                    .then((response) => {
                        console.log(response.data)
                        if (response.status === 200) {
                            this.cards = response.data;
                            this.loading = false;
                        }
                    }).catch((error) => {
                    this.text = "Connection error";
                    console.log(error)
                    this.snackbar = true;
                });
            },
            createCard(){
                axios.post(`${this.$hostname}/api/cards/create/`)
                    .then((response) => {
                        console.log(response.data)
                        if (response.status === 201) {
                            this.getData();
                            this.text = "Card created!";
                            this.snackbar = true;
                        }
                    }).catch((error) => {
                    this.text = "Connection error";
                    this.snackbar = true;
                });
            }
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