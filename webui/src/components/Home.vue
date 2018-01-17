<template>
    <div class="uk-panel uk-panel-box">
        <canvas id="canvas"></canvas>
    </div>
</template>


<script>
    var common = require('../common/common.js');

    export default {
        methods: {
            randomScalingFactor: function() {
            	return (Math.random() > 0.5 ? 1.0 : -1.0) * Math.round(Math.random() * 100);
            }
        },
        attached: function () {
            var config = {
                type: 'line',
                data: {
                    labels: ["January", "February", "March", "April", "May", "June", "July"],
                    datasets: [{
                        label: "dataset - big points",
                        data: [
                            this.randomScalingFactor(),
                            this.randomScalingFactor(),
                            this.randomScalingFactor(),
                            this.randomScalingFactor(),
                            this.randomScalingFactor(),
                            this.randomScalingFactor(),
                            this.randomScalingFactor()
                        ],
                        backgroundColor: this.chartColors.red,
                        borderColor: this.chartColors.red,
                        fill: false,
                        borderDash: [5, 5],
                        pointRadius: 15,
                        pointHoverRadius: 10,
                    }, {
                        label: "dataset - individual point sizes",
                        data: [
                            this.randomScalingFactor(),
                            this.randomScalingFactor(),
                            this.randomScalingFactor(),
                            this.randomScalingFactor(),
                            this.randomScalingFactor(),
                            this.randomScalingFactor(),
                            this.randomScalingFactor()
                        ],
                        backgroundColor: this.chartColors.blue,
                        borderColor: this.chartColors.blue,
                        fill: false,
                        borderDash: [5, 5],
                        pointRadius: [2, 4, 6, 18, 0, 12, 20],
                    }, {
                        label: "dataset - large pointHoverRadius",
                        data: [
                            this.randomScalingFactor(),
                            this.randomScalingFactor(),
                            this.randomScalingFactor(),
                            this.randomScalingFactor(),
                            this.randomScalingFactor(),
                            this.randomScalingFactor(),
                            this.randomScalingFactor()
                        ],
                        backgroundColor: this.chartColors.green,
                        borderColor: this.chartColors.green,
                        fill: false,
                        pointHoverRadius: 30,
                    }, {
                        label: "dataset - large pointHitRadius",
                        data: [
                            this.randomScalingFactor(),
                            this.randomScalingFactor(),
                            this.randomScalingFactor(),
                            this.randomScalingFactor(),
                            this.randomScalingFactor(),
                            this.randomScalingFactor(),
                            this.randomScalingFactor()
                        ],
                        backgroundColor: this.chartColors.yellow,
                        borderColor: this.chartColors.yellow,
                        fill: false,
                        pointHitRadius: 20,
                    }]
                },
                options: {
                    responsive: true,
                    legend: {
                        position: 'bottom',
                    },
                    hover: {
                        mode: 'index'
                    },
                    scales: {
                        xAxes: [{
                            display: true,
                            scaleLabel: {
                                display: true,
                                labelString: 'Month'
                            }
                        }],
                        yAxes: [{
                            display: true,
                            scaleLabel: {
                                display: true,
                                labelString: 'Value'
                            }
                        }]
                    },
                    title: {
                        display: true,
                        text: 'Welcome to Mirage'
                    }
                }
            };
            var ctx = $('#canvas');
            this.myLine = new Chart(ctx, config);
        },
        data() {
            return {
                chartColors: {
                	red: 'rgb(255, 99, 132)',
                	orange: 'rgb(255, 159, 64)',
                	yellow: 'rgb(255, 205, 86)',
                	green: 'rgb(75, 192, 192)',
                	blue: 'rgb(54, 162, 235)',
                	purple: 'rgb(153, 102, 255)',
                	grey: 'rgb(231,233,237)'
                },
                servers:[],
                newServer:{
                    idx:0,
                    name:'',
                    pic_name:'',
                    sn:'',
                    height: 0,
                    props: '',
                    voltage_list:'',
                    node:'',
                    desc:'',
                }
            }
        },
    }
</script>
