<template>
    <v-content color="primary">
        <v-container fluid id="main-container" grid-list-md>
            <v-layout row wrap justify-center>
                <v-flex md4 justify-center>
                    <v-card>
                        <apexchart type=area height=350 :options="chartOptions" :series="series"/>
                    </v-card>
                </v-flex>
                <v-flex md4 justify-center>
                    <v-card>
                        <column/>
                    </v-card>
                </v-flex>
                <v-flex md4 justify-center>
                    <v-card>
                       <bar/>
                    </v-card>
                </v-flex>
                <v-flex md6 justify-center>
                    <v-card>
                        <pie/>
                    </v-card>
                </v-flex>
                <v-flex md6 justify-center>
                    <v-card>
                        <bubble/>
                    </v-card>
                </v-flex>
                <v-flex md12 justify-center>
                    <v-card>
                        <tetris/>
                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>

    </v-content>
</template>

<script>
    import axios from "axios";
    import Column from "../../components/Charts/column";
    import Bar from "../../components/Charts/bar";
    import Pie from "../../components/Charts/pie";
    import Bubble from "../../components/Charts/bubble";
    import Tetris from "../../components/Charts/tetris";

    window.Apex.theme = {
        palette: 'palette1' // upto palette10
    };

    export default {
        name: "Home",
        components: {Tetris, Bubble, Pie, Bar, Column},
        data() {
            return {
                selection: 'one_year',

                series: [{
                    name:'Cards',
                    data: []
                },
                    {
                        name:'Subscribers',
                        data: []
                    }],
                chartOptions: {
                    legend: {
                        position: 'top',
                        horizontalAlign: 'left'
                    },
                    stacked: true,
                    annotations: {
                    },
                    dataLabels: {
                        enabled: false
                    },

                    markers: {
                        size: 0,
                        style: 'hollow',
                    },
                    xaxis: {
                        type: 'datetime',
                        // min: new Date().getTime(),
                        tickAmount: 6,
                    },
                    tooltip: {
                        x: {
                            format: 'hh:mm dd-MMM-yyyy'
                        }
                    },
                    fill: {
                        type: 'gradient',
                        gradient: {
                            shadeIntensity: 1,
                            opacityFrom: 0.7,
                            opacityTo: 0.9,
                            stops: [0, 100]
                        }
                    },
                }
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
        methods: {
            getData() {
                axios.get(`${this.$hostname}/api/dashboard/`)
                    .then((response) => {
                        console.log(response.data)
                        if (response.status === 200) {
                            const xCard = response.data.xCard;
                            const yCard = response.data.yCard;
                            const dataCard = xCard.map((item, i) => {
                                return [new Date(item).getTime(), yCard[i]]
                            });
                            const xSub = response.data.xSub;
                            const ySub = response.data.ySub;
                            const dataSub = xSub.map((item, i) => {
                                return [new Date(item).getTime(), ySub[i]]
                            });
                            console.log(dataCard)
                            this.series[0].data = dataCard;
                            this.series[1].data = dataSub;
                        }
                    }).catch((error) => {
                    this.text = "Connection error";
                    console.log(error)
                    this.snackbar = true;
                });
            },
        },
        mounted() {
            this.getData();
        },
        beforeCreate() {
            if (!this.$session.exists()) {
                this.$router.push('/')
            }
            if(!this.$session.get('isSuperuser')){
                this.$router.push('/cards')
            }
        },
    }

</script>

<style lang="scss">
    .apexcharts-toolbar, .apexcharts-tooltip {
        z-index: 2 !important;
    }
</style>