from logics_layer.User_Handler import *
from logics_layer.Responses_Handler import   *
from logics_layer.Playlist_Handler import   *
from logics_layer.Songs_Handler import   *

def test_add_song_to_DB():
    song_genre="Mid"
    song_year="2021"
    song_performer="Omer Adam"
    song_title="Millioners15"

    r, song_added = add_song_to_DB(song_genre, song_year, song_performer, song_title)
    assert response_ok(r), r.json()["error"]
    r, song_recieved = get_song_from_db("Millioners15")
    assert response_ok(r), r.json()["error"]
    #assert song_added in user_recived.get("playlist"), "Song not been added"



