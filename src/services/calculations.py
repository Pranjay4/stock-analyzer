def calculate_debt_to_equity(total_debt, total_equity):
    if total_equity == 0:
        return float('inf')  # Avoid division by zero
    return total_debt / total_equity

def calculate_current_ratio(current_assets, current_liabilities):
    if current_liabilities == 0:
        return float('inf')  # Avoid division by zero
    return current_assets / current_liabilities

def calculate_net_profit_margin(net_income, revenue):
    if revenue == 0:
        return 0  # Avoid division by zero
    return net_income / revenue

def calculate_revenue_growth(previous_revenue, current_revenue):
    if previous_revenue == 0:
        return float('inf')  # Avoid division by zero
    return (current_revenue - previous_revenue) / previous_revenue

def calculate_free_cash_flow(cash_flow_from_operations, capital_expenditures):
    return cash_flow_from_operations - capital_expenditures