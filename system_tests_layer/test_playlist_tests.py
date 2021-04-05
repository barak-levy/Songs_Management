
from logics_layer.User_Handler import *
from logics_layer.Responses_Handler import   *
from logics_layer.Playlist_Handler import   *

"""
def test_add_song():
    song_genre="Pop", song_year="2021", song_performer="Static & Ben-El", song_title="Kaktus"
    r,song_added=add_song(song_genre ,song_year, song_performer, song_title)
    assert response_ok(r), r.json()["error"]
    r, song_recived= get_song(song_added)
    assert response_ok(r), r.json()["error"]
    assert song_added == song_recived.get("user_name"), "Song not been added"

"""





def test_add_song_to_PL():
    user_name="Barak"
    user_password="1010"
    Playlist_name="BPlay"
    song_title="Kaktus"
    r,song_added=add_song_to_PL(user_name ,user_password, Playlist_name, song_title)
    assert response_ok(r), r.json()["error"]
    r, user_recived, message = get_user("Barak")
    assert response_ok(r), r.json()["error"]
    assert song_added in user_recived.get("playlists")[Playlist_name], "Song not been added"
