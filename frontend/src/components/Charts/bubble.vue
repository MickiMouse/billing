<template>
    <apexchart type=scatter height=350 :options="chartOptions" :series="series" />

</template>

<script>
    function generateDayWiseTimeSeries(baseval, count, yrange) {
        var i = 0;
        var series = [];
        while (i < count) {
            var y = Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;

            series.push([baseval, y]);
            baseval += 86400000;
            i++;
        }
        return series;
    }
    export default {
        name: "bubble",
        data(){
            return{
                series: [{
                    name: 'TEAM 1',
                    data: generateDayWiseTimeSeries(new Date('11 Feb 2017 GMT').getTime(), 20, {
                        min: 10,
                        max: 60
                    })
                },
                    {
                        name: 'TEAM 2',
                        data: generateDayWiseTimeSeries(new Date('11 Feb 2017 GMT').getTime(), 20, {
                            min: 10,
                            max: 60
                        })
                    },
                    {
                        name: 'TEAM 3',
                        data: generateDayWiseTimeSeries(new Date('11 Feb 2017 GMT').getTime(), 30, {
                            min: 10,
                            max: 60
                        })
                    },
                    {
                        name: 'TEAM 4',
                        data: generateDayWiseTimeSeries(new Date('11 Feb 2017 GMT').getTime(), 10, {
                            min: 10,
                            max: 60
                        })
                    },
                    {
                        name: 'TEAM 5',
                        data: generateDayWiseTimeSeries(new Date('11 Feb 2017 GMT').getTime(), 30, {
                            min: 10,
                            max: 60
                        })
                    },
                ],
                chartOptions: {
                    chart: {

                        zoom: {
                            type: 'xy'
                        }
                    },

                    dataLabels: {
                        enabled: false
                    },
                    grid: {
                        xaxis: {
                            showLines: true
                        },
                        yaxis: {
                            showLines: true
                        },
                    },
                    xaxis: {
                        type: 'datetime',

                    },
                    yaxis: {
                        max: 70
                    }
                }
            }
        }
    }
</script>

<style scoped>

</style>