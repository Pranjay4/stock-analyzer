from typing import Dict

def get_explanation(metrics: Dict[str, float], company: str) -> str:
    """Generate a basic analysis of financial metrics."""
    
    analysis_parts = []
    
    # Revenue Growth Analysis
    if metrics['revenue_growth'] > 20:
        growth_analysis = f"Strong revenue growth at {metrics['revenue_growth']}%"
    elif metrics['revenue_growth'] > 0:
        growth_analysis = f"Positive but moderate revenue growth at {metrics['revenue_growth']}%"
    else:
        growth_analysis = f"Declining revenue with growth at {metrics['revenue_growth']}%"
    analysis_parts.append(growth_analysis)
    
    # Net Margin Analysis
    if metrics['net_margin'] > 20:
        margin_analysis = f"Excellent profit margins at {metrics['net_margin']}%"
    elif metrics['net_margin'] > 10:
        margin_analysis = f"Good profit margins at {metrics['net_margin']}%"
    else:
        margin_analysis = f"Low profit margins at {metrics['net_margin']}%"
    analysis_parts.append(margin_analysis)
    
    # Debt to Equity Analysis
    if metrics['debt_equity'] < 0.5:
        debt_analysis = "Conservative debt levels"
    elif metrics['debt_equity'] < 1.5:
        debt_analysis = "Moderate debt levels"
    else:
        debt_analysis = "High debt levels - potential risk"
    analysis_parts.append(debt_analysis)
    
    # Current Ratio Analysis
    if metrics['current_ratio'] > 2:
        liquidity_analysis = "Strong liquidity position"
    elif metrics['current_ratio'] > 1:
        liquidity_analysis = "Adequate liquidity"
    else:
        liquidity_analysis = "Potential liquidity concerns"
    analysis_parts.append(liquidity_analysis)
    
    # Combine all analyses
    analysis = f"Analysis for {company}:\n\n" + "\n".join(f"• {part}" for part in analysis_parts)
    
    return analysis