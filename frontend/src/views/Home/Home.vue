<template>
    <v-content color="primary">
        <v-container fluid id="main-container" grid-list-md>
            <v-layout row wrap justify-center>
                <v-flex md4 justify-center>
                   <total-subscribers-chart/>
                </v-flex>
                <v-flex md4 justify-center>
                    <apexchart type=area height=350 :options="chartOptions" :series="series" />

                </v-flex>
            </v-layout>
        </v-container>

    </v-content>
</template>

<script>
    import TotalSubscribersChart from "@/components/Charts/totalSubscribersChart";
    export default {
        name: "Home",
        components: {TotalSubscribersChart},
        data() {
            return {
                series: [{
                    name: 'Inflation',
                    data: [2.3, 3.1, 4.0, 10.1, 4.0, 3.6, 3.2, 2.3, 1.4, 0.8, 0.5, 0.2]
                }],
                chartOptions: {
                    chart: {
                        foreColor: '#fff',
                        toolbar: {
                            show: false
                        },
                    },
                    colors: ['#FCCF31', '#17ead9', '#f02fc2'],
                    stroke: {
                        width: 3
                    },
                    dataLabels: {
                        enabled: false
                    },
                    grid: {
                        borderColor: "#40475D",
                    },
                    xaxis: {
                        axisTicks: {
                            color: '#333'
                        },
                        axisBorder: {
                            color: "#333"
                        }
                    },
                    fill: {
                        type: 'gradient',
                        gradient: {
                            gradientToColors: ['#F55555', '#6078ea', '#6094ea']
                        },
                    },
                    tooltip: {
                        theme: 'dark',
                        x: {
                            // formatter: function (val) {
                            //
                            // }
                        }
                    },
                    yaxis: {
                        decimalsInFloat: 2,
                        opposite: true,
                        labels: {
                            offsetX: -10
                        }
                    }
                }
            }
        }
    }

</script>

<style scoped>

</style>