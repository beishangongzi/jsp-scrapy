import json
import os
import re
import time

import requests


with open("numbers.txt", "r") as f:
    lines = f.readlines()
    # print(len(lines))


for line in lines:
    number = line.split("=")[-1].rstrip()
    if os.path.exists(f"Data/{number}.txt"):
        print(number, "skip")
        continue
    url = "https://webapi.spenceloa.com/api/v1/businessservices/certificates?searchTerm={}&partialMatches=false&page=1&pageSize=20&applicationId=52D95372-C5BC-4DE3-B073-4CE6FC42EE5B&organizationId=E2BEE467-6B7D-4D0E-9781-629001B93452".format(number)
    res = requests.get(url).json()
    with open(f"Data/{number}.txt", "w") as f:
        json.dump(res, f)
    print(number, "ok--------------")
    # time.sleep(0.5)

