import json
import os

os.chdir("Data")
ls = os.listdir()
fp = open("../res.csv", "w")
for l in ls:
    with open(l, "r") as f:
        res = json.load(f)
        number = res["items"][0]['certificateNumber']
        signers = res["items"][0]['signer']["nickName"]
        signableItem = res["items"][0]["signableItem"]
        categoryName = res["items"][0]["signer"]["categoryName"]
        notes = res["items"][0]["notes"]
        print(notes)
        if notes is None:
            notes = ""
        if categoryName is None:
            categoryName = ''
        if signableItem is None:
            signableItem = ''
        if signers is None:
            signers = ''
        fp.write(",".join([number, signers, signableItem, categoryName, "CONTACT TO UPGRADE TO LOA\n", notes]))