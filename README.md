# Stock Price Alarm Bot
This simple Python bot will send a window notification informing you of many stock price actions.
These are the features of the application.
+ Periodically check the real-time market price of many of your chosen stocks.
+ Allow you to add multiple limit-buy and limit-sell price alerts.
+ A dedicated icon tray of the bot for easy access.

This Python script monitors the stock prices of specified tickers using the Yahoo Finance API (via the yfinance library). It runs a background thread that periodically checks the last closing prices of selected stocks. If a stock's price surpasses predefined upper or lower limits, a desktop notification is triggered with relevant information. Additionally, a system tray icon is used to provide an option to exit the script.

**NOTE**: python 3.12 removed Distutils you might need to install setup tools on your machine with:

_pip install setuptools_ 

for more information about the release check this [link](https://docs.python.org/3/whatsnew/3.12.html#:~:text=This%20article%20explains%20the%20new,released%20on%20October%202%2C%202023.) 
+ Ensure that you have a reliable internet connection as the script relies on fetching real-time stock data from Yahoo Finance.
+ The script is designed to work on Windows due to the use of the winotify library for notifications.

## Features
+ Stock Price Monitoring:

The script monitors the stock prices of specified tickers using the Yahoo Finance API, providing real-time data on selected stocks.
 Price Alert System:

The script generates desktop notifications when a stock's price exceeds predefined upper or lower limits, giving users timely alerts for potential selling or buying opportunities.
+ System Tray Integration:

The script includes a system tray icon for a non-intrusive presence. Users can easily exit the script using the "Exit" option in the system tray menu, providing a convenient and user-friendly interface.

+ In priceAlarm.py change value of *tickers, upper_limits, lower_limits* according to your chosen stocks.
## How to use
+ Install required libraries: pip install yfinance winotify pystray Pillow.
+ Place images (sell.png, buy.png, bot.png) in the same directory as the script.
+ Update tickers, upper_limits, and lower_limits based on the stocks you want to monitor and their corresponding price limits.
Run the script.


