document.addEventListener('DOMContentLoaded', function() {
    // Enhanced chart initialization
    if (typeof performanceChart !== 'undefined') {
        performanceChart.options = {
            ...performanceChart.options,
            elements: {
                line: {
                    tension: 0.3
                },
                point: {
                    radius: 0,
                    hoverRadius: 6,
                    backgroundColor: 'rgba(0, 240, 255, 1)',
                    borderWidth: 2
                }
            },
            plugins: {
                legend: {
                    labels: {
                        color: '#e0e0e0',
                        font: {
                            family: "'Exo 2', sans-serif"
                        }
                    }
                },
                tooltip: {
                    backgroundColor: 'rgba(30, 30, 47, 0.9)',
                    titleColor: '#ffffff',
                    bodyColor: '#e0e0e0',
                    borderColor: 'rgba(138, 43, 226, 0.5)',
                    borderWidth: 1
                }
            },
            scales: {
                x: {
                    grid: {
                        color: 'rgba(255, 255, 255, 0.05)'
                    },
                    ticks: {
                        color: '#b8b8d1'
                    }
                },
                y: {
                    grid: {
                        color: 'rgba(255, 255, 255, 0.05)'
                    },
                    ticks: {
                        color: '#b8b8d1'
                    }
                }
            }
        };
        performanceChart.update();
    }
    
    // Table row hover effects
    document.querySelectorAll('.table-dark tr').forEach(row => {
        row.addEventListener('mouseenter', function() {
            this.style.transform = 'translateX(4px)';
        });
        row.addEventListener('mouseleave', function() {
            this.style.transform = '';
        });
    });
    
    // Chart period switcher
    document.querySelectorAll('.btn-chart').forEach(btn => {
        btn.addEventListener('click', function() {
            document.querySelectorAll('.btn-chart').forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            // Here you would typically fetch new data for the selected period
            console.log('Selected period:', this.dataset.period);
        });
    });
});