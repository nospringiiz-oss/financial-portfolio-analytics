

## Project Overview

This project is a financial portfolio analytics dashboard built with Python, Pandas, NumPy, SQL, MySQL, Power BI, and Matplotlib.

The project analyzes stock portfolio holdings, historical stock prices, sector allocation, investment performance, and risk metrics. It follows a complete data analysis workflow, including raw data inspection, data cleaning, financial metric calculation, SQL-based analysis, MySQL data storage, and Power BI dashboard visualization.

The main goal of this project is to demonstrate practical financial data analysis, portfolio performance measurement, risk analytics, and business intelligence reporting skills.

---

## Tech Stack

- Python
- Pandas
- NumPy
- SQL
- MySQL
- Power BI
- Matplotlib

---

## Dataset

The dataset contains portfolio holdings, historical stock prices, and market index data.

Main files used in this project:

- `Portfolio.csv`
- `Portfolio_prices.csv`
- `Dow_Jones.csv`
- `NASDAQ.csv`
- `SP500.csv`

The core analysis mainly uses:

- `Portfolio.csv` for current portfolio holdings
- `Portfolio_prices.csv` for historical stock price and return data


## Project Structure

financial-portfolio-analytics/
├── data/
│   ├── raw/
│   │   ├── Portfolio.csv
│   │   ├── Portfolio_prices.csv
│   │   ├── Dow_Jones.csv
│   │   ├── NASDAQ.csv
│   │   └── SP500.csv
│   │
│   └── processed/
│       ├── stock_prices_cleaned.csv
│       ├── portfolio_summary.csv
│       ├── risk_metrics.csv
│       └── portfolio_performance.csv
│
├── notebooks/
│   ├── portfolio_analysis.py
│   ├── clean_data.py
│   └── generate_figures.py
│
├── sql/
│   ├── create_tables.sql
│   ├── import_to_mysql.py
│   └── analysis_queries.sql
│
├── powerbi/
│   └── portfolio_dashboard.pbix
│
├── reports/
│   ├── portfolio_report.md
│   └── figures/
│       ├── cumulative_return.png
│       └── drawdown_chart.png
│
├── screenshots/
│   ├── portfolio_overview.png
│   ├── sector_allocation.png
│   ├── risk_analysis.png
│   └── performance_analysis.png
│
├── README.md
└── requirements.txt
<img width="2075" height="1185" alt="c54416f3bbecd42845ff7e839e9a3dd3" src="https://github.com/user-attachments/assets/0eb52c22-28f1-4600-b93b-b09370149a2f" />
<img width="2027" height="1197" alt="2a09ec4749aecffc4ae2e41f5cc06888" src="https://github.com/user-attachments/assets/8910665e-2561-48f2-851c-0f4c9098134e" />
<img width="2059" height="1188" alt="eb60ed30a14743ac075b981c1ebee1b8" src="https://github.com/user-attachments/assets/490bd47e-2d72-4c9a-a496-f7f3b4f6a495" />
<img width="2003" height="1183" alt="55d58191842128713b259ffc12157134" src="https://github.com/user-attachments/assets/230fbbf7-d747-4b53-8053-3fc0279bdb8c" />
