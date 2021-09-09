from smartapi import SmartConnect #from smartapi.SmartConnect import SmartConnect
import pandas as pd
import requests
import login as l
import time
import math
import numpy as np

############################ Session Block #############
#login api call
obj=SmartConnect(api_key=l.api_key)
data = obj.generateSession(l.user_name,l.password)
refreshToken= data['data']['refreshToken']

#fetch the feedtoken
feedToken=obj.getfeedToken()
l.feed_token = feedToken
#fetch User Profile
userProfile=obj.getProfile(refreshToken)
print(userProfile)

############################ End of Session Block #############

############################ Symbol Mapping Block #############

Dailydata = {}
def intializeSymbolTokenMap():
    url = 'https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json'
    d = requests.get(url).json()
    global token_df
    token_df = pd.DataFrame.from_dict(d)
    token_df['expiry'] = pd.to_datetime(token_df['expiry'])
    token_df = token_df.astype({'strike': float})
    l.token_map = token_df
    print("In Initialze TokenInfo")
    print(token_df)

def getTokenInfo (symbol, exch_seg ='NSE'):
    df = l.token_map
    print(df)
    if exch_seg == 'NSE':
        eq_df = df[(df['exch_seg'] == 'NSE') & (df['symbol'].str.contains('EQ')) ]
        print("In Get TokenInfo")
        print(eq_df)
        return eq_df[eq_df['name'] ==symbol]

print ("Starting...")

stocks = ['SBIN', 'SRF', 'TATAMOTORS']

intializeSymbolTokenMap()

for ticker in stocks:
    tokendetails = getTokenInfo(ticket,'NSE').iloc[0]
    symbol = tokendetails['symbol']
    token = tokendetails['symbol']
    Dailydata[ticker] = OHLCHistory(str(symbol),str(token), "ONE_DAY", "2021-02-08 00:00", "2021-06-05 00:00")

print("End of Algo")


############################ End of Symbol Mapping Block #############



############################ OHLC Block #############

def OHLCHistory(symbol,token,interval,fdate,todate):
    try:
        historicParam={       
        "exchange": "NSE",
        "tradingsymbol":symbol,
        "symboltoken": token,
        "interval": interval,
        "fromdate": fdate,
        "todate": todate
        }

        history = obj.getCandleData(historicParam)['data']
        history = pd.DataFrame(history)

        history = history.rename(
            columns={0: "Datetime", 1: "open", 2: "high", 3: "low", 4: "close", 5: "Volume"})

        history['Datetime'] = pd.to_datetime(history['Datetime'])
        history = history.set_index('Datetime')

        return history
    except Exception as e:
        print("API failed: {}".format(e))

minute5data = OHLCHistory("SBIN-EQ", "3045", "FIVE_MINUTE", "2021-06-03 00:00", "2021-06-04 15:30")
print("5 minute data Live:")
my_df = pd.DataFrame(minute5data)
print(my_df)


############################ End of OHLC Block #############
  
############################ Order Placement Block #############
"""
def place_order(symbol,token,qty,exch_seg,buy_sell,ordertype,price):
    try:
        orderparams = {
            "variety":"NORMAL",
            "tradingsymbol":symbol,
            "symboltoken":token,
            "transactiontype":buy_sell,
            "exchange":exch_seg,
            "ordertype":ordertype,
            "producttype":"INTRADAY",
            "duration":"DAY",
            "price":price,
            "squareoff":"0",
            "stoploss":"0",
            "quantity":qty
            }
        orderId=obj.placeOrder(orderparams)
        print("The order id is: {}".format(orderId))
    except Exception as e:
        print("Order placement failed: {}".format(e))              

print(place_order("SBIN-EQ", "3045",1,'NSE','BUY','MARKET','0'))
print("End Program")
"""
############################ Endo of Order Placement Block #############
