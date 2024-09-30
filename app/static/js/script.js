let loadChart;

async function sendRequest() {
    const cache = document.getElementById('cache').checked;
    const data = document.getElementById('data').value;

    const response = await fetch(`/request?cache=${cache}&data=${data}`);
    const result = await response.json();

    document.getElementById('response').innerHTML = `Response: ${result.message}`;
    updateLoad();
}

async function updateLoad() {
    const response = await fetch('/load');
    const load = await response.json();

    const labels = Object.keys(load);
    const data = Object.values(load);

    if (loadChart) {
        loadChart.destroy();
    }

    const ctx = document.getElementById('loadChart').getContext('2d');
    loadChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Server Load',
                data: data,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

// Poll server load every 5 seconds
setInterval(updateLoad, 5000);
