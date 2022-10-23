from parent import *
import pandas as pd
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

print(place_order("SBIN-EQ", "3045",1,'NSE','BUY','MARKET','0'))
print("End Program")

############################ Endo of Order Placement Block #############
