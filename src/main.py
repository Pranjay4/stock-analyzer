from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from .api.financial_data import fetch_financial_data
from .api.llm import get_explanation
from .services.analysis import analyze_financials
from pydantic import BaseModel
import os

app = FastAPI()

# Get the current file's directory
BASE_DIR = Path(__file__).resolve().parent

# Mount static files and templates with correct paths
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# Add health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

class StockRequest(BaseModel):
    ticker: str

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analyze")
async def analyze_stock(stock_request: StockRequest):
    try:
        print(f"Analyzing ticker: {stock_request.ticker}")
        financial_data = fetch_financial_data(stock_request.ticker)
        metrics = analyze_financials(financial_data)
        explanation = get_explanation(metrics, stock_request.ticker)
        return {"metrics": metrics, "explanation": explanation}
    except Exception as e:
        print(f"Error processing request: {str(e)}")
        raise HTTPException(
            status_code=400, 
            detail=f"Could not analyze stock {stock_request.ticker}: {str(e)}"
        )