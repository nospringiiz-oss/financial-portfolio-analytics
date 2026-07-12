

USE portfolio_analytics;


-- 1. Check table row counts

SELECT COUNT(*) AS portfolio_rows
FROM portfolio_summary;

SELECT COUNT(*) AS risk_metric_rows
FROM risk_metrics;

SELECT COUNT(*) AS stock_price_rows
FROM stock_prices;



-- 2. Portfolio Overview

SELECT
    COUNT(*) AS number_of_holdings,
    ROUND(SUM(market_value), 2) AS total_market_value,
    ROUND(AVG(market_value), 2) AS average_holding_value,
    ROUND(MAX(market_value), 2) AS largest_holding_value,
    ROUND(MIN(market_value), 2) AS smallest_holding_value
FROM portfolio_summary;



-- 3. Holdings Detail
SELECT
    ticker,
    sector,
    quantity,
    ROUND(current_price, 2) AS current_price,
    ROUND(market_value, 2) AS market_value,
    ROUND(allocation_pct * 100, 2) AS allocation_percentage
FROM portfolio_summary
ORDER BY market_value DESC;



-- 4. Top 10 Holdings by Market Value

SELECT
    ticker,
    sector,
    ROUND(market_value, 2) AS market_value,
    ROUND(allocation_pct * 100, 2) AS allocation_percentage
FROM portfolio_summary
ORDER BY market_value DESC
LIMIT 10;



-- 5. Sector Allocation

SELECT
    sector,
    COUNT(*) AS number_of_stocks,
    ROUND(SUM(market_value), 2) AS sector_market_value,
    ROUND(SUM(allocation_pct) * 100, 2) AS sector_allocation_percentage
FROM portfolio_summary
GROUP BY sector
ORDER BY sector_market_value DESC;



-- 6. Number of Stocks by Sector

SELECT
    sector,
    COUNT(ticker) AS number_of_stocks
FROM portfolio_summary
GROUP BY sector
ORDER BY number_of_stocks DESC;



-- 7. Annualized Volatility Ranking

SELECT
    ticker,
    ROUND(annualized_volatility * 100, 2) AS annualized_volatility_percentage,
    ROUND(max_drawdown * 100, 2) AS max_drawdown_percentage,
    ROUND(sharpe_ratio, 2) AS sharpe_ratio
FROM risk_metrics
ORDER BY annualized_volatility DESC;



-- 8. Top 10 Most Volatile Stocks

SELECT
    ticker,
    ROUND(annualized_volatility * 100, 2) AS annualized_volatility_percentage,
    ROUND(max_drawdown * 100, 2) AS max_drawdown_percentage,
    ROUND(sharpe_ratio, 2) AS sharpe_ratio
FROM risk_metrics
ORDER BY annualized_volatility DESC
LIMIT 10;



-- 9. Worst Maximum Drawdown

SELECT
    ticker,
    ROUND(max_drawdown * 100, 2) AS max_drawdown_percentage,
    ROUND(annualized_volatility * 100, 2) AS annualized_volatility_percentage,
    ROUND(sharpe_ratio, 2) AS sharpe_ratio
FROM risk_metrics
ORDER BY max_drawdown ASC;



-- 10. Top 10 Worst Drawdown Stocks

SELECT
    ticker,
    ROUND(max_drawdown * 100, 2) AS max_drawdown_percentage,
    ROUND(annualized_volatility * 100, 2) AS annualized_volatility_percentage,
    ROUND(sharpe_ratio, 2) AS sharpe_ratio
FROM risk_metrics
ORDER BY max_drawdown ASC
LIMIT 10;



-- 11. Sharpe Ratio Ranking

SELECT
    ticker,
    ROUND(sharpe_ratio, 2) AS sharpe_ratio,
    ROUND(annualized_volatility * 100, 2) AS annualized_volatility_percentage,
    ROUND(max_drawdown * 100, 2) AS max_drawdown_percentage
FROM risk_metrics
ORDER BY sharpe_ratio DESC;



-- 12. Top 10 Sharpe Ratio Stocks
SELECT
    ticker,
    ROUND(sharpe_ratio, 2) AS sharpe_ratio,
    ROUND(annualized_volatility * 100, 2) AS annualized_volatility_percentage,
    ROUND(max_drawdown * 100, 2) AS max_drawdown_percentage
FROM risk_metrics
ORDER BY sharpe_ratio DESC
LIMIT 10;



-- 13. Portfolio Holdings with Risk Metrics

SELECT
    p.ticker,
    p.sector,
    ROUND(p.market_value, 2) AS market_value,
    ROUND(p.allocation_pct * 100, 2) AS allocation_percentage,
    ROUND(r.annualized_volatility * 100, 2) AS annualized_volatility_percentage,
    ROUND(r.max_drawdown * 100, 2) AS max_drawdown_percentage,
    ROUND(r.sharpe_ratio, 2) AS sharpe_ratio
FROM portfolio_summary p
JOIN risk_metrics r
    ON p.ticker = r.ticker
ORDER BY p.market_value DESC;



-- 14. High Allocation and High Volatility Holdings


SELECT
    p.ticker,
    p.sector,
    ROUND(p.market_value, 2) AS market_value,
    ROUND(p.allocation_pct * 100, 2) AS allocation_percentage,
    ROUND(r.annualized_volatility * 100, 2) AS annualized_volatility_percentage,
    ROUND(r.max_drawdown * 100, 2) AS max_drawdown_percentage,
    ROUND(r.sharpe_ratio, 2) AS sharpe_ratio
FROM portfolio_summary p
JOIN risk_metrics r
    ON p.ticker = r.ticker
WHERE p.allocation_pct >= 0.05
ORDER BY r.annualized_volatility DESC;



-- 15. Stock Price Data Coverage

SELECT
    ticker,
    COUNT(*) AS number_of_price_records,
    MIN(date) AS start_date,
    MAX(date) AS end_date
FROM stock_prices
GROUP BY ticker
ORDER BY number_of_price_records DESC;



-- 16. Final Cumulative Return by Ticker

SELECT
    sp.ticker,
    ROUND(sp.cumulative_return * 100, 2) AS final_cumulative_return_percentage
FROM stock_prices sp
JOIN (
    SELECT
        ticker,
        MAX(date) AS latest_date
    FROM stock_prices
    GROUP BY ticker
) latest
    ON sp.ticker = latest.ticker
    AND sp.date = latest.latest_date
ORDER BY sp.cumulative_return DESC;



-- 17. Holdings with Final Cumulative Return

SELECT
    p.ticker,
    p.sector,
    ROUND(p.market_value, 2) AS market_value,
    ROUND(p.allocation_pct * 100, 2) AS allocation_percentage,
    ROUND(sp.cumulative_return * 100, 2) AS final_cumulative_return_percentage
FROM portfolio_summary p
JOIN stock_prices sp
    ON p.ticker = sp.ticker
JOIN (
    SELECT
        ticker,
        MAX(date) AS latest_date
    FROM stock_prices
    GROUP BY ticker
) latest
    ON sp.ticker = latest.ticker
    AND sp.date = latest.latest_date
ORDER BY sp.cumulative_return DESC;



-- 18. Daily Portfolio Performance

SELECT
    date,
    ROUND(portfolio_daily_return * 100, 4) AS portfolio_daily_return_percentage,
    ROUND(portfolio_cumulative_return * 100, 2) AS portfolio_cumulative_return_percentage
FROM portfolio_performance
ORDER BY date;



-- 19. Final Portfolio Cumulative Return

SELECT
    date,
    ROUND(portfolio_cumulative_return * 100, 2) AS final_portfolio_cumulative_return_percentage
FROM portfolio_performance
WHERE date = (
    SELECT MAX(date)
    FROM portfolio_performance
);



-- 20. Average Portfolio Daily Return

SELECT
    ROUND(AVG(portfolio_daily_return) * 100, 4) AS average_portfolio_daily_return_percentage
FROM portfolio_performance;