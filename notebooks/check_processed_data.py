from pathlib import Path
import pandas as pd
BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR/"data"/"processed"

prices = pd.read_csv(PROCESSED_DIR/"stock_prices_cleaned.csv")
portfolio = pd.read_csv(PROCESSED_DIR / "portfolio_summary.csv")
risk = pd.read_csv(PROCESSED_DIR / "risk_metrics.csv")

print("========== stock_prices_cleaned.csv ==========")
print("Shape:", prices.shape)
print("Columns:", prices.columns.tolist())
print(prices.head().to_string())

print("\nMissing values:")
print(prices.isnull().sum())

print("\n========== portfolio_summary.csv ==========")
print("Shape:", portfolio.shape)
print("Columns:", portfolio.columns.tolist())
print(portfolio.head().to_string())

print("\nTotal market value:")
print(portfolio["market_value"].sum())

print("\nAllocation sum:")
print(portfolio["allocation_pct"].sum())

print("\n========== risk_metrics.csv ==========")
print("Shape:", risk.shape)
print("Columns:", risk.columns.tolist())
print(risk.head().to_string())