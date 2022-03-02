# Honeygain-py

### usage

```py
from Honeygain import Honeygain

account = Honeygain()
account.login("client@email.com", "s3cr3tPass")
print(account.getBalance())
```

or 

```py
account = Honeygain("secretBearerToken")
print(account.getBalance())
```
