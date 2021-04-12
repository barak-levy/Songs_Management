# import logics_layer.User_Handler,logics_layer.Responses_Handler
from logics_layer.User_Handler import *
from logics_layer.Responses_Handler import *


def test_add_user(clearUsersDB):
    r, user_added = add_user("Barak", "1010")
    assert response_ok(r), r.json()["error"]
    r, user_recived, message = get_user("Barak")
    # print(user_recived["data"]["user_name"])
    # print("Barak!!!!!!")
    assert user_added == user_recived.get("user_name"), message


def test_add_friend(clearUsersDB):
    r, user_added = add_user("Barak", "1010")
    r = add_friend("Barak", "1010", "Paz Davidov")
    assert response_ok(r), r.json()["error"]
    r, user_recived, message = get_user("Barak")
    assert "Paz Davidov" in user_recived["friends"], message


def test_add_playlist(clearUsersDB):
    r, user_added = add_user("Barak", "1010")
    r, playlist_added = add_playlist("Barak", "1010", "BPlay")
    assert response_ok(r), r.json()["error"]
    # r,playlist_received=get_playlist("Barak","1010",playlist_added)
    r, user_received, message = get_user("Barak")

    assert playlist_added in user_received.get("playlists")


def test_add_same_name_playlist(clearUsersDB):
    r, user_added = add_user("Barak", "1010")
    r, playlist_added = add_playlist("Barak", "1010", "BPlay")
    r, playlist_added = add_playlist("Barak", "1010", "BPlay")
    assert not response_ok(r), r.json()["error"]


def test_add_functions_without_pass(clearUsersDB):
    r, user_added = add_user("Barak", "1010")
    r = add_friend("Barak", "10", "Paz Davidov")
    assert not response_ok(r), r.json()["error"]
    r, playlist_added = add_playlist("Barak", "110", "BPlay")
    assert not response_ok(r), r.json()["error"]


def test_add_same_username(clearUsersDB):
    r, user_added = add_user("Barak", "1010")
    r, user_added = add_user("Barak", "1010")
    assert not response_ok(r), r.json()["error"]


def test_same_playlist_two_users(clearUsersDB):
    r, user_added = add_user("Barak", "1010")
    add_user("Paz Davidov", "1010")

    r, playlist_added = add_playlist("Paz Davidov", "1010", "playlist")
    assert response_ok(r), r.json()["error"]
    r, user_recived, message = get_user("Paz Davidov")
    assert playlist_added in user_recived.get("playlists")
    r, playlist_added = add_playlist("Barak", "1010", "playlist")
    assert response_ok(r), r.json()["error"]
    r, user_recived, message = get_user("Barak")
    assert playlist_added in user_recived.get("playlists")

def test_get_user(clearUsersDB,clearSongsDB):
    user_name="Barak"
    user_password="1010"
    r, user_added = add_user(user_name, user_password)
    assert response_ok(r), r.json()["error"]
    r, user_recived, message = get_user(user_name)
    assert response_ok(r),r.json()["error"]
    assert user_recived["user_name"]==user_name,"user name not equal to the user name added"
    assert "user_password" not in user_recived,"The password returned in user data"

def test_change_password(clearUsersDB,clearSongsDB):
    user_name = "Barak"
    user_password = "1010"
    r, user_added = add_user(user_name, user_password)
    new_pass="10101993"
    r = change_user_password(user_name,user_password,new_pass)
    assert response_ok(r),r.json()["error"]
    # I dont have a way to check the new password because i cant get it (with get)