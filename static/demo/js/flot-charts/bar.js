'use strict';

$(document).ready(function(){

    // Chart Data
    var barChartData = [
        {
            label: '2015',
            data: [[1,60], [2,30], [3,50], [4,100], [5,10], [6,90], [7,85]],
            bars: {
                order: 0,
                fillColor: '#fff'
            },
            color: '#fff'
        },

    ];


    // Chart Options
    var barChartOptions = {
        series: {
            bars: {
                show: true,
                barWidth: 0.075,
                fill: 0.1,
                lineWidth: 0
            }
        },
        grid : {
            borderWidth: 1,
            borderColor: 'rgba(255,255,255,0.1)',
            show : true,
            hoverable : true,
            clickable : true
        },
        yaxis: {
            tickColor: 'rgba(255,255,255,0.1)',
            tickDecimals: 0,
            font: {
                lineHeight: 13,
                style: 'normal',
                color: 'rgba(255,255,255,0.75)',
                size: 11
            },
            shadowSize: 0
        },
        xaxis: {
            tickColor: 'rgba(255,255,255,0.1)',
            tickDecimals: 0,
            font: {
                lineHeight: 13,
                style: 'normal',
                color: 'rgba(255,255,255,0.75)',
                size: 11
            },
            shadowSize: 0
        },
        legend:{
            container: '.flot-chart-legends--bar',
            backgroundOpacity: 0.5,
            noColumns: 0,
            lineWidth: 0,
            labelBoxBorderColor: 'rgba(255,255,255,0)'
        }
    };

    // Create chart
    if ($('.flot-bar')[0]) {
        $.plot($('.flot-bar'), barChartData, barChartOptions);
    }
});
