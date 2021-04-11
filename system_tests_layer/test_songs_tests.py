from logics_layer.User_Handler import *
from logics_layer.Responses_Handler import   *
from logics_layer.Playlist_Handler import   *
from logics_layer.Songs_Handler import   *

def test_add_song_to_DB():
    song_genre="Mid"
    song_year="2021"
    song_performer="Omer Adam"
    song_title="Millioners16"

    r, song_added = add_song_to_DB(song_genre, song_year, song_performer, song_title)
    assert response_ok(r), r.json()["error"]
    r, song_recieved = get_song_from_db("Millioners16")
    assert response_ok(r), r.json()["error"]
    #assert song_added in user_recived.get("playlist"), "Song not been added"


def test_song_upvote():
    user_name = "Barak"
    user_password = "1010"
    playlist_name ="BPlay"
    song_title = "Millioners15"
    """
    add function that get the last vote rank and check if the rank upvoted by 1 after
    """
    playlist = get_playlist(user_name, user_password, playlist_name)
    first_rating = get_song_rank(song_title, playlist)
    r = song_upvote(user_name,user_password,playlist_name,song_title)
    assert response_ok(r),r.json()["error"]
    assert get_song_rank(song_title, playlist) - 1 == first_rating

def test_song_downvote():

    user_name = "Barak"
    user_password = "1010"
    playlist_name = "BPlay"
    song_title = "Millioners16"
    """
    add function that get the last vote rank and check if the rank downvoted by 1 after
    """
    playlist=get_playlist(user_name,user_password,playlist_name)
    first_rating= get_song_rank(song_title,playlist)
    r = song_downvote(user_name, user_password, playlist_name, song_title)
    assert response_ok(r), r.json()["error"]
    assert get_song_rank(song_title,playlist)+1 == first_rating


#write test of vote twice