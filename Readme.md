# Honeygain-py

### bearer token

Open the Honeygain dashboard, right click and inspect, find the network tab, 
find a Honeygain API url (eg https://dashboard.honeygain.com/api/v1/users/me) and search for something along the lines of "Authorization Bearer __eyJ0eXAiOiJKV1QiLCJh__ ...."

### usage

```py
from Honeygain import Honeygain

bearer = "mysecretbearertoken"
account = Honeygain(bearer_token=bearer) # mockData=True for fake data
print(account.getBalance())

```
