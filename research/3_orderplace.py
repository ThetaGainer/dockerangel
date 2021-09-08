from smartapi.SmartConnect import SmartConnect
import pandas as pd
import requests
import login as l

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

print(place_order("SBIN-EQ", "3045",1,'NSE','BUY','MARKET,0'))
print("End Program")

############################ Endo of Order Placement Block #############
