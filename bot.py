import ccxt
import time
import datetime

#telling the script which source, and which api is going to get used for our automated botting. 
exchange = ccxt.binance({
    'apiKey': 'INSERT API',
    'secret': 'SECRET API'
})

exchange.load_time_difference()
#in this example we use the trading pair SHIB, and SEI. please remember to commit your own studies, and to analyze the specific indicators more well. This is not an advisor for financial decisions.
buy_time_shib = "22:00"
sell_time_shib = "01:30"
buy_time_sei = "02:06"
sell_time_sei = "21:06"

def get_current_time():
    return datetime.datetime.now().strftime("%H:%M")

#tells the system that the API interagations with Binance should use the maximum number of available USDC capital, if u use BNB, BSC, BTC, ETH, please replace that
#error messages like "Not enough USDC balance to buy SHIB at XX:XX" or successful notifiers like "Bought XXXX at XX:XX: ORDER" are also shown in terminal console for that
def trade():
    current_time = get_current_time()
    
    balance = exchange.fetch_balance()
    usdc_balance = balance['USDC']['free']
    
    if current_time == buy_time_shib:
        if usdc_balance > 0:
            order = exchange.create_market_buy_order('SHIB/USDC', usdc_balance / exchange.fetch_ticker('SHIB/USDC')['last'])
            print(f"Bought SHIB at {current_time}: {order}")
        else:
            print(f"Not enough USDC balance to buy SHIB at {current_time}")
    elif current_time == sell_time_shib:
        shib_balance = balance['SHIB']['free']
        if shib_balance > 0:
            order = exchange.create_market_sell_order('SHIB/USDC', shib_balance)
            print(f"Sold SHIB at {current_time}: {order}")
        else:
            print(f"Not enough SHIB balance to sell at {current_time}")
    
    if current_time == buy_time_sei:
        if usdc_balance > 0:
            order = exchange.create_market_buy_order('SEI/USDC', usdc_balance / exchange.fetch_ticker('SEI/USDC')['last'])
            print(f"Bought SEI at {current_time}: {order}")
        else:
            print(f"Not enough USDC balance to buy SEI at {current_time}")
    elif current_time == sell_time_sei:
        sei_balance = balance['SEI']['free']
        if sei_balance > 0:
            order = exchange.create_market_sell_order('SEI/USDC', sei_balance)
            print(f"Sold SEI at {current_time}: {order}")
        else:
            print(f"Not enough SEI balance to sell at {current_time}")

while True:
    trade()
    time.sleep(60)

"""
Lovely Greetings,
Lahdo Gorieh, Lahdo
LinkedIn.com/in/Lahdo/
"""
