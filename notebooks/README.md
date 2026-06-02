# Hyperliquid Trader Sentiment Analysis

## Project Overview

This project explores the relationship between Bitcoin market sentiment and Hyperliquid trader performance.

The analysis combines Fear & Greed Index data with historical Hyperliquid trader data to identify patterns between market emotions and trading outcomes.

The goal is to uncover insights that can support smarter trading strategies.

---

## Datasets Used

### 1. Bitcoin Market Sentiment Dataset

Contains market sentiment classification such as:

- Fear
- Greed
- Extreme Greed
- Neutral

Columns include:

- Date
- Classification

### 2. Hyperliquid Historical Trader Data

Contains trader activity and trading information.

Columns include:

- Account
- Coin / Symbol
- Execution Price
- Size Tokens
- Size USD
- Side
- Timestamp
- Start Position
- Direction
- Closed PnL

---

## Objectives

The main objectives of this project are:

- Explore trader performance under different market sentiments
- Discover hidden patterns in trading behavior
- Measure profitability and win rate
- Generate insights for smarter trading strategies

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## Analysis Performed

This project includes:

- Data Cleaning
- Date Formatting
- Dataset Merging
- Sentiment Classification Analysis
- Average PnL Analysis
- Win Rate Analysis
- Data Visualization

---

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python data/src/analysis.py
```

---

## Outputs

Generated files:

- merged_output.csv
- sentiment_analysis.csv
- average_pnl_chart.png
- win_rate_chart.png

All outputs are saved inside the outputs folder.

---

## Key Insight

This project studies how trader profitability changes with market sentiment and identifies which sentiment category produces better trading performance.