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
    url = 
    d = requests.get(url).json()
    global token_df
    token_df = pd.DataFrame.from_dict(d)
    token_df['expiry'] = pd.to_datetime(token_df['expiry'])
    token_df = token_df.astype({'strike': float})
    l.token_map = token_df
    print(token_df)

############################ End of Symbol Mapping Block #############
