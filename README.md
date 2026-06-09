# Bursa Malaysia Stock Analysis Using Python

# Overview
This project analyzes five Bursa Malaysia stocks using Python and real market data obtained from Yahoo Finance. The analysis evaluates recent stock price movements, estimates investment returns based on an RM1,000 capital allocation, performs portfolio screening using pandas, and visualizes stock performance through charts.

The project was developed as part of a business analytics programming exercise to demonstrate data retrieval, data analysis, portfolio evaluation, and financial data visualization using Python.

## Objectives
* Retrieve Bursa Malaysia stock data using yfinance.
* Analyze stock performance over a recent one-month period.
* Simulate an RM1,000 investment in each selected stock.
* Calculate returns and portfolio performance metrics.
* Perform data filtering and GroupBy analysis using pandas.
* Visualize stock trends and portfolio performance using matplotlib.

## Stocks Analyzed
  1. Inari Amertron (0166.KL) - Technology 
  2. Press Metal (8869.KL) - Industrial
  3. IOI Corporation (1961.KL) - Plantation 
  4. Tenaga Nasional (5347.KL) - Utilities
  5. IHH Healthcare (5225.KL) - Healthcare 

These stocks were selected from different sectors to provide portfolio diversification and allow comparison of performance across industries.

## Function Used
* Python
* yfinance
* pandas
* matplotlib
* numpy

## Project Features
### Stock Analysis

For each stock, the program calculates:
* Yesterday Closing Price
* Today Closing Price
* Daily Return
* Number of Shares Purchasable with RM1,000
* Estimated Total Return
* Return Percentage

### Portfolio Screening
Using pandas slicing, a summary table is generated containing:
* Ticker
* Previous Closing Price
* Latest Closing Price
* Estimated Total Return
* Return Percentage

### Performance Classification
Stocks are categorized into:
* Negative Return
* Moderate Return
* High Return
GroupBy analysis is then used to calculate the average estimated return for each category.

### Data Visualization
Two charts are generated:
1. Closing Price Trend (Line Chart)
2. Return Percentage Comparison (Bar Chart)

## Output

The program produces:
* Stock Analysis DataFrame
* Portfolio Summary Table
* Performance Category Analysis
* Closing Price Trend Chart
* Return Percentage Comparison Chart


## Author
Moganapirya (299360)
Business Analytics Programming Individual Assignment
Universiti Utara Malaysia
