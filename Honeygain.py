import requests

"""
This Class is made to use the undocumented Honeygain API.
There are a few more things possible, like changing passwords or 
rename devices, which are not implemented nor planned.

Their API is ratelimited and they will ban your account and IP if
you go over their limit. The limit is unknown but the webinterface does
11 initial requests and then fetches /users/balances every minute.

"""

class Honeygain():
    def __init__(self, token=None, debug=False):
        self.basueUrl = 'https://dashboard.honeygain.com/api'
        self.token = token
        self.debug = debug
    
    def login(self, email=None, password=None):
        if email is None or password is None:
            raise Exception("Email and password are required")
        try:
            self.token = requests.post("https://dashboard.honeygain.com/api/v1/users/tokens", json={'email': email,'password': password}).json()['data']["access_token"]
        except Exception as e:
            raise Exception(e)
        
    def __checkBearerToken(self):
        if self.token == None:
            raise Exception("No Bearer Token set. Call login() or set bearer token in constructor")

    def __request(self, endpoint):
        url = self.basueUrl + endpoint
        if self.debug:
            print("Requesting: " + url)
        self.__checkBearerToken()
        auth = "Bearer " + self.token
        headers = {"Authorization": auth}
        try:
            r = requests.get(url, headers=headers).json()
        except Exception as e:
            raise Exception(e)
        return r

    def getBalance(self):
        return self.__request("/v1/users/balances")

    def getJumpTaskEarnings(self):
        return self.__request("/v1/earnings/jt")

    def getUser(self):
        return self.__request("/v1/users/me")

    def getUserDevices(self, page=1):
        return self.__request("/v1/devices?page=" + str(page))

    def getTosInfo(self):
        return self.__request("/v1/users/tos")

    def getMonthlyGatherings(self):
        return self.__request("/v1/earnings/stats")

    def getReferrals(self, page=1):
        return self.__request("/v1/referrals?page=" + str(page))

    def getReferralEarnings(self):
        return self.__request("/v1/referrals/earnings")

    def getTodaysEarnings(self):
        return self.__request("/v1/earnings/today")

    def getRegisteredDevices(self):
        return self.__request("/v2/devices")

    def getMonthlyWalletStats(self):
        return self.__request("/v1/earnings/wallet-stats")

    def getMonthlyTrafficStats(self):
         return self.__request("/v1/dashboards/traffic_stats")


