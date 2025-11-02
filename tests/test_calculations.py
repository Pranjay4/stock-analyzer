def test_revenue_growth():
    # Example test for revenue growth calculation
    from src.services.calculations import calculate_revenue_growth

    previous_year_revenue = 100000
    current_year_revenue = 120000
    expected_growth = 0.2  # 20%

    assert calculate_revenue_growth(previous_year_revenue, current_year_revenue) == expected_growth


def test_net_profit_margin():
    # Example test for net profit margin calculation
    from src.services.calculations import calculate_net_profit_margin

    net_income = 30000
    total_revenue = 150000
    expected_margin = 0.2  # 20%

    assert calculate_net_profit_margin(net_income, total_revenue) == expected_margin


def test_debt_to_equity_ratio():
    # Example test for debt-to-equity ratio calculation
    from src.services.calculations import calculate_debt_to_equity_ratio

    total_debt = 50000
    total_equity = 100000
    expected_ratio = 0.5  # 50%

    assert calculate_debt_to_equity_ratio(total_debt, total_equity) == expected_ratio


def test_current_ratio():
    # Example test for current ratio calculation
    from src.services.calculations import calculate_current_ratio

    current_assets = 80000
    current_liabilities = 40000
    expected_ratio = 2.0  # 2:1

    assert calculate_current_ratio(current_assets, current_liabilities) == expected_ratio


def test_free_cash_flow_trend():
    # Example test for free cash flow trend calculation
    from src.services.calculations import calculate_free_cash_flow_trend

    cash_flows = [20000, 25000, 30000]
    expected_trend = "Increasing"

    assert calculate_free_cash_flow_trend(cash_flows) == expected_trend