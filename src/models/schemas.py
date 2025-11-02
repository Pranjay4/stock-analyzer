from pydantic import BaseModel
from typing import Optional, List

class FinancialData(BaseModel):
    ticker: str
    revenue: Optional[float] = None
    net_income: Optional[float] = None
    total_debt: Optional[float] = None
    total_equity: Optional[float] = None
    current_assets: Optional[float] = None
    current_liabilities: Optional[float] = None
    free_cash_flow: Optional[float] = None
    year_over_year_growth: Optional[float] = None

class AnalysisResponse(BaseModel):
    metrics: FinancialData
    interpretation: str

class ErrorResponse(BaseModel):
    detail: str