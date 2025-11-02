document.getElementById('analyzeForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const ticker = document.getElementById('ticker').value;
    const resultsDiv = document.getElementById('results');
    
    try {
        resultsDiv.innerHTML = '<div class="loading">Analyzing...</div>';
        resultsDiv.style.display = 'block';
        
        const response = await fetch('/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ ticker: ticker })
        });
        
        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.detail || 'Analysis failed');
        }
        
        // Display results
        resultsDiv.innerHTML = `
            <div class="metrics">
                <div class="metric-card">
                    <h3>Revenue Growth</h3>
                    <p>${data.metrics.revenue_growth}%</p>
                </div>
                <div class="metric-card">
                    <h3>Net Margin</h3>
                    <p>${data.metrics.net_margin}%</p>
                </div>
                <div class="metric-card">
                    <h3>Debt-to-Equity</h3>
                    <p>${data.metrics.debt_equity}</p>
                </div>
                <div class="metric-card">
                    <h3>Current Ratio</h3>
                    <p>${data.metrics.current_ratio}</p>
                </div>
            </div>
            <div class="analysis">
                <h3>Analysis</h3>
                <p>${data.explanation}</p>
            </div>
        `;
    } catch (error) {
        resultsDiv.innerHTML = `
            <div class="error">
                <h3>Error Analyzing Stock</h3>
                <p>${error.message}</p>
                <p>Please verify the ticker symbol and try again.</p>
            </div>`;
    }
});