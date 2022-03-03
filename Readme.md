# Honeygain-py

### why?
Its an easy way to check your data without the need of a webbrowser on many devices. A simple class like this is easy to understand and maintain.
Almost all API wrapper that make use of Honeygains API are absolute crap or incomplete and if they are not broken yet, will be in the future.


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
