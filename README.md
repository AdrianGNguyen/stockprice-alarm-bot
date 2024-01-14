# stockprice-alarm-bot
This simple Python bot will send a window notification informing you of many stock price actions.
These are the features of the application.
+ Periodically check the real-time market price of many of your chosen stocks.
+ Allow you to add multiple limit-buy and limit-sell price alerts.
+ A dedicated icon tray of the bot for easy access.

**NOTE**: python 3.12 removed Distutils you might need to install setup tools on your machine with:

_pip install setuptools_ 

for more information about the release check this [link](https://docs.python.org/3/whatsnew/3.12.html#:~:text=This%20article%20explains%20the%20new,released%20on%20October%202%2C%202023.) 

## Getting started
+ Clone the repository
+ In your command prompt install these dependencies using these commands:
  
_pip install yfinance_

_pip install winotify_

+ In priceAlarm.py change value of *tickers, upper_limits, lower_limits* according to your chosen stocks.
