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
                <td class="text-xs-left no-wrap">{{ props.item.item }}</td>
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
                        text: 'Reseller',
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