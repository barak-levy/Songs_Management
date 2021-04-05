from instrafucture_layer import RestSender
import json
with open(r"C:\Users\barakl1\Songs_Management/config.json", "r") as jsonfile:
    data = json.load(jsonfile)




def response_ok(r):
    data=r.json()
    print(data)
    if "error" in data:
        return False
    if "messgae" in data:
        if data["messgae"]=="OK":
            return True
    else:
        if data["message"]=="OK":
            return True
    return False
