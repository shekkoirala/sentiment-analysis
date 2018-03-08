window.onload = function () {

    var dps = []; // dataPoints
    var chart = new CanvasJS.Chart("chartContainer", {
        title :{
            text: "Tweet analysis"
        },
        axisY: {
            includeZero: false
        },      
        data: [{
            type: "line",
            dataPoints: dps
        }]
    });
    
    var xVal = 10;
    var yVal = 100; 
    var updateInterval = 1000;
    var dataLength = 10; // number of dataPoints visible at any point
    
    var updateChart = function (count) {
    
        count = count || 1;
    
        for (var j = 0; j < count; j++) {
            //aile chai yo static data xa NLP ko data aayexi chai json file bata update lidai plot garxa ani live dekhinxa
            //yesma milau ta bipin 
            var obj = JSON.parse('{ "xVAL":"10", "yVAL":"100"}');
            xVal=parseInt(obj.xVAL);
            yVal=parseInt(obj.yVAL);
            //yVal = yVal +  Math.round(5 + Math.random() *(-5-5));
            dps.push({
                x: xVal,
                y: yVal
            });
           // xVal++;
        }
    
        if (dps.length > dataLength) {
            dps.shift();
        }
    
        chart.render();
    };
    
    updateChart(dataLength);
    setInterval(function(){updateChart()}, updateInterval);
}