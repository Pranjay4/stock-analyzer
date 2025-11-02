import yfinance as yf
from typing import Dict, Any

def fetch_financial_data(ticker: str) -> Dict[str, Any]:
    try:
        stock = yf.Ticker(ticker)
        
        # Get financial statements
        income_stmt = stock.financials
        balance_sheet = stock.balance_sheet
        
        if income_stmt.empty or balance_sheet.empty:
            raise ValueError(f"No financial data available for {ticker}")
        
        # Debug logging
        print(f"Balance Sheet Columns: {balance_sheet.columns.tolist()}")
        print(f"Balance Sheet Items: {balance_sheet.index.tolist()}")
        print(f"Income Statement Items: {income_stmt.index.tolist()}")
        
        return {
            "income_statement": income_stmt,
            "balance_sheet": balance_sheet
        }
    except Exception as e:
        raise Exception(f"Failed to fetch data for {ticker}: {str(e)}")