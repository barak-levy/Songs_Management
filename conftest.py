from instrafucture_layer import RestSender
import json
import pytest
from logics_layer.User_Handler import *
from logics_layer.Responses_Handler import   *
from logics_layer.Playlist_Handler import   *
from logics_layer.Songs_Handler import *


with open(r"C:\Users\barakl1\Songs_Management/config.json", "r") as jsonfile:
    data = json.load(jsonfile)

@pytest.fixture()
def clearUsersDB():
    response = RestSender.send_delete_message(data["PATH"] + data["delete_all_users"])
    print("ALL USERS DELETED FROM DB")

@pytest.fixture()
def clearSongsDB():
    response = RestSender.send_delete_message(data["PATH"]+data["Delete all songs"])
    print("ALL SONGS DELETED FROM DB")


@pytest.fixture()
def add_users_and_songs():
    user_name = "Barak"
    user_password = "1010"
    Playlist_name = "BPlay"
    song_title = "Millionaires19"
    song_genre = "Mid"
    song_year = "2021"
    song_performer = "Omer Adam"

    add_user(user_name, user_password)
    add_user("Paz Davidov", "1010")
    r, song_added = add_song_to_DB(song_genre, song_year, song_performer, song_title)
