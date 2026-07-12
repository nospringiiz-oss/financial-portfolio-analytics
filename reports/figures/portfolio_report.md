# Financial Portfolio Analytics Report

## 1. Objective

The objective of this project is to analyze stock portfolio performance using historical stock price data and current portfolio holding data.

This project focuses on portfolio valuation, sector allocation, investment performance, and risk analysis. The final output is an interactive Power BI dashboard that helps users understand the current portfolio structure, historical performance, and risk exposure.

The project demonstrates a complete financial data analysis workflow, including data inspection, data cleaning, financial metric calculation, SQL analysis, MySQL data storage, Matplotlib visualization, and Power BI dashboard reporting.

---

## 2. Dataset Description

The dataset contains portfolio holdings, historical stock prices, and market index data.

The main files used in this project are:

- `Portfolio.csv`
- `Portfolio_prices.csv`
- `Dow_Jones.csv`
- `NASDAQ.csv`
- `SP500.csv`

The core analysis mainly uses:

- `Portfolio.csv` for current portfolio holdings
- `Portfolio_prices.csv` for historical stock price and return data

`Portfolio.csv` contains current holding information, including ticker, quantity, sector, close price, and portfolio weight.

`Portfolio_prices.csv` contains historical stock price data, including date, ticker, open price, high price, low price, close price, adjusted price, daily return, and volume.

The market index files can be used for future benchmark comparison, such as comparing portfolio performance with S&P 500, NASDAQ, or Dow Jones.

---

## 3. Data Inspection

Before cleaning the data, the raw CSV files were inspected using Python and Pandas.

The inspection process included:

- Checking dataset shape
- Reviewing column names
- Previewing the first rows
- Checking data types
- Checking missing values
- Checking duplicate rows
- Checking duplicate tickers
- Checking duplicate date and ticker combinations

For `Portfolio.csv`, each row represents one current stock holding.

For `Portfolio_prices.csv`, each row represents one stock price record on one trading date.

The key uniqueness rules were:

```text
Portfolio.csv: ticker should be unique
Portfolio_prices.csv: date + ticker should be unique
```

The inspection showed that the dataset was relatively clean. There were no missing values, no duplicated rows, and no duplicated key records.

---

## 4. Data Cleaning and Processing

Python and Pandas were used to clean and prepare the data.

The main data cleaning and processing steps were:

1. Loaded raw CSV files.
2. Standardized column names.
3. Converted date fields into datetime format.
4. Standardized ticker symbols.
5. Sorted historical price data by ticker and date.
6. Calculated cumulative return.
7. Calculated return index and drawdown.
8. Calculated market value and allocation percentage for each holding.
9. Calculated risk metrics for each stock.
10. Calculated portfolio-level daily return and cumulative return.

The processed datasets were saved into the `data/processed/` folder.

Generated processed files:

- `stock_prices_cleaned.csv`
- `portfolio_summary.csv`
- `risk_metrics.csv`
- `portfolio_performance.csv`

---

## 5. Portfolio Valuation

Portfolio market value was calculated for each stock holding.

```text
Market Value = Quantity × Current Price
```

The total portfolio market value was calculated by summing the market value of all holdings.

Allocation percentage was calculated as:

```text
Allocation Percentage = Holding Market Value / Total Portfolio Market Value
```

These calculations allow the dashboard to show:

- Total portfolio value
- Top holdings
- Stock-level allocation
- Sector-level allocation
- Portfolio concentration

The Portfolio Overview page in Power BI presents the main portfolio summary, including total market value, number of holdings, average holding value, largest holding value, market value by ticker, and asset allocation by sector.

---

## 6. Sector Allocation Analysis

Sector allocation analysis was used to evaluate the industry exposure of the portfolio.

The dashboard shows:

- Total number of sectors
- Largest sector value
- Number of holdings
- Market value by sector
- Sector allocation percentage
- Number of stocks by sector
- Sector holding details

This analysis helps identify whether the portfolio is concentrated in a small number of industries.

A high allocation in one sector may indicate sector concentration risk. For example, if one sector accounts for a large percentage of total market value, the portfolio may become more sensitive to sector-specific market events.

---

## 7. Risk Analysis

Risk metrics were calculated for each stock using historical daily returns.

The main risk metrics are:

### Annualized Volatility

Annualized volatility measures how much a stock's return fluctuates over a year.

```text
Annualized Volatility = Standard Deviation of Daily Returns × √252
```

A higher annualized volatility indicates greater price fluctuation and higher uncertainty.

### Maximum Drawdown

Maximum drawdown measures the largest decline from a historical peak.

A more negative drawdown means the stock experienced a larger historical loss from its previous high.

### Sharpe Ratio

Sharpe Ratio measures risk-adjusted performance.

A higher Sharpe Ratio indicates better return relative to risk.

The Risk Analysis page compares stocks using:

- Annualized volatility
- Maximum drawdown
- Sharpe Ratio
- Risk metrics summary table

This allows users to identify high-risk stocks and stocks with stronger risk-adjusted performance.

---

## 8. Performance Analysis

The performance analysis uses historical price data to visualize stock and portfolio performance over time.

The dashboard includes:

- Ticker filter
- Close price trend by ticker
- Cumulative return by ticker
- Drawdown by ticker
- Portfolio cumulative return over time

### Close Price Trend by Ticker

This chart shows how selected stocks' close prices changed over time.

### Cumulative Return by Ticker

This chart compares the cumulative return of selected stocks.

This metric is calculated at the individual stock level. It should not be interpreted as the total portfolio return.

### Drawdown by Ticker

This chart shows historical drawdown for selected stocks.

It helps users understand downside risk over time.

### Portfolio Cumulative Return Over Time

This chart shows the cumulative return of the whole portfolio.

It was calculated using weighted daily returns:

```text
Portfolio Daily Return = Σ(Stock Daily Return × Allocation Percentage)
```

The portfolio cumulative return provides a portfolio-level performance view, which is different from individual stock cumulative return.

---

## 9. SQL Analysis

Processed datasets were imported into MySQL for SQL-based analysis.

The project includes SQL queries for:

- Portfolio total market value
- Number of holdings
- Top holdings
- Sector market value
- Sector allocation percentage
- Number of stocks by sector
- Annualized volatility ranking
- Maximum drawdown ranking
- Sharpe Ratio ranking
- Combined holding and risk analysis
- Final cumulative return by ticker

Example SQL query for sector allocation:

```sql
SELECT
    sector,
    COUNT(*) AS number_of_stocks,
    ROUND(SUM(market_value), 2) AS sector_market_value,
    ROUND(SUM(allocation_pct) * 100, 2) AS sector_allocation_percentage
FROM portfolio_summary
GROUP BY sector
ORDER BY sector_market_value DESC;
```

This query helps identify which sectors account for the largest share of the portfolio.

---

## 10. Power BI Dashboard Design

The Power BI dashboard contains four pages.

### Page 1: Portfolio Overview

This page provides a high-level summary of the portfolio.

It includes:

- Total market value
- Number of holdings
- Average holding value
- Largest holding value
- Market value by ticker
- Asset allocation by sector
- Top holdings table

### Page 2: Sector Allocation

This page analyzes sector exposure and concentration.

It includes:

- Total sectors
- Largest sector value
- Number of holdings
- Market value by sector
- Sector allocation percentage
- Number of stocks by sector
- Sector holding details

### Page 3: Risk Analysis

This page compares risk metrics across portfolio holdings.

It includes:

- Average annualized volatility
- Worst maximum drawdown
- Best Sharpe Ratio
- High volatility holdings
- Annualized volatility by ticker
- Maximum drawdown by ticker
- Sharpe Ratio by ticker
- Risk metrics summary table

### Page 4: Performance Analysis

This page shows historical performance trends.

It includes:

- Ticker filter
- Close price trend by ticker
- Cumulative return by ticker
- Drawdown by ticker
- Portfolio cumulative return over time

---

## 11. Key Findings

The portfolio contains 27 stock holdings across multiple sectors.

The sector allocation dashboard shows how total market value is distributed across industries. This helps identify whether the portfolio is concentrated in a small number of sectors.

The risk analysis shows that some holdings have high annualized volatility and severe maximum drawdown. These stocks may contribute more to portfolio risk.

The cumulative return chart shows that some low-priced or highly volatile stocks can produce very large percentage movements. For clearer comparison, the dashboard includes a ticker filter so users can analyze selected holdings separately.

The portfolio cumulative return chart provides a broader view of overall portfolio performance by using weighted daily returns.

---

## 12. Limitations

This project has several limitations.

First, the portfolio uses a static holding structure. The analysis assumes that allocation percentages remain fixed during the historical period.

Second, transaction history is not included in the original dataset. Therefore, the project focuses on current holdings and historical performance rather than realized profit and loss from actual trades.

Third, the Sharpe Ratio calculation uses a simplified assumption and does not include a risk-free rate.

Fourth, the portfolio performance calculation is based on weighted stock returns and does not account for dividends, transaction costs, taxes, or rebalancing.

These limitations can be addressed in future versions of the project.

---

## 13. Future Improvements

Future improvements could include:

- Adding transaction history analysis
- Calculating realized and unrealized profit and loss
- Comparing portfolio performance with S&P 500, NASDAQ, and Dow Jones benchmarks
- Including dividend-adjusted returns
- Adding monthly return analysis
- Adding rolling volatility
- Adding Value at Risk
- Adding portfolio rebalancing simulation
- Connecting Power BI directly to MySQL
- Automating the data pipeline

---

## 14. Conclusion

This project demonstrates a complete financial data analysis workflow.

It covers data inspection, data cleaning, financial metric calculation, MySQL data storage, SQL analysis, Matplotlib visualization, and Power BI dashboard development.

The project shows practical skills in:

- Financial data preparation
- Portfolio valuation
- Sector allocation analysis
- Risk measurement
- Performance analysis
- SQL querying
- Dashboard reporting

This project is suitable for demonstrating skills relevant to financial data analyst, data analyst, BI analyst, finance data intern, and risk analytics intern roles.
