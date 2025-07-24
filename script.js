// Medical Dashboard JavaScript
// Implementing functionality based on design profile

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all components
    generateCalendar();
    createCharts();
    addInteractivity();
});

// Generate Calendar Days
function generateCalendar() {
    const calendarDays = document.getElementById('calendarDays');
    const currentDate = new Date();
    const currentDay = currentDate.getDate();
    const year = currentDate.getFullYear();
    const month = currentDate.getMonth();
    
    // Get first day of month and number of days
    const firstDay = new Date(year, month, 1);
    const lastDay = new Date(year, month + 1, 0);
    const daysInMonth = lastDay.getDate();
    const startingDayOfWeek = (firstDay.getDay() + 6) % 7; // Convert to Monday = 0
    
    // Clear existing days
    calendarDays.innerHTML = '';
    
    // Add empty cells for days before month starts
    for (let i = 0; i < startingDayOfWeek; i++) {
        const emptyDay = document.createElement('div');
        emptyDay.className = 'calendar-day empty';
        calendarDays.appendChild(emptyDay);
    }
    
    // Add days of the month
    for (let day = 1; day <= daysInMonth; day++) {
        const dayElement = document.createElement('div');
        dayElement.className = 'calendar-day';
        dayElement.textContent = day;
        
        // Highlight current day
        if (day === currentDay) {
            dayElement.classList.add('current');
        }
        
        // Add example selected day (day 16)
        if (day === 16) {
            dayElement.classList.add('selected');
        }
        
        // Add click handler
        dayElement.addEventListener('click', function() {
            // Remove previous selection
            document.querySelectorAll('.calendar-day.selected').forEach(el => {
                el.classList.remove('selected');
            });
            // Add selection to clicked day (unless it's current day)
            if (!dayElement.classList.contains('current')) {
                dayElement.classList.add('selected');
            }
        });
        
        calendarDays.appendChild(dayElement);
    }
}

// Create Charts using Chart.js
function createCharts() {
    // Chart.js default configuration for dark theme
    Chart.defaults.color = '#b0bec5';
    Chart.defaults.backgroundColor = '#16213e';
    
    // In Patient Consultation Chart
    const inPatientCtx = document.getElementById('inPatientChart').getContext('2d');
    new Chart(inPatientCtx, {
        type: 'bar',
        data: {
            labels: ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'],
            datasets: [{
                data: [250, 180, 320, 380, 290, 420, 350],
                backgroundColor: '#00d4aa',
                borderColor: '#00d4aa',
                borderWidth: 0,
                borderRadius: 4,
                borderSkipped: false,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    backgroundColor: '#0f1829',
                    titleColor: '#ffffff',
                    bodyColor: '#b0bec5',
                    borderColor: '#00d4aa',
                    borderWidth: 1
                }
            },
            scales: {
                x: {
                    grid: {
                        display: false
                    },
                    ticks: {
                        color: '#78909c',
                        font: {
                            size: 10
                        }
                    },
                    border: {
                        color: '#78909c'
                    }
                },
                y: {
                    display: false,
                    grid: {
                        display: false
                    }
                }
            },
            animation: {
                duration: 1000,
                easing: 'easeOutQuart'
            }
        }
    });
    
    // Out Patient Consultation Chart
    const outPatientCtx = document.getElementById('outPatientChart').getContext('2d');
    new Chart(outPatientCtx, {
        type: 'bar',
        data: {
            labels: ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'],
            datasets: [{
                data: [120, 150, 180, 95, 110, 200, 250],
                backgroundColor: '#ffc107',
                borderColor: '#ffc107',
                borderWidth: 0,
                borderRadius: 4,
                borderSkipped: false,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    backgroundColor: '#0f1829',
                    titleColor: '#ffffff',
                    bodyColor: '#b0bec5',
                    borderColor: '#ffc107',
                    borderWidth: 1
                }
            },
            scales: {
                x: {
                    grid: {
                        display: false
                    },
                    ticks: {
                        color: '#78909c',
                        font: {
                            size: 10
                        }
                    },
                    border: {
                        color: '#78909c'
                    }
                },
                y: {
                    display: false,
                    grid: {
                        display: false
                    }
                }
            },
            animation: {
                duration: 1000,
                easing: 'easeOutQuart'
            }
        }
    });
}

// Add Interactive Functionality
function addInteractivity() {
    // Stat cards hover effects
    const statCards = document.querySelectorAll('.stat-card');
    statCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
    
    // Table row hover effects
    const tableRows = document.querySelectorAll('.appointments-table tbody tr');
    tableRows.forEach(row => {
        row.addEventListener('mouseenter', function() {
            this.style.backgroundColor = '#0f1829';
        });
        
        row.addEventListener('mouseleave', function() {
            this.style.backgroundColor = 'transparent';
        });
    });
    
    // Action button interactions
    const actionButtons = document.querySelectorAll('.action-btn');
    actionButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Add click animation
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 100);
            
            // Handle specific actions
            if (this.textContent === 'This Week') {
                console.log('Filter by This Week');
                // Add actual filtering logic here
            } else if (this.textContent.includes('View All')) {
                console.log('View All Appointments');
                // Add navigation logic here
            }
        });
    });
    
    // Add smooth animations for elements entering viewport
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Observe all cards and animate them in
    document.querySelectorAll('.card, .stat-card').forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(card);
    });
}

// Utility function to update stats (can be called with real data)
function updateStats(newData) {
    const statValues = document.querySelectorAll('.stat-value');
    const statTitles = ['$105', '105', '20', '5']; // Default values
    
    if (newData && Array.isArray(newData)) {
        statValues.forEach((element, index) => {
            if (newData[index] !== undefined) {
                // Animate number change
                animateValue(element, element.textContent, newData[index], 1000);
            }
        });
    }
}

// Animate number changes
function animateValue(element, start, end, duration) {
    const startNum = parseInt(start.replace(/\D/g, '')) || 0;
    const endNum = parseInt(end.replace(/\D/g, '')) || 0;
    const range = endNum - startNum;
    const prefix = start.replace(/[\d]/g, '');
    let startTime = null;
    
    function step(currentTime) {
        if (startTime === null) startTime = currentTime;
        const timeElapsed = currentTime - startTime;
        const progress = Math.min(timeElapsed / duration, 1);
        const value = Math.floor(progress * range + startNum);
        element.textContent = prefix + value;
        
        if (progress < 1) {
            requestAnimationFrame(step);
        }
    }
    
    requestAnimationFrame(step);
}

// Responsive chart resize handler
window.addEventListener('resize', function() {
    // Chart.js automatically handles resize, but we can add custom logic here
    setTimeout(() => {
        Chart.instances.forEach(chart => {
            chart.resize();
        });
    }, 100);
});

// Mock data update (simulates real-time updates)
function simulateDataUpdate() {
    setInterval(() => {
        // Randomly update some statistics
        const randomStats = [
            '$' + (100 + Math.floor(Math.random() * 50)),
            String(100 + Math.floor(Math.random() * 20)),
            String(15 + Math.floor(Math.random() * 10)),
            String(3 + Math.floor(Math.random() * 5))
        ];
        
        // Uncomment to enable automatic updates
        // updateStats(randomStats);
    }, 30000); // Update every 30 seconds
}

// Initialize data simulation (uncomment to enable)
// simulateDataUpdate();