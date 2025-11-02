def test_fetch_financial_data(mocker):
    # Mock the API response
    mock_response = {
        "symbol": "AAPL",
        "financials": {
            "incomeStatement": {
                "revenue": [100000, 120000, 140000],  # Example revenue data
                "netIncome": [20000, 25000, 30000],  # Example net income data
            },
            "balanceSheet": {
                "totalDebt": [50000, 60000, 70000],  # Example debt data
                "totalEquity": [100000, 120000, 140000],  # Example equity data
            },
            "cashFlow": {
                "freeCashFlow": [15000, 18000, 20000],  # Example free cash flow data
            },
        },
    }

    mocker.patch('src.api.financial_data.fetch_financial_data', return_value=mock_response)

    # Call the function to test
    data = fetch_financial_data("AAPL")

    assert data["symbol"] == "AAPL"
    assert len(data["financials"]["incomeStatement"]["revenue"]) == 3

def test_calculate_metrics():
    # Example financial data
    financial_data = {
        "revenue": [100000, 120000, 140000],
        "netIncome": [20000, 25000, 30000],
        "totalDebt": [50000, 60000, 70000],
        "totalEquity": [100000, 120000, 140000],
        "freeCashFlow": [15000, 18000, 20000],
    }

    # Calculate metrics
    revenue_growth = calculate_revenue_growth(financial_data["revenue"])
    net_profit_margin = calculate_net_profit_margin(financial_data["netIncome"], financial_data["revenue"])
    debt_to_equity = calculate_debt_to_equity(financial_data["totalDebt"], financial_data["totalEquity"])
    current_ratio = calculate_current_ratio(financial_data["totalDebt"], financial_data["totalEquity"])
    free_cash_flow_trend = calculate_free_cash_flow_trend(financial_data["freeCashFlow"])

    assert revenue_growth == 0.4  # Example expected value
    assert net_profit_margin == 0.25  # Example expected value
    assert debt_to_equity == 0.5  # Example expected value
    assert current_ratio == 0.5  # Example expected value
    assert free_cash_flow_trend == [15000, 18000, 20000]  # Example expected value

def test_api_endpoint(client):
    response = client.get("/api/financials/AAPL")
    assert response.status_code == 200
    assert "financials" in response.json()