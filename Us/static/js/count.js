var countCanvasAll = document.getElementsByClassName("countGraph");
var events = Array.from(document.getElementsByClassName("summarycard__left"));

console.log(events);
Chart.defaults.global.defaultFontFamily = "Lato";
Chart.defaults.global.defaultFontSize = 18;

events.forEach(function(elem,index){
    console.log("xxxxxxxxxxx", registered[index]);
    var countCanvas = countCanvasAll[index];
    var countData = {
        labels: [
        "Registered",
        "Slots Left"
        ],
        datasets: [
            {
                data: [registered[index],120-registered[index]],
                backgroundColor: [
                    "#FF6384",
                    "#6384FF"
                ]
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
    
    var pieChart = new Chart(countCanvas, {
      type: 'doughnut',
      data: countData
    });
    
})
