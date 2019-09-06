<template>
    <v-card>
        <v-card-title>
            Total {{kind}}: {{total}}
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
                :items="data"
                :items-per-page="5"
                class="elevation-1"
                :loading="loading"
                :search="search"
        >
            <template slot="items" slot-scope="props">
                <td class="text-xs-left no-wrap">{{ props.item.name }}
                </td>
                <td class="text-xs-left no-wrap">{{ props.item.total }}</td>
                <td class="text-xs-left no-wrap">
                    <v-list-group
                            v-if="props.item.cards.length > 0 && props.item.cards[0]!=='None'"
                    >
                        <v-list-item
                                v-for="(card, i) in props.item.cards"
                                :key="i"
                        >

                            <v-list-tile-sub-title>
                                {{card}}
                            </v-list-tile-sub-title>
                        </v-list-item>
                    </v-list-group>
                    <v-icon v-else class="grey--text">remove</v-icon>
                </td>
            </template>

        </v-data-table>
    </v-card>
</template>

<script>
    export default {
        name: "ReportsReseller",
        props: {
            data: Array,
            loading: Boolean,
            total: Number,
            kind: String
        },
        data() {
            return {
                headers: [
                    {
                        text: 'Reseller',
                        align: 'left',
                        value: 'name',
                    },
                    {
                        text: 'Total cards',
                        align: 'left',
                        value: 'total',
                    },
                    {text: this.kind.charAt(0).toUpperCase() + this.kind.slice(1), value: 'cards'},
                ],
                search: '',
            }
        }
    }
</script>

<style>
    .cards-wrapper {
        position: relative;
        overflow-x: hidden;
        overflow-y: auto;
        height: 100px;
    }

    .cards-inner {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;

    }
    .v-list__group__header__append-icon{
        padding-left: 0 !important;
    }
</style>