 google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawVisualization);


      function drawVisualization() {
        // Some raw data (not necessarily accurate)
        var data = google.visualization.arrayToDataTable([
         ['Date', 'Hours Rendered', 'Offset', 'SL', 'VL', 'EL'],
         ['Apr 11',  12, 0, 0, 0, 0],
         ['Apr 12',  4, 4, 0, 0, 0],
         ['Apr 13', 0, 0, 8, 0, 0],
         ['Apr 14', 0, 0, 0, 0, 0],
         ['Apr 15', 0, 0, 0, 0, 0]
      ]);
        

    var options = {
      title : 'Daily Time Report',
      vAxis: {title: 'Hours'},
      hAxis: {title: 'Date'},
      seriesType: 'bars',
      legend: 'bottom',
    };

    var chart = new google.visualization.ComboChart(document.getElementById('chart_div'));
    chart.draw(data, options);
  }