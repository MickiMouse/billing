<template>
    <v-content color="primary">
        <v-container fluid id="main-container" grid-list-md>
            <v-layout row wrap justify-center>
                <v-flex md4 justify-center>
                    <v-card>
                        <apexchart type=area height=250 :options="chartOptionsLine1" :series="total"/>
                    </v-card>

                </v-flex>
                <v-flex md4 justify-center>
                    <v-card>
                        <apexchart type=area height=250 :options="chartOptionsLine2" :series="resellers"/>
                    </v-card>
                </v-flex>
                <v-flex md4 justify-center>
                    <v-card>
                        <apexchart type=area height=250 :options="chartOptionsArea" :series="profit"/>
                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>

    </v-content>
</template>

<script>
    window.Apex.theme = {
        palette: 'palette8' // upto palette10
    };
    window.Apex.grid = {
        show: true,
        yaxis: {
            lines: {
                show: false
            },
        },
        xaxis: {
            lines: {
                show: false
            }
        },
    };
    window.Apex.dataLabels = {
        enabled: false
    };
    window.Apex.markers = {
        markers: {
            size: 6,
            hover: {
                size: 10
            }
        },
    };
    window.Apex.xaxis = {
        type: 'datetime',
        categories: ["2018-09-19T00:00:00", "2018-09-19T01:30:00", "2018-09-19T02:30:00",
            "2018-09-19T03:30:00", "2018-09-19T04:30:00", "2018-09-19T05:30:00",
            "2018-09-19T06:30:00"
        ],
    };
    window.Apex.yaxis={
        min: 5,
        max: 300
    };
    window.Apex.tooltip = {
        x: {
            format: 'dd/MM/yy HH:mm'
        },
    };
    export default {
        name: "Home",

        data() {
            return {
                chartOptionsLine1: {
                    chart: {
                        id: 'fb',
                        group: 'social',
                    },

                    colors: ['#008FFB'],
                },
                chartOptionsLine2: {
                    chart: {
                        id: 'tw',
                        group: 'social',
                    },
                    colors: ['#546E7A'],

                },
                chartOptionsArea: {
                    chart: {
                        id: 'yt',
                        group: 'social',
                    },
                    colors: ['#00E396'],
                },
                selection: 'one_year',
                total: [{
                    name: 'Total money',
                    data: [32, 51, 65, 151, 51, 123, 253],
                }],
                resellers: [{
                    name: 'Resellers money',
                    data: [11, 20, 8, 31, 22, 89, 80],
                }],

            }
        },
        computed: {
            profit() {
                let dataArray = [];
                this.total[0].data.forEach((item, i) => {
                    dataArray[i] = item - this.resellers[0].data[i];
                    console.log(item, this.resellers[0].data[i], dataArray)
                });
                return [{
                    name: 'Profit',
                    data: dataArray,
                }]
            }
        },
        mounted() {

        },
        beforeCreate() {
            if (!this.$session.exists()) {
                this.$router.push('/')
            }
        },
    }

</script>

<style lang="scss">
    .apexcharts-toolbar,.apexcharts-tooltip{
        z-index: 2 !important;
    }
</style>