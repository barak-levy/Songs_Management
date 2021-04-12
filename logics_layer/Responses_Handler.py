from instrafucture_layer import RestSender
import json
from config_reader import data




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
