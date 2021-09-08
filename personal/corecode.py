# package import statement
from smartapi import SmartConnect #or from smartapi.smartConnect import SmartConnect
#import smartapi.smartExceptions(for smartExceptions)

# Creds
apikey = ''
username = ''
passwd = ''

#create object of call
obj=SmartConnect(api_key=apikey)
                #optional
                #access_token = "your access token",
                #refresh_token = "your refresh_token")

#login api call

data=obj.generateSession(username,passwd)
refreshToken=data['data']['refreshToken']

#fetch the feedtoken
feedToken=obj.getfeedToken()

#fetch User Profile
userProfile=obj.getProfile(refreshToken)

print(userProfile)
