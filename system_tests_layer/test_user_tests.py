#import logics_layer.User_Handler,logics_layer.Responses_Handler
from logics_layer.User_Handler import *
from logics_layer.Responses_Handler import   *

def test_add_user(clearUsersDB):
    r,user_added=add_user("Barak","1010")
    assert response_ok(r),r.json()["error"]
    r,user_recived,message=get_user("Barak")
    #print(user_recived["data"]["user_name"])
    #print("Barak!!!!!!")
    assert user_added==user_recived.get("user_name"),message


def test_add_friend():
    r=add_friend("Barak","1010","Paz Davidov")
    assert response_ok(r),r.json()["error"]
    r,user_recived,message=get_user("Barak")
    assert "Paz Davidov" in  user_recived["friends"],message

def test_add_playlist():
    r,playlist_added=add_playlist("Barak","1010","BPlay")
    assert response_ok(r),r.json()["error"]
    #r,playlist_received=get_playlist("Barak","1010",playlist_added)
    r,user_recived,message=get_user("Barak")

    assert playlist_added in user_recived.get("playlists")

def test_add_same_name_playlist():
    r, playlist_added = add_playlist("Barak", "1010", "BPlay")
    assert  not response_ok(r), r.json()["error"]


def test_add_functions_without_pass():
    r = add_friend("Barak", "10", "Paz Davidov")
    assert not response_ok(r), r.json()["error"]
    r, playlist_added = add_playlist("Barak", "110", "BPlay")
    assert not response_ok(r), r.json()["error"]



def test_add_same_username():
    r, user_added = add_user("Barak", "1010")
    assert not response_ok(r), r.json()["error"]
