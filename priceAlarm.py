
import os 
import time
import yfinance as yf
from winotify import Notification, audio
import pystray
import PIL.Image 
import threading


tickers = ["AAPL", "TSLA", "AMD", "TQQQ"]
upper_limits = [200, 260, 180, 55]
lower_limits = [190, 200, 100, 30]


#price alerts
def alert():
    while True:
       
        last_prices = [yf.Ticker(ticker).history(period="1d")["Close"].iloc[-1] for ticker in tickers]
        print(last_prices)
        time.sleep(45) #change interval for longer delays
        for i in range(len(tickers)):

            # If stock price hit upper limit
            if last_prices[i] > upper_limits[i]:
                toast = Notification(app_id="Stock Alarm Bot",
                                 title ="Price Alert for " + tickers[i],
                                 msg=f"{tickers[i]} has reached a price of {last_prices[i]:.2f}. You might want to sell.",
                                 icon=os.path.join(os.getcwd(),"sell.png"),
                                 duration="long")
            
                toast.add_actions(label="Go to IBKR", launch ="https://www.interactivebrokers.ca/en/home.php") #Change the broker according to your preference
                toast.set_audio(audio.LoopingAlarm6, loop=False)
                toast.show()

        # If stock price hit lower limit
            elif last_prices[i] < lower_limits[i]:
                toast = Notification(app_id="Stock Alarm Bot",
                                 title ="Price Alert for " + tickers[i],
                                 msg=f"{tickers[i]} has reached a price of {last_prices[i]:.2f}. You might want to buy.",
                                 icon=os.path.join(os.getcwd(),"buy.png"),
                                 duration="long")
            
                toast.add_actions(label="Go to IBKR", launch ="https://www.interactivebrokers.ca/en/home.php")
                toast.set_audio(audio.LoopingAlarm8, loop=False)
                toast.show()
            time.sleep(1) #To enable 2 notification to display at the same time
    
threading.Thread(target=alert, daemon=True).start()

#sytem tray
image = PIL.Image.open("bot.png")

def on_clicked(icon, item):
        
        if str(item) == "Exit":
            icon.stop()
            

icon = pystray.Icon("Stock Bot", image, menu=pystray.Menu(
pystray.MenuItem("Exit", on_clicked)
))
icon.run()
