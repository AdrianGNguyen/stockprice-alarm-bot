
import os 
import time
import yfinance as yf
from winotify import Notification, audio

tickers = ["AAPL", "TSLA", "AMD", "TQQQ"]
upper_limits = [185, 260, 180, 55]
lower_limits = [150, 200, 100, 30]

while True:
    last_prices = [yf.Ticker(ticker).history(period="1d")["Close"].iloc[-1] for ticker in tickers]
    print(last_prices)
    time.sleep(2) #change interval for longer delays
    for i in range(len(tickers)):
        if last_prices[i] > upper_limits[i]:
            toast = Notification(app_id="Stock Alarm Bot",
                                 title ="Price Alert for " + tickers[i],
                                 msg=f"{tickers[i]} has reached a price of {last_prices[i]}. You might want to sell.",
                                 duration="long")
            toast.set_audio(audio.LoopingAlarm6, loop=False)
            toast.show()
        elif last_prices[i] < lower_limits[i]:
            toast = Notification(app_id="Stock Alarm Bot",
                                 title ="Price Alert for " + tickers[i],
                                 msg=f"{tickers[i]} has reached a price of {last_prices[i]}. You might want to buy.",
                                 duration="long")
            toast.set_audio(audio.LoopingAlarm8, loop=False)
            toast.show()
        time.sleep(1) #To enable 2 notification to display at the same time
