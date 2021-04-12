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


#THERE IS NOT DELETE SONG FROM PL IN THE ICD

def get_playlist(user_name,user_password ,playlist_name):
    d={
        "user_name" : user_name,
        "user_password" : user_password,
        "playlist_name" : playlist_name,

    }
    #?user_name=Barak&user_password=1010&playlist_name=BPlay
    response = RestSender.send_get_message(data["PATH"] + data["get playlist"] + "?" + "user_name=" + user_name+"&" +"user_password="+user_password+"&"+"playlist_name="+playlist_name)
    playlist= response.json()["data"]
    return playlist


def check_playlist(playlist, title):
    otherPerformer=""
    for song in playlist:
        #print(song['performer'])
        #print(song['title'])
        if song['title'] == title:
            return True
    return False




def get_song_rank(song_name,playlist):
    for song in playlist:
        if song["title"]==song_name:
            return song["rating"]


#playlist=get_playlist("Barak","1010","BPlay")
#print(get_song_rank("Millioners16",playlist))