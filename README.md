# Stock Financial Analyzer

A FastAPI web application that analyzes stock financial metrics and provides simple explanations.

## Features
- Fetches financial data using Yahoo Finance API
- Analyzes key metrics:
  - Revenue Growth
  - Net Profit Margin
  - Debt-to-Equity Ratio
  - Current Ratio
- Provides plain-language explanations of financial metrics

## Installation
1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/stock-analyzer.git
   cd stock-analyzer
   ```

2. Create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Start the server:
   ```bash
   uvicorn src.main:app --reload
   ```

2. Open http://localhost:8000 in your browser
3. Enter a stock ticker (e.g., AAPL) and click Analyze

## Project Structure
```
stock-analyzer/
├── src/
│   ├── api/
│   │   ├── financial_data.py
│   │   └── llm.py
│   ├── services/
│   │   └── analysis.py
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   └── templates/
│       └── index.html
└── requirements.txt
```