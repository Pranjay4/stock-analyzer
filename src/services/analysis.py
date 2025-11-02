from typing import Dict, Any
import pandas as pd
import logging

def get_field_value(df: pd.DataFrame, field_names: list) -> float:
    """Safely extract value from DataFrame using multiple possible field names."""
    for name in field_names:
        if name in df.index:
            value = df.loc[name].iloc[0]
            if pd.notna(value):
                return float(value)
    return 0.0

def analyze_financials(data: Dict[str, Any]) -> Dict[str, float]:
    try:
        income_stmt = data["income_statement"]
        balance_sheet = data["balance_sheet"]

        # Revenue and growth
        revenue_fields = ['Total Revenue', 'Revenue']
        revenue = get_field_value(income_stmt, revenue_fields)
        prev_revenue = income_stmt.loc[revenue_fields[0]].iloc[1] if revenue_fields[0] in income_stmt.index else 0
        revenue_growth = ((revenue - prev_revenue) / prev_revenue * 100) if prev_revenue else 0

        # Net income and margin
        net_income = get_field_value(income_stmt, ['Net Income'])
        net_margin = (net_income / revenue * 100) if revenue else 0

        # Balance sheet metrics
        equity = get_field_value(balance_sheet, [
            'Total Stockholder Equity',
            'Stockholders Equity',
            'Total Equity'
        ])
        
        if equity == 0:
            print("Warning: Could not find stockholder equity")
            equity = 1  # Prevent division by zero
            
        total_debt = get_field_value(balance_sheet, ['Total Debt', 'Total Liabilities'])
        current_assets = get_field_value(balance_sheet, ['Total Current Assets'])
        current_liabilities = get_field_value(balance_sheet, ['Total Current Liabilities'])

        return {
            "revenue_growth": round(revenue_growth, 2),
            "net_margin": round(net_margin, 2),
            "debt_equity": round(total_debt / equity, 2),
            "current_ratio": round(current_assets / current_liabilities, 2) if current_liabilities else 0
        }
    except Exception as e:
        print(f"Analysis error: {str(e)}")
        raise Exception(f"Failed to analyze financials: {str(e)}")