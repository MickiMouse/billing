<template>
    <v-content color="primary">
        <v-container fluid id="main-container" grid-list-md fill-height>
            <v-dialog v-model="addManyCards" max-width="290" v-if="this.$session.get('isSuperuser')">
                <v-form ref="formManyCards">
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
                                                    :rules="[rules.counterRange, rules.numberRange]"
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
                                                    :rules="[rules.counterRange, rules.numberRange]"
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
                            <v-btn small text color="primary" @click.stop="applyManyCards">{{t('Add')}}</v-btn>
                        </v-card-actions>
                    </v-card>
                </v-form>
            </v-dialog>
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
            <v-layout
                    justify-center
                    wrap
            >
                <v-flex sm8 xs12>
                    <v-card
                            class="mx-auto"
                            :loading="loading"
                    >
                        <v-list two-line subheader dense>
                            <v-subheader>{{t('Details')}}
                                <v-dialog v-model="deleteDialog" max-width="290">
                                    <template v-slot:activator="{ on }">
                                        <v-btn color="error" v-on="on" small icon ripple class="ml-auto mr-0">
                                            <v-icon small>delete</v-icon>
                                        </v-btn>
                                    </template>
                                    <v-card>
                                        <v-card-title class="headline">{{t('Are you sure you want to delete?')}}</v-card-title>
                                        <v-card-text>{{t('This action cannot be undone')}}
                                        </v-card-text>
                                        <v-card-actions>
                                            <v-spacer></v-spacer>
                                            <v-btn small color="error" @click="deleteDialog = false">{{t('Close')}}</v-btn>
                                            <v-btn outline small color="error" @click="deleteSubscriber">{{t('Delete')}}</v-btn>
                                        </v-card-actions>
                                    </v-card>
                                </v-dialog>

                            </v-subheader>
                            <v-list-tile
                                    avatar
                                    @click=""
                            >
                                <v-list-tile-avatar>
                                    <v-icon class="grey lighten-1 white--text">person</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>{{t('Name')}}</v-list-tile-title>
                                    <p class="mb-0">{{details.first_name}} {{details.last_name}}
                                    </p>
                                </v-list-tile-content>
                            </v-list-tile>
                            <v-list-tile
                                    avatar
                                    @click=""
                            >
                                <v-list-tile-avatar>
                                    <v-icon class="grey lighten-1 white--text">person</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>U{{t('surname')}}</v-list-tile-title>
                                    <p class="mb-0">{{details.username}}
                                    </p>
                                </v-list-tile-content>
                            </v-list-tile>
                            <v-list-tile
                                    avatar
                                    @click=""
                                    v-if="$session.get('isSuperuser')"
                            >
                                <v-list-tile-avatar>
                                    <v-icon class="grey lighten-1 white--text">person</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>{{t('Permissions')}}</v-list-tile-title>
                                    <p class="mb-0">{{t(permissions)}}
                                    </p>
                                </v-list-tile-content>
                                <v-list-tile-avatar>
                                    <v-switch
                                            v-model="details.is_superuser"
                                            @change="updatePermissions"
                                            :disabled="!is_permission_edit"
                                    ></v-switch>
                                </v-list-tile-avatar>
                            </v-list-tile>
                            <v-list-tile
                                    avatar
                                    @click=""
                            >
                                <v-list-tile-avatar>
                                    <v-icon class="grey lighten-1 white--text">branding_watermark</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>{{t('Cards prefix')}}</v-list-tile-title>
                                    <p class="mb-0">{{details.rrr}}
                                    </p>
                                </v-list-tile-content>
                            </v-list-tile>
                            <v-list-tile
                                    avatar
                                    @click=""
                            >
                                <v-list-tile-avatar>
                                    <v-icon class="grey lighten-1 white--text">check</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>{{t('Status verification')}}</v-list-tile-title>
                                    <p class="mb-0">{{details.is_activated}}
                                    </p>
                                </v-list-tile-content>
                            </v-list-tile>
                            <v-list-tile
                                    v-if="!$store.getters.isPREPAYMENT"
                                    avatar
                                    @click=""
                            >
                                <v-list-tile-avatar>
                                    <v-icon class="grey lighten-1 white--text">account_balance_wallet</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>{{t('Balance')}}</v-list-tile-title>
                                    <p class="mb-0">{{details.balance + $store.getters.currency}}</p>
                                </v-list-tile-content>
                                <!--<v-list-tile-action>-->
                                    <!--<v-dialog v-model="dialog" max-width="600px">-->
                                        <!--<template v-slot:activator="{ on }">-->
                                            <!--<v-btn icon ripple v-on="on">-->
                                                <!--<v-icon color="grey lighten-1">edit</v-icon>-->
                                            <!--</v-btn>-->
                                        <!--</template>-->
                                        <!--<v-card>-->
                                            <!--<v-card-text>-->
                                                <!--<v-container grid-list-md>-->
                                                    <!--<v-layout wrap>-->

                                                        <!--<v-flex xs12>-->
                                                            <!--<v-form-->
                                                                    <!--ref="form">-->
                                                                <!--<v-text-field-->
                                                                        <!--label="Balance"-->
                                                                        <!--type="number" required-->
                                                                        <!--:rules="[rules.counter, rules.number]"-->
                                                                        <!--v-model="newBalance"></v-text-field>-->
                                                            <!--</v-form>-->
                                                        <!--</v-flex>-->

                                                    <!--</v-layout>-->
                                                <!--</v-container>-->
                                            <!--</v-card-text>-->
                                            <!--<v-card-actions>-->
                                                <!--<v-spacer></v-spacer>-->
                                                <!--<v-btn color="primary" text @click="dialog = false">Close</v-btn>-->
                                                <!--<v-btn color="primary" text @click="changeBalance">Save</v-btn>-->
                                            <!--</v-card-actions>-->
                                        <!--</v-card>-->
                                    <!--</v-dialog>-->
                                <!--</v-list-tile-action>-->
                            </v-list-tile>
                            <v-list-tile
                                    v-if="!$store.getters.isPREPAYMENT"
                                    avatar
                                    @click=""
                            >
                                <v-list-tile-avatar>
                                    <v-icon class="grey lighten-1 white--text">account_balance_wallet</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>{{t('Credit')}}</v-list-tile-title>
                                    <p class="mb-0">{{details.credit + $store.getters.currency}}</p>
                                </v-list-tile-content>
                            </v-list-tile>
                            <v-list-tile
                                    avatar
                                    @click=""
                            >
                                <v-list-tile-avatar>
                                    <v-icon class="grey lighten-1 white--text">card_membership</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>{{t('Card price')}}</v-list-tile-title>
                                    <p class="mb-0">{{details.price_card + $store.getters.currency}}</p>
                                </v-list-tile-content>
                            </v-list-tile>
                            <v-list-tile
                                    avatar
                                    @click=""
                            >
                                <v-list-tile-avatar>
                                    <v-icon class="grey lighten-1 white--text">mail</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>{{t('Email')}}</v-list-tile-title>
                                    <p class="mb-0">{{details.email}}</p>
                                </v-list-tile-content>
                            </v-list-tile>
                            <v-list-tile
                                    avatar
                                    @click=""
                            >
                                <v-list-tile-avatar>
                                    <v-icon class="grey lighten-1 white--text">phone</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>{{t('Phone')}}</v-list-tile-title>
                                    <p class="mb-0">{{details.telephone}}</p>
                                </v-list-tile-content>
                            </v-list-tile>
                            <v-list-tile
                                    avatar
                                    @click=""
                            >
                                <v-list-tile-avatar>
                                    <v-icon class="grey lighten-1 white--text">place</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>{{t('Address')}}</v-list-tile-title>
                                    <p class="mb-0">{{details.address}}</p>
                                </v-list-tile-content>
                            </v-list-tile>
                            <v-list-tile
                                    avatar
                                    @click=""
                            >
                                <v-list-tile-avatar>
                                    <v-icon class="grey lighten-1 white--text">place</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>{{t('Zone')}}</v-list-tile-title>
                                    <p class="mb-0">{{details.zone}}</p>
                                </v-list-tile-content>
                            </v-list-tile>
                            <v-list-tile
                                    avatar
                                    @click=""
                            >
                                <v-list-tile-avatar>
                                    <v-icon class="grey lighten-1 white--text">comment</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>{{t('Comment')}}</v-list-tile-title>
                                    <p class="mb-0">{{details.comment}}
                                    </p>
                                </v-list-tile-content>
                            </v-list-tile>
                        </v-list>
                    </v-card>
                    <v-card class="mt-3" v-if="$session.get('isSuperuser')">
                        <v-card-title>
                            <v-text-field
                                    v-model="searchLogs"
                                    append-icon="search"
                                    :label='t("Search")'
                                    single-line
                                    hide-details
                            ></v-text-field>
                        </v-card-title>
                    </v-card>
                    <v-card class="my-3" v-if="$session.get('isSuperuser')">
                        <v-subheader>{{t('Logs')}}</v-subheader>
                        <v-data-table
                                :headers="headersLogs"
                                :items="details.logs"
                                items-per-page="5"
                                class="elevation-1"
                                :search="searchLogs"
                                :rows-per-page-text="t('Rows per page')"
                                :rows-per-page-items='[10,25, 50, {text: $translate.locale["All"], value: -1}]'
                        >
                            <template slot="items" slot-scope="props">
                                <td class="text-xs-left no-wrap">{{ props.item.date }}</td>
                                <td class="text-xs-left no-wrap">{{ props.item.log }}</td>
                            </template>
                            <template slot="pageText" slot-scope="item">
                                {{t('Elements')}} {{item.pageStart}} - {{item.pageStop}}, {{t('total')}}: {{item.itemsLength}}
                            </template>
                            <template slot="no-data">
                                <v-subheader>{{t('No data available')}}</v-subheader>
                            </template>
                        </v-data-table>
                    </v-card>
                </v-flex>
                <v-flex sm4 xs12>
                    <v-card class="mb-3">
                        <v-card-title>
                            <v-text-field
                                    v-model="search"
                                    append-icon="search"
                                    :label='t("Search")'
                                    single-line
                                    hide-details
                            ></v-text-field>
                        </v-card-title>
                    </v-card>
                    <v-card class="my-3">
                        <v-subheader>{{t('Cards')}}</v-subheader>
                        <v-data-table
                                :headers="headers"
                                :items="cards"
                                items-per-page="5"
                                class="elevation-1"
                                :loading="loadingCards"
                                :search="search"
                                :rows-per-page-text="t('Rows per page')"
                                :rows-per-page-items='[10,25, 50, {text: $translate.locale["All"], value: -1}]'
                        >
                            <template slot="items" slot-scope="props">
                                <td class="text-xs-left no-wrap">{{ props.item.label }}</td>
                                <td class="text-xs-left no-wrap">
                                    <v-tooltip bottom>
                                        <template v-slot:activator="{ on }">
                                            <v-btn v-on="on" :to="`/cards/${props.item.pk}/details/`" color="info"
                                                   ripple
                                                   icon small dark>
                                                <v-icon small>info</v-icon>
                                            </v-btn>
                                        </template>
                                        <span>{{t('Detail')}}</span>
                                    </v-tooltip>
                                    <v-tooltip bottom v-if="props.item.status !== 'Active'">
                                        <template v-slot:activator="{ on }">
                                            <v-btn v-on="on" color="error" @click="removeCard(props.item.pk)" ripple
                                                   icon
                                                   small dark>
                                                <v-icon small>close</v-icon>
                                            </v-btn>
                                        </template>
                                        <span>{{t('Remove')}}</span>
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
                    <v-card class="my-3" v-if="is_permission_edit">
                        <v-subheader>{{t('Available cards')}}</v-subheader>
                        <v-data-table
                                :headers="headers"
                                :items="aviableCards"
                                items-per-page="5"
                                class="elevation-1"
                                :loading="loadingAviableCards"
                                :search="search"
                                :rows-per-page-text="t('Rows per page')"
                                :rows-per-page-items='[10,25, 50, {text: $translate.locale["All"], value: -1}]'
                        >
                            <template slot="items" slot-scope="props">
                                <td class="text-xs-left no-wrap">{{ props.item.label }}</td>
                                <td class="text-xs-left no-wrap">
                                    <v-tooltip bottom>
                                        <template v-slot:activator="{ on }">
                                            <v-btn v-on="on" :to="`/cards/${props.item.pk}/details/`" color="info"
                                                   ripple
                                                   icon small dark>
                                                <v-icon small>info</v-icon>
                                            </v-btn>
                                        </template>
                                        <span>{{t('Detail')}}</span>
                                    </v-tooltip>
                                    <v-tooltip bottom>
                                        <template v-slot:activator="{ on }">
                                            <v-btn v-on="on" @click="addCard(props.item.pk)" color="success" ripple icon
                                                   small dark>
                                                <v-icon small>add</v-icon>
                                            </v-btn>
                                        </template>
                                        <span>{{t('Add')}}</span>
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

                </v-flex>
            </v-layout>
            <v-btn
                    color="primary"
                    dark
                    fixed
                    bottom
                    right
                    fab
                    transition="slide-y-transition"
                    v-if="$session.get('isSuperuser') && aviableCards"
            >
                <v-icon @click.stop="addManyCards = true">library_add</v-icon>
            </v-btn>
        </v-container>
    </v-content>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "ResellersDetails",
        data() {
            return {
                snack: false,
                snackColor: '',
                snackText: '',
                loading: true,
                loadingCards: true,
                loadingAviableCards: true,
                snackbar: false,
                dialog: false,
                deleteDialog: false,
                search: '',
                searchLogs:'',
                text: 'Oops... Something went wrong',
                timeout: 5000,
                newBalance: '',
                addManyCards: false,
                is_permission_edit: false,
                details: {
                    address: "",
                    balance: 0,
                    cards: Array(0),
                    email: '',
                    is_permission_edit: false
                },

                headers: [
                    {
                        text: this.$translate.locale['Label'],
                        align: 'left',
                        //  sortable: false,
                        value: 'label',
                    },
                    {text: this.$translate.locale['Action'], value: 'action', sortable: false},
                    // {text: 'Calories', value: 'calories'},
                ],
                headersLogs: [
                    {text: this.$translate.locale['Date'], value: 'date'},
                    {
                        text: this.$translate.locale['Header'],
                        align: 'left',
                        //  sortable: false,
                        value: 'log',
                    },

                    // {text: 'Calories', value: 'calories'},
                ],
                cards: [],
                aviableCards: [],
                min: 1,
                range: [],
                rules: {
                    counter: value => value <= 2147483647 || this.$translate.locale['Max 2147483647'],
                    number: value => {
                        const pattern = /^\d+$/;
                        return pattern.test(value) || this.$translate.locale['Invalid number.']
                    },
                    counterRange: value => (value <= 2147483647 && value >= 1) || this.$translate.locale['Min 1 and Max 2147483647'],
                    numberRange: value => {
                        const pattern = /^\d+$/;
                        return pattern.test(value) || this.$translate.locale['Invalid number.']
                    },
                },
            }
        },
        computed: {
            max() {
                return  99999;
            },
            permissions(){
                return this.details.is_superuser ? 'Admin' : "Reseller"
            }
        },
        methods: {
            getData() {
                this.loadingCards = true;
                this.loadingAviableCards = true;
                axios.get(`${this.$hostname}/api/resellers/${this.$route.params.id}/`)
                    .then((response) => {
                        if (response.status === 200) {
                            console.log(response.data)
                            this.details = response.data;
                            if(localStorage.currentLanguage === 'arabian'){
                                this.details.logs = JSON.parse(
                                    JSON.stringify(this.details.logs)
                                        .replace(/(ID)/g,'هوية شخصية')
                                        .replace(/(CARD)/g,'بطاقة')
                                        .replace(/(LOG)/g,'سجل')
                                        .replace(/(SUBSCRIBER)/g,'مكتتب')
                                        .replace(/(card)/g,'بطاقة')
                                        .replace(/(Card)/g,'بطاقة')
                                        .replace(/(to subscriber)/g,'إلى المشترك')
                                        .replace(/(Get)/g,'احصل على')
                                        .replace(/(Remove)/g,'إزالة')
                                        .replace(/(pick up the)/g,'التقط')
                                        .replace(/(Pick up)/g,'امسك')
                                        .replace(/(to reseller)/g,'للموزع')
                                        .replace(/(Tie)/g,'ربطة عنق')
                                        .replace(/(Payed)/g,'سيولي')
                                        .replace(/(Price)/g,'السعر')
                                        .replace(/(handed subscriber)/g,'سلم مشترك')
                                        .replace(/(the card)/g,'بطاقة')
                                        .replace(/(Balance)/g,'توازن')
                                        .replace(/(Update expired date)/g,'تحديث تاريخ انتهاء الصلاحية')
                                        .replace(/(Reseller)/g,'موزع')
                                        .replace(/(RESELLER)/g,'موزع')
                                        .replace(/(package)/g,'صفقة')
                                        .replace(/(add)/g,'إضافة')
                                        .replace(/(Add)/g,'إضافة')
                                        .replace(/(enable)/g,'مكن')
                                        .replace(/(disable)/g,'تعطيل')
                                        .replace(/(suspend subscription)/g,'تعليق الاشتراك')
                                        .replace(/(remove)/g,'إزالة')
                                        .replace(/(Remove)/g,'إزالة')
                                        .replace(/(from subscriber )/g,'من المشترك')
                                        .replace(/(from reseller)/g,'من الموزع')
                                        .replace(/(Created)/g,'خلقت')
                                        .replace(/(Edit balance)/g,'تحرير الرصيد')
                                        .replace(/(Deleted)/g,'تم الحذف')
                                        .replace(/(Pick up card from reseller)/g,'التقط بطاقة من الموزع')
                                        .replace(/(Card add to subscriber)/g,'إضافة بطاقة للمشترك')
                                        .replace(/(New value)/g,'قيمة جديدة')
                                        .replace(/(Remove card)/g,'أزل البطاقة')
                                        .replace(/(Registered)/g,'مسجل')
                                        .replace(/(Created card)/g,'بطاقة تم إنشاؤها')
                                );
                            }
                            console.log(this.details.logs)
                            this.cards = this.details.cards;
                            this.aviableCards = this.details.available_cards;
                            this.loadingAviableCards = false;
                            this.min = 1;
                            this.range = [this.min, this.aviableCards.length - 1];
                            this.newBalance = this.details.balance;
                            this.loadingCards = false;
                            this.loadingAviableCards = false;
                            this.details.is_activated = this.details.is_activated ? 'Active' : 'Inactive';
                            axios.get(`${this.$hostname}/api/is-permission-editable/${this.$route.params.id}/`)
                                .then((response) => {
                                    if (response.status === 200) {
                                        console.log(response.data.permission)
                                        this.is_permission_edit = response.data.permission;
                                    }
                                }).catch((error) => {
                                this.text = "Connection error";
                                console.log(error)
                                this.snackbar = true;
                            });
                        }
                    }).catch((error) => {
                    this.text = "Connection error";
                    console.log(error)
                    this.snackbar = true;
                });
            },
            changeBalance() {
                if (!this.$refs.form.validate()) {
                    this.text = "Fill the form correctly";
                    this.snackbar = true;
                } else {
                    this.loading = true;
                    const putBody = {
                        balance: this.newBalance
                    };
                    axios.put(`${this.$hostname}/api/subscribers/edit/balance/${this.$route.params.id}/`, putBody)
                        .then((response) => {
                            if (response.status === 200) {
                                this.details.balance = response.data.balance;
                                this.newBalance = this.details.balance;
                                this.loading = false;
                                this.dialog = false;
                                this.text = "Balance changed!";
                                this.snackbar = true;
                            }
                        }).catch((error) => {
                        if (error.response.status === 400) {
                            this.text = "Balance too low";
                            this.snackbar = true;
                            this.dialog = false;
                        } else {
                            this.text = "Connection error";
                            console.log(error)
                            this.snackbar = true;
                        }
                    });
                }
            },
            addCard(pk) {
                axios.put(`${this.$hostname}/api/resellers/tie/${this.$route.params.id}/`, {card: pk})
                    .then((response) => {
                        if (response.status === 200) {
                            console.log(response.data);
                            this.getData();
                        }
                    }).catch((error) => {
                    this.text = "Connection error";
                    console.log(error)
                    this.snackbar = true;
                });
            },
            applyManyCards() {
                if (!this.$refs.formManyCards.validate()) {
                    this.text = "Fill the form correctly";
                    this.snackbar = true;
                } else {
                    this.loading = true;
                    axios.put(`${this.$hostname}/api/resellers/tie/cards/${this.$route.params.id}/`, {start: this.range[0], stop: this.range[1]})
                        .then((response) => {
                            console.log(response.data)
                            if (response.status === 200) {
                                this.getData();
                                this.text = `Cards were applied!`;
                                this.snackbar = true;
                                this.addManyCards = false;
                            }
                        }).catch((error) => {
                        if (error.response.status === 400) {
                            this.text = "Incorrect range";
                            this.snackbar = true;
                            this.dialog = false;
                        }else{
                            this.text = "Connection error";
                            console.log(error)
                            this.snackbar = true;
                        }
                    });
                }
            },
            removeCard(pk) {
                axios.put(`${this.$hostname}/api/resellers/pickup/${this.$route.params.id}/`, {card: pk})
                    .then((response) => {
                        if (response.status === 200) {
                            console.log(response.data);
                            this.getData();
                        }
                    }).catch((error) => {
                    this.text = "Connection error";
                    console.log(error)
                    this.snackbar = true;
                });
            },
            deleteSubscriber() {
                axios.delete(`${this.$hostname}/api/resellers/delete/${this.$route.params.id}/`)
                    .then((response) => {
                        if (response.status === 204) {
                            console.log(response.data);
                            this.$router.push('/resellers')
                        }
                    }).catch((error) => {
                    this.text = "Connection error";
                    console.log(error)
                    this.snackbar = true;
                });
            },
            updatePermissions(){
                axios.put(`${this.$hostname}/api/change-permission/${this.$route.params.id}/`,{is_superuser: this.details.is_superuser})
                    .then((response) => {
                        if (response.status === 200) {
                            this.text = "Permissions changed!";
                            this.snackbar = true;
                            this.details.is_superuser = response.data.is_superuser;
                        }
                    }).catch((error) => {
                    this.text = "Connection error";
                    this.snackbar = true;
                    this.details.is_superuser = !this.details.is_superuser;
                });
            }
        },
        beforeCreate() {
            if (!this.$session.exists()) {
                this.$router.push('/')
            }
            if(!this.$session.get('isSuperuser')){
                this.$router.push('/cards')
            }
        },
        mounted() {
            this.getData();

        }
    }
</script>

<style scoped>
    /*.v-list__tile__sub-title {*/
    /*overflow-x: auto;*/
    /*}*/
</style>
