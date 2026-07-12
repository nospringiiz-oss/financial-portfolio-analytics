from pathlib import Path
import pandas as pd
# 1. Set project paths
BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = BASE_DIR / "data" / "raw"
portfolio_path = RAW_DIR / "Portfolio.csv"
prices_path = RAW_DIR / "Portfolio_prices.csv"

# 2. Read raw CSV files
portfolio = pd.read_csv(portfolio_path)
prices = pd.read_csv(prices_path)

# 3. Basic data inspection
print("shape:", portfolio.shape)
print("\nColumns:")

print(portfolio.columns.tolist())
print("\nFirst 5 rows:")

print(portfolio.head())
print("\nData types:")

print(portfolio.info())

print("\nMissing Value:")
print(portfolio.isnull().sum())

print("\nDuplicated rows:")
print(portfolio.duplicated().sum())

print("\nDuplicated tickers:")
print(portfolio.duplicated(subset =["Ticker"]).sum())

print("\n\n========== Portfolio_prices.csv ==========")
print("shape:")
print(prices.shape)

print("\ncolumns:")
print(prices.columns.tolist())

print("\nFirst 5 rows:")
print(prices.head())

print("\nData Type:")
print(prices.dtypes)

print("\nMissing Value")
print(prices.isnull().sum())

print("\nDuplicated rows:")
print(prices.duplicated().sum())

print("\nDuplicated Date + Ticker:")
print(prices.duplicated(subset = ["Date","Ticker"]).sum())



