from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR/"data"/"processed"
FIGURE_DIR = BASE_DIR / "reports" / "figures"

FIGURE_DIR.mkdir(parents=True, exist_ok=True)

prices = pd.read_csv(PROCESSED_DIR / "stock_prices_cleaned.csv")
portfolio = pd.read_csv(PROCESSED_DIR / "portfolio_summary.csv")

top_tickers = (
    portfolio.sort_values("market_value", ascending=False)
    .head(8)["ticker"]
    .tolist()
)
top_prices = prices[prices["ticker"].isin(top_tickers)]

# Cumulative return chart
plt.figure(figsize=(12,6))
for ticker in top_tickers:
    temp = top_prices[top_prices["ticker"]==ticker]
    plt.plot(temp["date"], temp["cumulative_return"], label=ticker)
    plt.title("Cumulative Return of Top Portfolio Holdings")
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.legend()
plt.tight_layout()
plt.savefig(FIGURE_DIR / "cumulative_return.png", dpi=300)
plt.close()

# Drawdown chart
plt.figure(figsize=(12, 6))

for ticker in top_tickers:
    temp = top_prices[top_prices["ticker"] == ticker]
    plt.plot(temp["date"], temp["drawdown"], label=ticker)

plt.title("Drawdown of Top Portfolio Holdings")
plt.xlabel("Date")
plt.ylabel("Drawdown")
plt.legend()
plt.tight_layout()

plt.savefig(FIGURE_DIR / "drawdown_chart.png", dpi=300)
plt.close()

print(FIGURE_DIR / "cumulative_return.png")
print(FIGURE_DIR / "drawdown_chart.png")