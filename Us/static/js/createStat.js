var oilCanvas = document.getElementById("eventStat");

Chart.defaults.global.defaultFontFamily = "Lato";
Chart.defaults.global.defaultFontSize = 18;

var oilData = {
    labels: workshops,
    datasets: [
        {
            label: "Dislike",
            data: dislikes,
            backgroundColor: 'rgba(255, 10, 10, 0.3)'
        },
        {
            label: "Like",
            data: likes,
            backgroundColor: 'rgba(10, 255, 10, 0.3)'
        }],
options: {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
        yAxes: [{
            ticks: {
                beginAtZero:true
            }
        }]
    }
}
};

var pieChart = new Chart(oilCanvas, {
  type: 'line',
  data: oilData
});

var oilCanvas1 = document.getElementById("eventStat1");

Chart.defaults.global.defaultFontFamily = "Lato";
Chart.defaults.global.defaultFontSize = 18;

var oilData1 = {
    labels: workshops,
    datasets: [
        {
            label: "Polarity",
            data: polarity,
            backgroundColor: 'rgba(200, 100, 100, 0.3)'
        }],
options: {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
        yAxes: [{
            ticks: {
                beginAtZero:true
            }
        }]
    }
}
};

var pieChart1 = new Chart(oilCanvas1, {
  type: 'bar',
  data: oilData1
});
