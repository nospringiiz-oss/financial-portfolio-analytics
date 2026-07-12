from pathlib import Path
from urllib.parse import quote_plus

import pandas as pd
from sqlalchemy import create_engine, text



# 1. Project paths

BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"

stock_prices_path = PROCESSED_DIR / "stock_prices_cleaned.csv"
portfolio_path = PROCESSED_DIR / "portfolio_summary.csv"
risk_path = PROCESSED_DIR / "risk_metrics.csv"



# MySQL connection settings


MYSQL_USER = "root"
MYSQL_PASSWORD = quote_plus("zjc593930050") 
MYSQL_HOST = "localhost"
MYSQL_PORT = "3306"
MYSQL_DATABASE = "portfolio_analytics"



server_engine = create_engine(
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/?charset=utf8mb4"
)

with server_engine.begin() as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {MYSQL_DATABASE}"))


engine = create_engine(
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8mb4"
)



stock_prices = pd.read_csv(stock_prices_path)
portfolio = pd.read_csv(portfolio_path)
risk_metrics = pd.read_csv(risk_path)



# Keep useful columns only


stock_prices = stock_prices[
    [
        "date",
        "ticker",
        "open_price",
        "high_price",
        "low_price",
        "close_price",
        "adjusted_price",
        "daily_return",
        "volume",
        "cumulative_return",
        "return_index",
        "running_max",
        "drawdown",
    ]
]

portfolio = portfolio[
    [
        "ticker",
        "quantity",
        "sector",
        "current_price",
        "original_weight",
        "market_value",
        "allocation_pct",
    ]
]

risk_metrics = risk_metrics[
    [
        "ticker",
        "average_daily_return",
        "daily_volatility",
        "max_drawdown",
        "annualized_volatility",
        "sharpe_ratio",
    ]
]

stock_prices["date"] = pd.to_datetime(stock_prices["date"]).dt.date



# Import into MySQL

portfolio.to_sql(
    name="portfolio_summary",
    con=engine,
    if_exists="replace",
    index=False,
)

risk_metrics.to_sql(
    name="risk_metrics",
    con=engine,
    if_exists="replace",
    index=False,
)

stock_prices.to_sql(
    name="stock_prices",
    con=engine,
    if_exists="replace",
    index=False,
    chunksize=1000,
    method="multi",
)



# Verify row counts

with engine.connect() as conn:
    portfolio_count = conn.execute(text("SELECT COUNT(*) FROM portfolio_summary")).scalar()
    risk_count = conn.execute(text("SELECT COUNT(*) FROM risk_metrics")).scalar()
    stock_count = conn.execute(text("SELECT COUNT(*) FROM stock_prices")).scalar()

print("Data imported into MySQL successfully.")
print("portfolio_summary rows:", portfolio_count)
print("risk_metrics rows:", risk_count)
print("stock_prices rows:", stock_count)