from parent import *
import pandas as pd

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

minute5data = OHLCHistory("SBIN-EQ", "3045", "FIVE_MINUTE", "2022-10-17 00:00", "2022-10-17 15:30")
print("5 minute data Live:")
my_df = pd.DataFrame(minute5data)
print(my_df)

# ONE_MINUTE	1 Minute
# THREE_MINUTE	3 Minute
# FIVE_MINUTE	5 Minute
# TEN_MINUTE	10 Minute
# FIFTEEN_MINUTE	15 Minute
# THIRTY_MINUTE	30 Minute
# ONE_HOUR	1 Hour
# ONE_DAY 1 Day

   
############################ End of OHLC Block #############
