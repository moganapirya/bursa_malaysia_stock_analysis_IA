
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np

def fetch_stock_data(tickers, period='1mo'):
    data = yf.download(tickers, period=period, progress=False)['Close']
    return data

def calculate_stock_metrics(tickers, investment_capital=1000):
    data = yf.download(tickers, period='1mo', progress=False)['Close'].dropna()

    results = {
        'Ticker': [],
        'Yesterday Closing Price (RM)': [],
        'Today Closing Price (RM)': [],
        'Daily Return (RM)': [],
        'Number of Shares Purchasable': [],
        'Estimated Total Return (RM)': [],
        'Return Percentage (%)': []
    }
    
    for ticker in tickers:
        yesterday_price = data[ticker].iloc[-2]
        today_price = data[ticker].iloc[-1]
        daily_return = today_price - yesterday_price
        shares_purchasable = investment_capital / yesterday_price
        estimated_total_return = shares_purchasable * daily_return
        return_percentage = (daily_return / yesterday_price) * 100
        results['Ticker'].append(ticker)
        results['Yesterday Closing Price (RM)'].append(round(yesterday_price, 4))
        results['Today Closing Price (RM)'].append(round(today_price, 4))
        results['Daily Return (RM)'].append(round(daily_return, 4))
        results['Number of Shares Purchasable'].append(round(shares_purchasable, 2))
        results['Estimated Total Return (RM)'].append(round(estimated_total_return, 2))
        results['Return Percentage (%)'].append(round(return_percentage, 2))
    
    df = pd.DataFrame(results)
    return df
stocks = ['0166.KL', '8869.KL', '1961.KL', '5347.KL', '5225.KL']
stock_names = ['Inari Amertron', 'Press Metal', 'IOI Corp', 'Tenaga Nasional', 'IHH Healthcare']
sectors = ['Tech', 'Industrial', 'Plantation', 'Utilities', 'Healthcare']

# Question 1: Generate analysis DataFrame
df_analysis = calculate_stock_metrics(stocks)
print("\nBursa Malaysia Stock Analysis for 1-Month Period")
print(df_analysis.to_string(index=False))
print("\n")

df_main = df_analysis.copy()

# QUESTION 2: DATA FILTERING AND GROUPBY ANALYSIS 
# Portfolio Summary Table using slicing
print(" PORTFOLIO SUMMARY TABLE")
# Using pandas slicing to create portfolio summary
portfolio_summary = df_main[['Ticker', 'Yesterday Closing Price (RM)', 
                              'Today Closing Price (RM)', 'Estimated Total Return (RM)', 
                              'Return Percentage (%)']].copy()
portfolio_summary.columns = ['Ticker', 'Previous Closing Price', 'Latest Closing Price', 
                              'Estimated Total Return', 'Return Percentage (%)']

print(portfolio_summary.to_string(index=False))
print("\n")

#  GroupBy Analysis with Performance Classification
print("PERFORMANCE CATEGORY CLASSIFICATION AND GROUPBY ANALYSIS")

def classify_performance(return_pct):
    if return_pct < 0:
        return 'Negative Return'
    elif return_pct <= 2:
        return 'Moderate Return'
    else:
        return 'High Return'

# Add Performance Category column
df_main['Performance Category'] = df_main['Return Percentage (%)'].apply(classify_performance)

print("\nStock Classification by Performance Category:")
print(df_main[['Ticker', 'Return Percentage (%)', 'Performance Category']].to_string(index=False))

# GroupBy analysis
print("\n\nAverage Estimated Total Return by Performance Category:")
groupby_result = df_main.groupby('Performance Category')['Estimated Total Return (RM)'].mean()
print(groupby_result)
print("\n")

# QUESTION 3: DATA VISUALIZATION 

# 1-month data for charting
data_full = yf.download(stocks, period='1mo', progress=False)['Close']
ticker_to_name = dict(zip(stocks, stock_names))

# Chart 1: Closing Price Trend
plt.figure(figsize=(12, 6))
for ticker in stocks:
    label = f"{ticker} - {ticker_to_name.get(ticker, '')}"
    plt.plot(data_full.index, data_full[ticker], marker='o', label=label, linewidth=2)

plt.title('Closing Price Trend - 5 Bursa Malaysia Stocks (1-Month Period)', fontsize=14, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Closing Price (RM)', fontsize=12)
plt.legend(loc='best', fontsize=10)
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('chart1_closing_price_trend.png', dpi=300, bbox_inches='tight')
plt.show()

print("\nChart 1: Closing Price Trend - Saved as 'chart1_closing_price_trend.png'")

# Chart 2: Return Percentage Comparison
plt.figure(figsize=(12, 6))
colors = ['green' if x > 0 else 'red' for x in df_main['Return Percentage (%)']]
labels = [f"{ticker}\n{ticker_to_name.get(ticker, '')}" for ticker in df_main['Ticker']]
bars = plt.bar(labels, df_main['Return Percentage (%)'], color=colors, alpha=0.7, edgecolor='black')

plt.title('Return Percentage Comparison - 5 Bursa Malaysia Stocks', fontsize=14, fontweight='bold')
plt.xlabel('Stock Ticker and Name', fontsize=12)
plt.ylabel('Return Percentage (%)', fontsize=12)
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
plt.grid(True, alpha=0.3, axis='y')

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.2f}%', ha='center', va='bottom' if height > 0 else 'top', fontsize=10)

plt.tight_layout()
plt.savefig('chart2_return_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

print("Chart 2: Return Percentage Comparison - Saved as 'chart2_return_comparison.png'")
print("\n")

# Optional: Display summary statistics
print("SUMMARY STATISTICS:")
print(df_main[['Ticker', 'Yesterday Closing Price (RM)', 'Today Closing Price (RM)', 
               'Return Percentage (%)']].describe().to_string())
