from instrafucture_layer import RestSender
import json


with open(r"C:\Users\barakl1\Songs_Management/config.json", "r") as jsonfile:
    data = json.load(jsonfile)
    print("Read successful")



def add_song_to_DB(song_genre, song_year, song_performer, song_title):
    d = {
        "song_genre": song_genre,
        "song_year": song_year,
        "song_performer": song_performer,
        "song_title": song_title
    }
    print(d)
    response = RestSender.send_post_message(data["PATH"] + data["add song to DB"], d)
    song_return = d["song_title"]
    return response, song_return


def get_song_from_db(song_title):

    response = RestSender.send_get_message(data["PATH"] + data["get song from DB"]+ "?"+ "song_title=" +song_title)
    song_return =song_title
    return response,song_return


def song_upvote(user_name,user_password ,playlist_name,song_title):
    d={
        "user_name": user_name,
        "user_password" : user_password,
        "playlist_name" : playlist_name,
        "song_title" : song_title

    }
    response= RestSender.send_put_message(data["PATH"]+data["song upvote"],d)
    return response

def song_downvote(user_name,user_password ,playlist_name,song_title):
    d={
        "user_name": user_name,
        "user_password" : user_password,
        "playlist_name" : playlist_name,
        "song_title" : song_title

    }
    response= RestSender.send_put_message(data["PATH"]+data["song downvote"],d)
    return response



