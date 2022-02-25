import requests

"""
This Class is made to use the undocumented Honeygain API.
There are a few more things possible, like changing passwords or 
rename devices, which are not implemented nor planned.

Their API is ratelimited and they will ban your account and IP if
you go over their limit. The limit is unknown but the webinterface does
11 initial requests and then fetches /users/balances every minute.

For this reason, every function has a set of fake data you can call
without making a real request to build your app and test code.

The class also counts the requests made to the API. Its your 
responsibility to handle this with caution.
"""

class Honeygain():
    def __init__(self, bearer_token=None, version="v1", mockData=False):
        self.__url__ = "https://dashboard.honeygain.com/api/"
        self.__bearer_token__ = bearer_token
        self.__version__ = version
        self.__mockData__ = mockData
        self.__requestCount__ = 0

    def setBearerToken(self, bearer_token):
        self.__bearer_token__ = bearer_token

    def __checkBearerToken__(self):
        if self.__bearer_token__ == None:
            raise Exception("No Bearer Token set")

    def setMockData(self, mockData):
        self.__mockData__ = mockData
    
    def __request__(self, endpoint, versionOverride=None):
        print("Requesting: " + self.__url__ + self.__version__ + "/" + endpoint)
        self.__checkBearerToken__()

        ver = self.__version__
        if versionOverride != None:
            ver = versionOverride

        url = self.__url__ + ver +"/"+ endpoint
        auth = "Bearer " + self.__bearer_token__
        headers = {"Authorization": auth}

        try:
            r = requests.get(url, headers=headers).json()
        except requests.exceptions.RequestException as e:
            raise Exception(e)
        except ValueError as e:
            raise Exception(e)
        
        self.__requestCount__ += 1
        return r
        
    def getRequestCount(self):
        return self.__requestCount__

    def getBalance(self, versionOverride=None):
        if self.__mockData__ == False:
            return self.__request__(endpoint="users/balances", versionOverride=None)
        else:
            return {"meta":None,"data":{"realtime":{"credits":111.22,"usd_cents":11},"payout":{"credits":5000.00,"usd_cents":500},"min_payout":{"credits":20000.0,"usd_cents":2000}}}


    def getJumpTaskEarnings(self, versionOverride=None):
        if self.__mockData__ == False:
            return self.__request__(endpoint="earnings/jt", versionOverride=None)
        else:
            return {"meta":None,"data":{"total_credits":0.0,"bonus_credits":0.0,"total_usd_cents":0,"bonus_usd_cents":0}}


    def getUser(self, versionOverride=None):
        if self.__mockData__ == False:
            return self.__request__(endpoint="users/me", versionOverride=None)
        else:
            return {"data":{"id":"k49cb3p5-k3z4-1114-bvbf-86flyx7di9c","email":"totallylegit@mail.com","status":"registered","total_devices":7,"email_confirmed":True,"referral_code":"REFCODE0123","created_at":"2021-02-22T10:57:55+00:00","features":["jtEnabled"],"active_devices_count":2,"jt_toggle":None}}


    def getUserDevices(self, page=1 ,versionOverride=None):
        if self.__mockData__ == False:
            endp="devices?page=" + str(page)
            return self.__request__(endpoint=endp, versionOverride=versionOverride)
        else:
            return {'meta': {'pagination': {'total_items': 7, 'total_pages': 1, 'items_per_page': 10, 'current_page': 1}, 'ordering': {'ordered_by': 'created_at', 'order_direction': 'desc'}}, 'data': [{'id': 'ade95577dca3877dcfa0337ab87793c4becc9d30021d271825abd9275f270d7e', 'manufacturer': 'TOSHIBA', 'model': 'PSC0UE-00D001GR', 'title': None, 'platform': 'windows', 'version': '6.1.7601', 'streaming_enabled': True, 'stats': {'total_traffic': 40198, 'total_credits': 1.29, 'streaming_seconds': 0}}, {'id': 'f2c9fbe6fbc2305c149092b94a1e1a45', 'manufacturer': 'HUAWEI', 'model': 'JSN-L21', 'title': None, 'platform': 'android', 'version': '10', 'streaming_enabled': False, 'stats': {'total_traffic': 1117417, 'total_credits': 347.91, 'streaming_seconds': 0}}, {'id': 'ade95577dca3877dcfa0337ab87793c4becc9d30021d271825abd9275f270d7e', 'manufacturer': 'Docker', 'model': 'server', 'title': None, 'platform': 'linux', 'version': '0.6.6', 'streaming_enabled': False, 'stats': {'total_traffic': 0, 'total_credits': 0.0, 'streaming_seconds': 0}}, {'id': 'ade95577dca3877dcfa0337ab87793c4becc9d30021d271825abd9275f270d7e', 'manufacturer': 'Amazon', 'model': 'AFTMM', 'title': None, 'platform': 'android', 'version': '7.1.2', 'streaming_enabled': False, 'stats': {'total_traffic': 54743, 'total_credits': 0.58,'streaming_seconds': 0}}, {'id': 'ade95577dca3877dcfa0337ab87793c4becc9d30021d271825abd9275f270d7e', 'manufacturer': 'Docker', 'model': 'docker2', 'title': None, 'platform': 'linux', 'version': '0.6.6', 'streaming_enabled': False, 'stats': {'total_traffic': 0, 'total_credits': 0.0, 'streaming_seconds': 0}}, {'id': 'ade95577dca3877dcfa0337ab87793c4becc9d30021d271825abd9275f270d7e', 'manufacturer': 'Docker', 'model': 'linode_docker1', 'title': None, 'platform': 'linux', 'version': '0.6.6', 'streaming_enabled': False, 'stats': {'total_traffic': 0, 'total_credits': 0.0, 'streaming_seconds': 0}}, {'id': 'ade95577dca3877dcfa0337ab87793c4becc9d30021d271825abd9275f270d7e', 'manufacturer': 'Xiaomi', 'model': 'M2101K6G', 'title': None, 'platform': 'android', 'version': '12', 'streaming_enabled': False, 'stats': {'total_traffic': 15265012, 'total_credits': 473.77, 'streaming_seconds': 0}}]}


    def getTosInfo(self, versionOverride=None):
        if self.__mockData__ == False:
            return self.__request__(endpoint="users/tos", versionOverride=None)
        else:
            return {"meta":None,"data":{"version":"v200113","status":"accepted","first_terms_accepted_at":"2021-02-22"}}


    def getMonthlyGatherings(self, versionOverride=None):
        if self.__mockData__ == False:
            return self.__request__(endpoint="earnings/stats", versionOverride=None)
        else:
            return {"2022-01-27":{"gathering":{"credits":0.0,"traffic":0},"content_delivery":{"credits":0.0,"time":0},"referrals":{"credits":0.0},"winnings":{"credits":0.0},"other":{"credits":0.0},"bonus":{"credits":0.0}},"2022-01-28":{"gathering":{"credits":0.0,"traffic":0},"content_delivery":{"credits":0.0,"time":0},"referrals":{"credits":0.0},"winnings":{"credits":0.0},"other":{"credits":0.0},"bonus":{"credits":0.0}},"2022-01-29":{"gathering":{"credits":0.0,"traffic":0},"content_delivery":{"credits":0.0,"time":0},"referrals":{"credits":0.0},"winnings":{"credits":0.0},"other":{"credits":0.0},"bonus":{"credits":0.0}},"2022-01-30":{"gathering":{"credits":0.0,"traffic":0},"content_delivery":{"credits":0.0,"time":0},"referrals":{"credits":0.0},"winnings":{"credits":0.0},"other":{"credits":0.0},"bonus":{"credits":0.0}},"2022-01-31":{"gathering":{"credits":0.0,"traffic":0},"content_delivery":{"credits":0.0,"time":0},"referrals":{"credits":0.0},"winnings":{"credits":0.0},"other":{"credits":0.0},"bonus":{"credits":0.0}},"2022-02-01":{"gathering":{"credits":0.0,"traffic":0},"content_delivery":{"credits":0.0,"time":0},"referrals":{"credits":0.0},"winnings":{"credits":0.0},"other":{"credits":0.0},"bonus":{"credits":0.0}},"2022-02-02":{"gathering":{"credits":0.0,"traffic":0},"content_delivery":{"credits":0.0,"time":0},"referrals":{"credits":0.0},"winnings":{"credits":0.0},"other":{"credits":0.0},"bonus":{"credits":0.0}},"2022-02-03":{"gathering":{"credits":0.0,"traffic":0},"content_delivery":{"credits":0.0,"time":0},"referrals":{"credits":0.0},"winnings":{"credits":0.0},"other":{"credits":0.0},"bonus":{"credits":0.0}},"2022-02-04":{"gathering":{"credits":0.0,"traffic":0},"content_delivery":{"credits":0.0,"time":0},"referrals":{"credits":0.0},"winnings":{"credits":0.0},"other":{"credits":0.0},"bonus":{"credits":0.0}},"2022-02-05":{"gathering":{"credits":0.0,"traffic":0},"content_delivery":{"credits":0.0,"time":0},"referrals":{"credits":0.0},"winnings":{"credits":0.0},"other":{"credits":0.0},"bonus":{"credits":0.0}},"2022-02-06":{"gathering":{"credits":0.0,"traffic":0},"content_delivery":{"credits":0.0,"time":0},"referrals":{"credits":0.0},"winnings":{"credits":0.0},"other":{"credits":0.0},"bonus":{"credits":0.0}},"2022-02-07":{"gathering":{"credits":0.0,"traffic":0},"content_delivery":{"credits":0.0,"time":0},"referrals":{"credits":0.0},"winnings":{"credits":0.0},"other":{"credits":0.0},"bonus":{"credits":0.0}},"2022-02-08":{"gathering":{"credits":0.0,"traffic":0},"content_delivery":{"credits":0.0,"time":0},"referrals":{"credits":0.0},"winnings":{"credits":0.0},"other":{"credits":0.0},"bonus":{"credits":0.0}},"2022-02-09":{"gathering":{"credits":0.0,"traffic":0},"content_delivery":{"credits":0.0,"time":0},"referrals":{"credits":0.0},"winnings":{"credits":0.0},"other":{"credits":0.0},"bonus":{"credits":0.0}},"2022-02-10":{"gathering":{"credits":0.0,"traffic":0},"content_delivery":{"credits":0.0,"time":0},"referrals":{"credits":0.0},"winnings":{"credits":0.0},"other":{"credits":0.0},"bonus":{"credits":0.0}},"2022-02-11":{"gathering":{"credits":0.0,"traffic":0},"content_delivery":{"credits":0.0,"time":0},"referrals":{"credits":0.0},"winnings":{"credits":0.0},"other":{"credits":0.0},"bonus":{"credits":0.0}},"2022-02-12":{"gathering":{"credits":0.0,"traffic":0},"content_delivery":{"credits":0.0,"time":0},"referrals":{"credits":0.0},"winnings":{"credits":0.0},"other":{"credits":0.0},"bonus":{"credits":0.0}},"2022-02-13":{"gathering":{"credits":0.0,"traffic":0},"content_delivery":{"credits":0.0,"time":0},"referrals":{"credits":0.0},"winnings":{"credits":0.0},"other":{"credits":0.0},"bonus":{"credits":0.0}},"2022-02-14":{"gathering":{"credits":0.0,"traffic":0},"content_delivery":{"credits":0.0,"time":0},"referrals":{"credits":0.0},"winnings":{"credits":0.0},"other":{"credits":0.0},"bonus":{"credits":0.0}},"2022-02-15":{"gathering":{"credits":0.0,"traffic":0},"content_delivery":{"credits":0.0,"time":0},"referrals":{"credits":0.0},"winnings":{"credits":0.0},"other":{"credits":0.0},"bonus":{"credits":0.0}},"2022-02-16":{"gathering":{"credits":0.0,"traffic":0},"content_delivery":{"credits":0.0,"time":0},"referrals":{"credits":0.0},"winnings":{"credits":0.0},"other":{"credits":0.0},"bonus":{"credits":0.0}},"2022-02-17":{"gathering":{"credits":0.0,"traffic":0},"content_delivery":{"credits":0.0,"time":0},"referrals":{"credits":0.0},"winnings":{"credits":0.0},"other":{"credits":0.0},"bonus":{"credits":0.0}},"2022-02-18":{"gathering":{"credits":0.0,"traffic":0},"content_delivery":{"credits":0.0,"time":0},"referrals":{"credits":0.0},"winnings":{"credits":0.0},"other":{"credits":0.0},"bonus":{"credits":0.0}},"2022-02-19":{"gathering":{"credits":0.0,"traffic":0},"content_delivery":{"credits":0.0,"time":0},"referrals":{"credits":0.0},"winnings":{"credits":0.0},"other":{"credits":0.0},"bonus":{"credits":0.0}},"2022-02-20":{"gathering":{"credits":0.0,"traffic":0},"content_delivery":{"credits":0.0,"time":0},"referrals":{"credits":0.0},"winnings":{"credits":0.0},"other":{"credits":0.0},"bonus":{"credits":0.0}},"2022-02-21":{"gathering":{"credits":0.0,"traffic":0},"content_delivery":{"credits":0.0,"time":0},"referrals":{"credits":0.0},"winnings":{"credits":0.0},"other":{"credits":0.0},"bonus":{"credits":0.0}},"2022-02-22":{"gathering":{"credits":0.0,"traffic":368318040},"content_delivery":{"credits":0.0,"time":0},"referrals":{"credits":0.0},"winnings":{"credits":0.0},"other":{"credits":0.0},"bonus":{"credits":0.0}},"2022-02-23":{"gathering":{"credits":0.0,"traffic":839307679},"content_delivery":{"credits":0.0,"time":0},"referrals":{"credits":0.0},"winnings":{"credits":0.0},"other":{"credits":0.0},"bonus":{"credits":0.0}},"2022-02-24":{"gathering":{"credits":0.0,"traffic":749178004},"content_delivery":{"credits":0.0,"time":0},"referrals":{"credits":0.0},"winnings":{"credits":0.0},"other":{"credits":0.0},"bonus":{"credits":0.0}},"2022-02-25":{"gathering":{"credits":0.0,"traffic":767895590},"content_delivery":{"credits":0.0,"time":0},"referrals":{"credits":0.0},"winnings":{"credits":0.0},"other":{"credits":0.0},"bonus":{"credits":0.0}}}


    def getReferrals(self, page=1, versionOverride=None):
        if self.__mockData__ == False:
            endp = "referrals?page=" + str(page)
            return self.__request__(endpoint=endp, versionOverride=versionOverride)
        else:
            return {'meta': {'pagination': {'total_items': 3, 'total_pages': 1, 'items_per_page': 10, 'current_page': 1}, 'ordering': {'ordered_by': 'created_at', 'order_direction': 'desc'}}, 'data': [{'email': 'u*************@g*****.com', 'registered_at': '2022-02-22 16:23:22'}, {'email': 'f**********@g*****.com', 'registered_at': '2022-02-23 19:07:00'}, {'email': 'm**************@g*****.com', 'registered_at': '2022-02-25 05:21:15'}]}


    def getReferralEarnings(self, versionOverride=None):
        if self.__mockData__ == False:
            return self.__request__(endpoint="referrals/earnings", versionOverride=None)
        else:
            return {"count":3,"total_earnings":208.31,"average_earnings":69.44,"first_referrals":["U","F","M"]}


    def getTodaysEarnings(self, versionOverride=None):
        if self.__mockData__ == False:
            return self.__request__(endpoint="earnings/today", versionOverride=None)
        else:
            return {"total":{"credits":333.49},"winning":{"credits":10.0},"referral":{"credits":93.66},"other":{"credits":0.0},"cdn":{"credits":0.0,"seconds":0},"gathering":{"credits":229.83,"bytes":767895590},"total_credits":333.49,"gathering_bytes":767895590,"streaming_seconds":0,"winning_credits":10.0,"referral_credits":93.66,"other_credits":0.0}


    def getRegisteredDevices(self, versionOverride="v2"):
        if self.__mockData__ == False:
            return self.__request__(endpoint="devices", versionOverride=versionOverride)
        else:
            return {"meta":{"pagination":{"total_items":7,"total_pages":None,"items_per_page":None,"current_page":None},"ordering":None},"data":[{"id":"gggff1h2h2h2h2h2h2h2h2h2h2h2h2h2","manufacturer":"Xiaomi","model":"D3346V1A","title":None,"platform":"android","version":"12","streaming_enabled":False,"stats":{"total_traffic":1562113892,"total_credits":468.63,"streaming_seconds":0},"ip":"192.168.2.1","status":"active","last_active_time":"2022-02-25 22:30:39"},{"id":"ffffffffffffffffffffffffffffff12","manufacturer":"TOSHIBA","model":"AAAAA-BBBBB","title":None,"platform":"windows","version":"6.1.7601","streaming_enabled":True,"stats":{"total_traffic":913261,"total_credits":0.27,"streaming_seconds":0},"ip":"192.168.2.2","status":"active","last_active_time":"2022-02-25 22:28:19"},{"id":"111111111122222222223333333333oi","manufacturer":"HUAWEI","model":"CCC-X22","title":None,"platform":"android","version":"10","streaming_enabled":False,"stats":{"total_traffic":1159717417,"total_credits":347.91,"streaming_seconds":0},"ip":"192.168.2.3","status":"inactive","last_active_time":"2022-02-25 22:00:40"},{"id":"qwertzuioplkjhgfdsayxcvbnm123456","manufacturer":"Amazon","model":"AFTMM","title":None,"platform":"android","version":"7.1.2","streaming_enabled":False,"stats":{"total_traffic":1954743,"total_credits":0.58,"streaming_seconds":0},"ip":"192.168.2.4","status":"inactive","last_active_time":"2022-02-24 19:46:28"},{"id":"ddddddddddddddddddddddddddddddddddddd","manufacturer":"Docker","model":"docker1","title":None,"platform":"linux","version":"0.6.6","streaming_enabled":False,"stats":{"total_traffic":0,"total_credits":0,"streaming_seconds":0},"ip":None,"status":"inactive","last_active_time":None},{"id":"ggggggggggggggggggggggggggggggggggggggg","manufacturer":"Docker","model":"server","title":None,"platform":"linux","version":"0.6.6","streaming_enabled":False,"stats":{"total_traffic":0,"total_credits":0,"streaming_seconds":0},"ip":None,"status":"inactive","last_active_time":None},{"id":"bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb","manufacturer":"Docker","model":"docker2","title":None,"platform":"linux","version":"0.6.6","streaming_enabled":False,"stats":{"total_traffic":0,"total_credits":0,"streaming_seconds":0},"ip":None,"status":"inactive","last_active_time":None}]}


    def getMonthlyWalletStats(self, versionOverride=None):
        if self.__mockData__ == False:
            return self.__request__(endpoint="earnings/wallet-stats", versionOverride=None)
        else:
            return {"meta":{"pagination":None,"ordering":None},"data":{"2022-01-27":{"hg_credits":0.0,"jt_credits":0.0},"2022-01-28":{"hg_credits":0.0,"jt_credits":0.0},"2022-01-29":{"hg_credits":0.0,"jt_credits":0.0},"2022-01-30":{"hg_credits":0.0,"jt_credits":0.0},"2022-01-31":{"hg_credits":0.0,"jt_credits":0.0},"2022-02-01":{"hg_credits":0.0,"jt_credits":0.0},"2022-02-02":{"hg_credits":0.0,"jt_credits":0.0},"2022-02-03":{"hg_credits":0.0,"jt_credits":0.0},"2022-02-04":{"hg_credits":0.0,"jt_credits":0.0},"2022-02-05":{"hg_credits":0.0,"jt_credits":0.0},"2022-02-06":{"hg_credits":0.0,"jt_credits":0.0},"2022-02-07":{"hg_credits":0.0,"jt_credits":0.0},"2022-02-08":{"hg_credits":0.0,"jt_credits":0.0},"2022-02-09":{"hg_credits":0.0,"jt_credits":0.0},"2022-02-10":{"hg_credits":0.0,"jt_credits":0.0},"2022-02-11":{"hg_credits":0.0,"jt_credits":0.0},"2022-02-12":{"hg_credits":0.0,"jt_credits":0.0},"2022-02-13":{"hg_credits":0.0,"jt_credits":0.0},"2022-02-14":{"hg_credits":0.0,"jt_credits":0.0},"2022-02-15":{"hg_credits":0.0,"jt_credits":0.0},"2022-02-16":{"hg_credits":0.0,"jt_credits":0.0},"2022-02-17":{"hg_credits":0.0,"jt_credits":0.0},"2022-02-18":{"hg_credits":0.0,"jt_credits":0.0},"2022-02-19":{"hg_credits":0.0,"jt_credits":0.0},"2022-02-20":{"hg_credits":0.0,"jt_credits":0.0},"2022-02-21":{"hg_credits":0.0,"jt_credits":0.0},"2022-02-22":{"hg_credits":5117.630005,"jt_credits":0.0},"2022-02-23":{"hg_credits":388.735924,"jt_credits":0.0},"2022-02-24":{"hg_credits":395.32499,"jt_credits":0.0},"2022-02-25":{"hg_credits":333.493495,"jt_credits":0.0}}}


    def getMonthlyTrafficStats(self, versionOverride=None):
        if self.__mockData__ == False:
            return self.__request__(endpoint="dashboards/traffic_stats", versionOverride=None)
        else:
            return {'meta': None, 'data': {'total_traffic': 2737589759, 'total_streaming_seconds': 0, 'traffic_stats': [{'date': '2022-01-27','traffic': 0, 'streaming_seconds': 0}, {'date': '2022-01-28', 'traffic': 0, 'streaming_seconds': 0}, {'date': '2022-01-29','traffic': 0, 'streaming_seconds': 0}, {'date': '2022-01-30', 'traffic': 0, 'streaming_seconds': 0}, {'date': '2022-01-31','traffic': 0, 'streaming_seconds': 0}, {'date': '2022-02-01', 'traffic': 0, 'streaming_seconds': 0}, {'date': '2022-02-02','traffic': 0, 'streaming_seconds': 0}, {'date': '2022-02-03', 'traffic': 0, 'streaming_seconds': 0}, {'date': '2022-02-04','traffic': 0, 'streaming_seconds': 0}, {'date': '2022-02-05', 'traffic': 0, 'streaming_seconds': 0}, {'date': '2022-02-06','traffic': 0, 'streaming_seconds': 0}, {'date': '2022-02-07', 'traffic': 0, 'streaming_seconds': 0}, {'date': '2022-02-08','traffic': 0, 'streaming_seconds': 0}, {'date': '2022-02-09', 'traffic': 0, 'streaming_seconds': 0}, {'date': '2022-02-10','traffic': 0, 'streaming_seconds': 0}, {'date': '2022-02-11', 'traffic': 0, 'streaming_seconds': 0}, {'date': '2022-02-12','traffic': 0, 'streaming_seconds': 0}, {'date': '2022-02-13', 'traffic': 0, 'streaming_seconds': 0}, {'date': '2022-02-14','traffic': 0, 'streaming_seconds': 0}, {'date': '2022-02-15', 'traffic': 0, 'streaming_seconds': 0}, {'date': '2022-02-16','traffic': 0, 'streaming_seconds': 0}, {'date': '2022-02-17', 'traffic': 0, 'streaming_seconds': 0}, {'date': '2022-02-18','traffic': 0, 'streaming_seconds': 0}, {'date': '2022-02-19', 'traffic': 0, 'streaming_seconds': 0}, {'date': '2022-02-20','traffic': 0, 'streaming_seconds': 0}, {'date': '2022-02-21', 'traffic': 0, 'streaming_seconds': 0}, {'date': '2022-02-22','traffic': 368318040, 'streaming_seconds': 0}, {'date': '2022-02-23', 'traffic': 839307679, 'streaming_seconds': 0}, {'date': '2022-02-24', 'traffic': 749178004, 'streaming_seconds': 0}, {'date': '2022-02-25', 'traffic': 780786036, 'streaming_seconds': 0}]}}

    
