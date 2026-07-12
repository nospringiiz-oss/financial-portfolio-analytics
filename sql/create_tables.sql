CREATE DATABASE IT NOT EXIST portfolio_analytics;
DROP TABLE IF EXISTS stock_prices;
DROP TABLE IF EXISTS portfolio_summary;
DROP TABLE IF EXISTS risk_metrics;

CREATE TABLE stock_prices(
id INT PRIMARY KEY AUTO_INCREMENT,
    date DATE,
    ticker VARCHAR(20),
    open_price DOUBLE,
    high_price DOUBLE,
    low_price DOUBLE,
    close_price DOUBLE,
    adjusted_price DOUBLE,
    daily_return DOUBLE,
    volume BIGINT,
    cumulative_return DOUBLE,
    return_index DOUBLE,
    running_max DOUBLE,
    drawdown DOUBLE
);
CREATE TABLE portfolio_summary (
    id INT PRIMARY KEY AUTO_INCREMENT,
    ticker VARCHAR(20),
    quantity INT,
    sector VARCHAR(100),
    current_price DOUBLE,
    original_weight DOUBLE,
    market_value DOUBLE,
    allocation_pct DOUBLE
);

CREATE TABLE risk_metrics (
    id INT PRIMARY KEY AUTO_INCREMENT,
    ticker VARCHAR(20),
    average_daily_return DOUBLE,
    daily_volatility DOUBLE,
    max_drawdown DOUBLE,
    annualized_volatility DOUBLE,
    sharpe_ratio DOUBLE
);
