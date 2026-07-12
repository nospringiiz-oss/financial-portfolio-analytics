from pathlib import Path
import pandas as pd
import numpy as np

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

portfolio_path = RAW_DIR / "Portfolio.csv"
prices_path = RAW_DIR / "Portfolio_prices.csv"

portfolio = pd.read_csv(portfolio_path)
prices = pd.read_csv(prices_path)

# Clean column names
portfolio.columns = portfolio.columns.str.strip()
prices.columns = prices.columns.str.strip()

prices = prices.rename(columns = {
    "Date": "date",
    "Ticker": "ticker",
    "Open": "open_price",
    "High": "high_price",
    "Low": "low_price",
    "Close": "close_price",
    "Adjusted": "adjusted_price",
    "Returns": "daily_return",
    "Volume": "volume"
})

portfolio = portfolio.rename(columns = {
    "Ticker": "ticker",
    "Quantity": "quantity",
    "Sector": "sector",
    "Close": "current_price",
    "Weight": "original_weight"
})

# Convert data types
prices["date"] = pd.to_datetime(prices["date"],errors = "coerce") 
prices["ticker"] = prices["ticker"].astype(str).str.strip().str.upper()

numeric_price_cols = [
    "open_price",
    "high_price",
    "low_price",
    "close_price",
    "adjusted_price",
    "daily_return",
    "volume"
]

for col in numeric_price_cols:
    prices[col] = pd.to_numeric(prices[col],errors = "coerce")


portfolio["sector"] = portfolio["sector"].fillna("Unknown").astype(str).str.strip()

# Remove invalid rows
prices = prices.dropna(subset = ["date", "ticker", "close_price"])
portfolio = portfolio.dropna(subset=["ticker", "quantity", "current_price"])
prices = prices[prices["close_price"]> 0]
portfolio = portfolio[portfolio["quantity"] > 0]
portfolio = portfolio[portfolio["current_price"] > 0]

# Remove duplicates
prices = prices.drop_duplicates()
portfolio = portfolio.drop_duplicates()

prices = prices.drop_duplicates(subset=["date", "ticker"], keep="last")
portfolio = portfolio.drop_duplicates(subset=["ticker"], keep="last")

# Sort data
prices = prices.sort_values(['ticker','date']).reset_index(drop = True)
portfolio = portfolio.sort_values('ticker').reset_index(drop = True)

# Calculate cumulative return
prices["cumulative_return"] = (
    1 + prices["daily_return"]
).groupby(prices["ticker"]).cumprod() - 1

# Calculate drawdown

prices["return_index"] = (
    1 + prices["daily_return"]
).groupby(prices["ticker"]).cumprod()

prices["running_max"] = prices.groupby("ticker")["return_index"].cummax()

prices["drawdown"] = (
    prices["return_index"] - prices["running_max"]
) / prices["running_max"]


# Calculate risk metrics

risk_metrics = prices.groupby("ticker").agg(
    average_daily_return=("daily_return", "mean"),
    daily_volatility=("daily_return", "std"),
    max_drawdown=("drawdown", "min")
).reset_index()

risk_metrics["annualized_volatility"] = risk_metrics["daily_volatility"] * np.sqrt(252)

risk_metrics["sharpe_ratio"] = (
    risk_metrics["average_daily_return"] / risk_metrics["daily_volatility"]
) * np.sqrt(252)

risk_metrics["sharpe_ratio"] = risk_metrics["sharpe_ratio"].replace([np.inf, -np.inf], np.nan)
risk_metrics["sharpe_ratio"] = risk_metrics["sharpe_ratio"].fillna(0)


#Calculate portfolio summary

portfolio["market_value"] = portfolio["quantity"] * portfolio["current_price"]

total_market_value = portfolio["market_value"].sum()

portfolio["allocation_pct"] = portfolio["market_value"] / total_market_value

# Save processed data
prices.to_csv(PROCESSED_DIR/"stock_prices_cleaned.csv", index=False)
portfolio.to_csv(PROCESSED_DIR/"portfolio_summary.csv", index=False)
risk_metrics.to_csv(PROCESSED_DIR / "risk_metrics.csv", index=False)

# Calculate portfolio performance
portfolio_weights = portfolio[["ticker", "allocation_pct"]]

portfolio_returns = prices.merge(
    portfolio_weights,
    on="ticker",
    how="inner"
)

portfolio_returns["weighted_daily_return"] = (
    portfolio_returns["daily_return"] * portfolio_returns["allocation_pct"]
)

portfolio_performance = (
    portfolio_returns
    .groupby("date", as_index=False)
    .agg(portfolio_daily_return=("weighted_daily_return", "sum"))
)

portfolio_performance["portfolio_cumulative_return"] = (
    1 + portfolio_performance["portfolio_daily_return"]
).cumprod() - 1

portfolio_performance.to_csv(
    PROCESSED_DIR / "portfolio_performance.csv",
    index=False
)
