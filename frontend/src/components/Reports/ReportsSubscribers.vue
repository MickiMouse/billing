<template>
    <v-card>
        <v-card-title>
            {{t('Total')}} {{kind}}: {{total}}
            <v-spacer></v-spacer>
            <v-text-field
                    v-model="search"
                    append-icon="search"
                    :label='t("Search")'
                    single-line
                    hide-details
            ></v-text-field>
        </v-card-title>
        <v-data-table
                :rows-per-page-text="t('Rows per page')"

                :headers="headers"
                :items="data"
                :items-per-page="5"
                class="elevation-1"
                :loading="loading"
                :search="search"
                :rows-per-page-items='[10,25, 50, {text: $translate.locale["All"], value: -1}]'
        >
            <template slot="items" slot-scope="props">
                <td class="text-xs-left no-wrap">{{ props.item.name }}
                </td>
                <td class="text-xs-left no-wrap">{{ props.item.item }}</td>
            </template>
            <template slot="pageText" slot-scope="item">
                {{t('Elements')}} {{item.pageStart}} - {{item.pageStop}}, {{t('total')}}: {{item.itemsLength}}
            </template>
            <template slot="no-data">
                <v-subheader>{{t('No data available')}}</v-subheader>
            </template>
        </v-data-table>
    </v-card>
</template>

<script>
    export default {
        name: "ReportsSubscribers",
        props:{
            data: Array,
            loading: Boolean,
            total: Number,
            kind: String
        },
        data(){
            return{
                headers: [
                    {
                        text:  this.$translate.locale['Reseller'],
                        align: 'left',
                        value: 'name',
                    },
                    {text: this.kind.charAt(0).toUpperCase() + this.kind.slice(1), value: 'item'},
                ],
                search: '',
            }
        }
    }
</script>

<style scoped>

</style>
