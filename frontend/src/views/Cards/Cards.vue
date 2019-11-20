<template>
    <v-content color="primary">
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
        <v-container fluid id="main-container" grid-list-md>
            <v-dialog v-model="addManyCards" max-width="290" v-if="this.$session.get('isSuperuser')">
                <v-form ref="form">
                    <v-card>
                        <!--<v-card-title class="headline">Lorem ipsum dolor sit.</v-card-title>-->
                        <v-card-text>
                            <v-row>
                                <v-col class="px-4">
                                    <v-range-slider
                                            v-model="range"
                                            :max="max"
                                            :min="min"
                                            hide-details
                                            class="align-center"
                                    >
                                        <template v-slot:prepend>
                                            <v-text-field
                                                    v-model="range[0]"
                                                    :rules="[rules.counter, rules.number]"
                                                    class="mt-0 pt-0"
                                                    hide-details
                                                    single-line
                                                    type="number"
                                                    style="width: 60px"
                                            ></v-text-field>
                                        </template>
                                        <template v-slot:append>
                                            <v-text-field
                                                    v-model="range[1]"
                                                    :rules="[rules.counter, rules.number]"
                                                    class="mt-0 pt-0"
                                                    hide-details
                                                    single-line
                                                    type="number"
                                                    style="width: 60px"
                                            ></v-text-field>
                                        </template>
                                    </v-range-slider>
                                </v-col>
                            </v-row>
                        </v-card-text>
                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn outline small color="error" @click.stop="addManyCards = false">{{t('Close')}}</v-btn>
                            <v-btn small text color="primary" @click.stop="createManyCards">{{t('Add')}}</v-btn>
                        </v-card-actions>
                    </v-card>
                </v-form>
            </v-dialog>
            <v-layout row wrap justify-center class="d-inline-block w-100 mb-5">
                <v-card>
                    <v-card-title>
                        {{t('Cards')}}
                        <v-spacer></v-spacer>
                        <v-text-field
                                v-model="search"
                                append-icon="search"
                                :label="t('Search')"
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
                            :rows-per-page-text="t('Rows per page')"
                            :rows-per-page-items='[10,25, 50, {text: $translate.locale["All"], value: -1}]'
                    >
                        <template slot="items" slot-scope="props">
                            <td class="text-xs-left">{{ props.item.pk }}</td>
                            <td class="text-xs-left">{{ props.item.label }}</td>
                            <td class="text-xs-left">{{ props.item.created_at }}</td>
                            <td class="text-xs-left">{{ props.item.last_change }}</td>
                            <td class="text-xs-left">{{ props.item.expired_date }}</td>
                            <td class="text-xs-left">{{ t(props.item.status) }}</td>
                            <!--<td class="text-xs-left">{{ props.item.price }}</td>-->
                            <td class="text-xs-left">
                                <v-tooltip bottom>
                                    <template v-slot:activator="{ on }">
                                        <v-btn v-on="on" color="info" ripple icon small dark
                                               :to="`/cards/${props.item.pk}/details/`">
                                            <v-icon small>info</v-icon>
                                        </v-btn>
                                    </template>
                                    <span>{{t('Detail')}}</span>
                                </v-tooltip>
                            </td>
                        </template>
                        <template slot="pageText" slot-scope="item">
                            {{t('Elements')}} {{item.pageStart}} - {{item.pageStop}}, {{t('total')}}: {{item.itemsLength}}
                        </template>
                        <template slot="no-data">
                            <v-subheader>{{t('No data available')}}</v-subheader>
                        </template>
                    </v-data-table>
                </v-card>
            </v-layout>
            <v-speed-dial
                    v-model="fab"
                    color="primary"
                    dark
                    fixed
                    bottom
                    right
                    fab
                    direction="top"
                    :open-on-hover="hover"
                    transition="slide-y-transition"
                    v-if="this.$session.get('isSuperuser')"
            >
                <template v-slot:activator>
                    <v-btn
                            v-model="fab"
                            color="primary"
                            dark
                            fab
                    >
                        <v-icon v-if="fab">close</v-icon>
                        <v-icon v-else>library_add</v-icon>
                    </v-btn>
                </template>
                <v-btn
                        fab
                        dark
                        small
                        color="primary darken-1"
                        @click="createCard"
                >
                    <v-icon>add</v-icon>
                </v-btn>
                <v-btn
                        fab
                        dark
                        small
                        color="primary darken-1"
                        @click.stop="addManyCards = true"
                >
                    <v-icon>playlist_add</v-icon>
                </v-btn>
            </v-speed-dial>
        </v-container>
    </v-content>

</template>

<script>
    import axios from 'axios';

    export default {
        name: "Cards",
        data() {
            return {
                headers: [
                    {
                        text: this.$translate.locale['Card ID'],
                        align: 'left',
                        value: 'pk',
                    },
                    {text: this.$translate.locale['Card Label'], value: 'label'},
                    {text: this.$translate.locale['Issued'], value: 'created_at'},
                    {text: this.$translate.locale['Edited'], value: 'last_change'},
                    {text: this.$translate.locale['Expired'], value: 'expired_date'},
                    {text: this.$translate.locale['Status'], value: 'status'},
                    // { text: 'Price', value: 'price' },
                    {text: this.$translate.locale['Action'], value: 'action', sortable: false},
                ],
                cards: [],
                loading: true,
                snackbar: false,
                search: '',
                fab: false,
                hover: true,
                text: 'Oops... Something went wrong',
                timeout: 5000,
                addManyCards: false,
                min: 0,
                range: [],
                rules: {
                    counter: value => (value <= 2147483647 && value >= 1) || this.$translate.locale['Min 1 and Max 2147483647'],
                    number: value => {
                        const pattern = /^\d+$/;
                        return pattern.test(value) || this.$translate.locale['Invalid number.']
                    },
                },
            }
        },
        computed: {
            max() {
                return this.min + 99;
            },
        },
        methods: {
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
                this.getRange();
            },
            createCard() {
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
            },
            createManyCards() {
                if (!this.$refs.form.validate()) {
                    this.text = "Fill the form correctly";
                    this.snackbar = true;
                } else {
                    this.loading = true;
                    axios.post(`${this.$hostname}/api/cards/create/range/`, {start: this.range[0], stop: this.range[1]})
                        .then((response) => {
                            console.log(response.data)
                            if (response.status === 201) {
                                this.getData();
                                this.text = `Cards were created!`;
                                this.snackbar = true;
                                this.addManyCards = false;
                            }
                        }).catch((error) => {
                        this.addManyCards = false;
                        this.text = "Connection error";
                        this.snackbar = true;
                    });
                }
            },
            getRange() {
                this.loading = true;
                axios.get(`${this.$hostname}/api/cards/create/range/`)
                    .then((response) => {
                        console.log(response.data)
                        if (response.status === 200) {
                            this.min = response.data.start;
                            this.loading = false;
                            this.range = [this.min, this.min + 10];
                            this.rules.counter = value => (value <= (this.min + 99) && value >= this.min) || 'Min 1 and Max 2147483647';
                        }
                    }).catch((error) => {
                    this.text = "Connection error";
                    console.log(error)
                    this.snackbar = true;
                });
            }
        },
        beforeCreate() {
            if (!this.$session.exists()) {
                this.$router.push('/')
            }
        },
        mounted() {
            this.getData();
        },
    }
</script>

<style scoped>

</style>
