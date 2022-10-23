from smartapi import SmartConnect #from smartapi.SmartConnect import SmartConnect
import login as l
import pyotp

############################ Session Block #############
#login api call
obj=SmartConnect(api_key=l.api_key)
data = obj.generateSession(l.user_name,l.password,pyotp.TOTP(l.code).now())
refreshToken= data['data']['refreshToken']

#fetch the feedtoken
feedToken=obj.getfeedToken()
#l.feed_token = feedToken
#fetch User Profile
userProfile=obj.getProfile(refreshToken)
#print(userProfile)

############################ End of Session Block #############
