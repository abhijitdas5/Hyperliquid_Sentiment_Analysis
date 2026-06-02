import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ===============================
# CREATE OUTPUT DIRECTORY
# ===============================

if not os.path.exists('output'):
    os.makedirs('output')
    
    print("Loading datasets...")
# ===============================
# LOAD DATA
# ===============================

fear = pd.read_csv("data/fear_greed_index.csv")

trade = pd.read_csv("data/historical_data.csv")

# ===============================
# CLEAN FEAR GREED DATA
# ===============================

fear['date'] = pd.to_datetime(fear['date'] , errors='coerce').dt.date

fear.dropna(inplace=True)

# ===============================
# CLEAN TRADER DATA
# ===============================

trade['date'] = pd.to_datetime(trade['Timestamp'] , unit='ms', errors='coerce').dt.date

trade['Close PnL'] = pd.to_numeric(trade['Closed PnL'], errors='coerce')
trade.dropna(subset=['Closed PnL'], inplace=True)
print("Cleaning Completed.")

# ===============================
# MERGE
# ===============================

merged = pd.merge(trade, fear, on='date', how='inner')

print("Merge Completed")
print("ROWS:", merged.shape[0]) # type: ignore

merged.to_csv("outputs/merged_output.csv", index=False) # type: ignore

# ===============================
# FEATURE ENGINEERING
# ===============================

merged['WinTrade'] = merged['Closed PnL'] > 0 # type: ignore

# ===============================
# ANALYSIS
# ===============================

avg_pnl = merged.groupby('classification')['Closed PnL'].mean() # type: ignore

median_pnl = merged.groupby('classification')['Closed PnL'].median() # type: ignore

trade_count = merged.groupby('classification')['Closed PnL'].count() # type: ignore

win_rate = merged.groupby('classification')['WinTrade'].mean() * 100 # type: ignore

summary = pd.DataFrame({
    'AveragePnL': avg_pnl,
    'MedianPnL': median_pnl,
    'TradeCount': trade_count,
    'WinRate': win_rate
})

print(summary)

summary.to_csv("outputs/sentiment_analysis.csv")

# ===============================
# VISUALIZATION
# ===============================

sns.set_style("whitegrid")

# PnL chart
plt.figure(figsize=(8, 6))

sns.barplot(x=summary.index, y=summary['AveragePnL'])

plt.title('Average PnL by Market Sentiment')
plt.xlabel("Fear & Greed Sentiment")

plt.ylabel("Average Closed PnL")

plt.savefig("outputs/average_pnl_chart.png")
plt.close()

# Win Rate chart
plt.figure(figsize=(8, 6))
sns.barplot(x=summary.index, y=summary['WinRate'])
plt.title('Win Rate by Market Sentiment')
plt.xlabel("Fear & Greed Sentiment")
plt.ylabel("Win Rate (%)")

plt.xticks(rotation=20)

plt.tight_layout()
plt.savefig("outputs/win_rate_chart.png")
plt.close()

# ===============================
# INSIGHTS
# ===============================

best = avg_pnl.idxmax()
worst = avg_pnl.idxmin()

print("\n------ INSIGHTS ------")

print("Best Sentiment:", best)

print("Best Average PnL:", round(avg_pnl[best], 2))

print("\nproject Completed Successfully.")

print("Check outputs folder")
