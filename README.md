\# Quantitative Trading Strategy Backtest



\## Overview

This project implements and evaluates a systematic momentum-based trading strategy using Python.  

It demonstrates the end-to-end quantitative research workflow, including data collection, signal generation, portfolio construction, backtesting, and performance evaluation.



The project is intentionally simple and realistic, designed to clearly showcase quantitative thinking and coding ability.



\---



\## Strategy Description

\*\*Momentum Strategy\*\*



Assets are selected based on recent performance. The strategy takes long positions in assets with positive momentum and remains out of assets with negative momentum.



\- Momentum signal: 20‑day historical return

\- Position rule:

&#x20; - Long (1) if momentum > 0

&#x20; - No position (0) otherwise

\- Portfolio construction: Equal‑weighted across active positions

\- Rebalancing frequency: Daily

\- Transaction costs: 0.1% per trade

\- No leverage or short selling



\---



\## Methodology

\- Historical price data retrieved using Yahoo Finance ('yfinance')

\- Clean price data processed using Pandas

\- Signals constructed using rolling percentage returns

\- Positions shifted by one day to avoid look‑ahead bias

\- Strategy backtested using daily returns

\- Performance evaluated using standard quantitative metrics



\---



\## Performance Metrics

The strategy is evaluated using the following metrics:



\- Total Return

\- Annualized Volatility

\- Sharpe Ratio

\- Maximum Drawdown

\- Hit Ratio (percentage of profitable days)



\---



\## Key Results

Backtest results over the sample period show strong risk‑adjusted performance:



\- \*\*Sharpe Ratio:\*\* \~2.7  

\- \*\*Maximum Drawdown:\*\* \~‑7%  

\- \*\*Volatility:\*\* \~11%  

\- \*\*Hit Ratio:\*\* \~42%  



Results are in‑sample and intended for demonstration and learning purposes.



\---



\## Project Structure

quant-trading-strategy-backtest/

│

├── data/

│   └── price\_data.csv

│

├── notebooks/

│   └── strategy\_research.ipynb

│

├── src/

│   ├── data\_loader.py

│   ├── signals.py

│   ├── backtest.py

│   ├── performance.py

│

├── results/

│   └── performance\_summary.csv

│

├── README.md

└── requirements.txt



\---



\## Technologies Used

\- Python

\- Pandas

\- NumPy

\- Matplotlib

\- yfinance

\- Jupyter Notebook



\---



\## Key Takeaways

\- Momentum strategies can deliver strong risk‑adjusted returns in trending markets

\- Proper backtesting methodology (no look‑ahead bias, transaction costs) is essential

\- Clean project structure improves readability and reproducibility

\- The project demonstrates practical quantitative research skills suitable for entry‑level quant, trading, or data roles

