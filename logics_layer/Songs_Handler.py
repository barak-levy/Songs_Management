from instrafucture_layer import RestSender
import json
import json
from config_reader import data



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



def get_songs_by_rank(rank,op):
    d={
        "rank" : rank,
        "op" : op
    }
    response = RestSender.send_get_message(data["PATH"] + data["Get song by rank"]+ "?"+ "rank=" +rank + "&op=" +op)
    data_response=response.json()
    return response, data_response["data"]

def check_ranks_of_songs(songs,rating,op):
    rating=int(rating)
    for song in songs:
        r,returned_song=get_song_from_db(song)
        returned_song= r.json()["data"]
        if op == "less":
            if returned_song["rating"] > rating:
                return False
        elif op =="greater":
            if returned_song["rating"] < rating:
                return False
        else:
            if returned_song["rating"] != rating:
                return False
    return True


