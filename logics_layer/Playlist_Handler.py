from instrafucture_layer import RestSender
import json


with open(r"C:\Users\barakl1\Songs_Management/config.json", "r") as jsonfile:
    data = json.load(jsonfile)
    print("Read successful")


def add_song_to_PL(user_name ,user_password, Playlist_name, song_title):
    d={
        "user_name":user_name,
        "user_password" :user_password,
        "playlist_name" : Playlist_name,
        "song_title" : song_title
    }
    print(d)
    response = RestSender.send_post_message(data["PATH"] + data["Add song to playlist"], d)
    song_return = d["song_title"]

    return response, song_return