from instrafucture_layer import RestSender
import json


with open(r"C:\Users\barakl1\Songs_Management/config.json", "r") as jsonfile:
    data = json.load(jsonfile)
    print("Read successful")


def add_user(user_name, user_password):
    user =  {
        "user_name":user_name,
        "user_password":user_password
        }
    print(user)
    response  = RestSender.send_post_message(data["PATH"]+ data["add user"], user)
    userName_return = user["user_name"]

    return response, userName_return

def get_user(user_name):
    response =RestSender.send_get_message(data["PATH"]+ data["get user"]+ "?"+ "user_name=" +user_name)
    data_response =response.json()
    message=""
    if "error" in data_response:
        message=data_response["error"]
        return response,None,message
    return response,data_response["data"],message


def add_friend(user_name,user_password, friend_name):
    user = {
        "friend_name": friend_name,
        "user_name" : user_name,
        "user_password" : user_password

    }
    response = RestSender.send_put_message(data["PATH"]+data["add_friend"],user)
    #getter =
    #user_friends_list = response.json()
   #print(user_friends_list["friends"])
    return response

def add_playlist(user_name,user_password,playlist_name):
    d = {
        "user_name": user_name,
        "user_password": user_password,
        "playlist_name": playlist_name
    }

    print(d)
    response = RestSender.send_post_message(data["PATH"] + data["add playlist"], d)
    playListName_return = d["playlist_name"]

    return response, playListName_return




