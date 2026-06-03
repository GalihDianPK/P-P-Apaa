  // ────────── Data Fetching ──────────
  async function sendPump(state) {
  try {
    await fetch(`/pump?state=${state}`);
  } catch (error) {
    console.error('pump control failed:', error);
  }
}

async function sendFan(state) {
  try {
    await fetch(`/fan?state=${state}`);
  } catch (error) {
    console.error('fan control failed:', error);
  }
}
  
  async function fetchData() {
    try {
      const res = await fetch('/data');
      const json = await res.json();
      updateGauge(json.moisture);
      updateChart(json.temperature, json.humidity);
      console.log('data:', json);
    } catch (e) {
      console.error('Fetch failed', e);
    }
  }
  setInterval(fetchData, 5000);
  window.onload = fetchData;

  

  // ────────── Speedometer-style Gauge ──────────
  const gaugeCanvas = document.getElementById('radialGauge');
  let gaugeChart;
  if (gaugeCanvas) {
    const ctx = gaugeCanvas.getContext('2d');
    gaugeChart = new Chart(ctx, {
      type: 'doughnut',
      data: {
        datasets: [{
          data: [0, 100],
          backgroundColor: ['#007bff','#eee'],
          needleValue: 0
        }]
      },
      options: {
        rotation: 270,
        circumference: 180,
        cutout: '60%',
        responsive: false,
        plugins: { legend: { display: false } }
      },
      plugins: [{
        id: 'gauge-needle',
        afterDraw(chart) {
          const {ctx, chartArea: {width, height}, config: {data}} = chart;
          let value = data.datasets[0].needleValue;
          const total = data.datasets[0].data.reduce((a,b)=>a+b,0);
          const angle = Math.PI * (1 + value/total);
          const cx = width/2;
          const cy = height;
          ctx.save();
          ctx.translate(cx, cy);
          ctx.rotate(angle);
          ctx.beginPath();
          ctx.moveTo(0, -5);
          ctx.lineTo((height - 20), 0);
          ctx.lineTo(0, 5);
          ctx.fillStyle = '#444';
          ctx.fill();
          ctx.restore();
          // center dot
          ctx.beginPath();
          ctx.arc(cx, cy, 5, 0, 2*Math.PI);
          ctx.fill();
          // text
          ctx.font = '16px sans-serif';
          ctx.fillStyle = '#000';
          ctx.textAlign = 'center';
          ctx.fillText(value + '%', cx, cy - 30);
        }
      }]
    });
  }

  function updateGauge(val) {
    if (!gaugeChart) return;
    val = Number(val);
    gaugeChart.data.datasets[0].data[0] = val;
    gaugeChart.data.datasets[0].data[1] = 100 - val;
    gaugeChart.data.datasets[0].needleValue = val;
    gaugeChart.update();
  }

  // ────────── Line Chart: Temperature & Humidity ──────────
  const lineCtx = document.getElementById('lineChart');
  let lineChart;
  if (lineCtx) {
    const ctx = lineCtx.getContext('2d');
    lineChart = new Chart(ctx, {
      type: 'line',
      data: { labels: [], datasets: [
        { label: 'Temperature (°C)', borderColor: 'red', data: [], fill: false },
        { label: 'Humidity (%)', borderColor: 'blue', data: [], fill: false }
      ]},
      options: { responsive: true, scales: { x: {display:false}, y: {beginAtZero:true} } }
    });
  }

  function updateChart(temp, hum) {
    if (!lineChart) return;
    const t = new Date().toLocaleTimeString();
    lineChart.data.labels.push(t);
    lineChart.data.datasets[0].data.push(temp);
    lineChart.data.datasets[1].data.push(hum);
    if (lineChart.data.labels.length > 20) {
      lineChart.data.labels.shift();
      lineChart.data.datasets.forEach(ds => ds.data.shift());
    }
    lineChart.update();
  }