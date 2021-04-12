
from logics_layer.User_Handler import *
from logics_layer.Responses_Handler import   *
from logics_layer.Playlist_Handler import   *
from logics_layer.Songs_Handler import *

"""
def test_add_song():
    song_genre="Pop", song_year="2021", song_performer="Static & Ben-El", song_title="Kaktus"
    r,song_added=add_song(song_genre ,song_year, song_performer, song_title)
    assert response_ok(r), r.json()["error"]
    r, song_recived= get_song(song_added)
    assert response_ok(r), r.json()["error"]
    assert song_added == song_recived.get("user_name"), "Song not been added"

"""





def test_add_song_to_PL(clearUsersDB,clearSongsDB):

    user_name="Barak"
    user_password="1010"
    Playlist_name="BPlay"
    song_title="Millionaires19"
    song_genre = "Mid"
    song_year = "2021"
    song_performer = "Omer Adam"

    r, song_added = add_song_to_DB(song_genre, song_year, song_performer, song_title)
    r, user_added = add_user(user_name, user_password)
    r, playlist_added = add_playlist(user_name, user_password, Playlist_name)
    r,song_added=add_song_to_PL(user_name ,user_password, Playlist_name, song_title)
    assert response_ok(r), r.json()["error"]
    r, user_recived, message = get_user(user_name)
    assert response_ok(r), r.json()["error"]
    playlistToCheck=get_playlist(user_name,user_password,Playlist_name)
    assert check_playlist(playlistToCheck, song_title), "Song not been added"



