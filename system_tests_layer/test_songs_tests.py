from logics_layer.User_Handler import *
from logics_layer.Responses_Handler import *
from logics_layer.Playlist_Handler import *
from logics_layer.Songs_Handler import *


def test_add_song_to_DB(clearUsersDB, clearSongsDB):
    song_genre = "Mid"
    song_year = "2021"
    song_performer = "Omer Adam"
    song_title = "Millionaires19"

    r, song_added = add_song_to_DB(song_genre, song_year, song_performer, song_title)
    assert response_ok(r), r.json()["error"]
    r, song_recieved = get_song_from_db(song_title)
    assert response_ok(r), r.json()["error"]
    song_rank=r.json()["data"]["rating"]
    assert song_rank==0,"song rate is not 0"


def test_song_upvote(clearUsersDB, clearSongsDB):
    song_genre = "Mid"
    song_year = "2021"
    song_performer = "Omer Adam"
    user_name = "Barak"
    user_password = "1010"
    playlist_name = "BPlay"
    song_title = "Millionaires19"

    # set conditions
    r, user_added = add_user(user_name, user_password)
    r, song_added = add_song_to_DB(song_genre, song_year, song_performer, song_title)
    r, playlist_added = add_playlist(user_name, user_password, playlist_name)
    r, song_added = add_song_to_PL(user_name, user_password, playlist_name, song_title)

    playlist = get_playlist(user_name, user_password, playlist_name)
    first_rating = get_song_rank(song_title, playlist)
    r = song_upvote(user_name, user_password, playlist_name, song_title)
    assert response_ok(r), r.json()["error"]
    playlist = get_playlist(user_name, user_password, playlist_name)
    assert get_song_rank(song_title, playlist) - 1 == first_rating


def test_song_downvote(clearUsersDB, clearSongsDB):
    song_genre = "Mid"
    song_year = "2021"
    song_performer = "Omer Adam"
    user_name = "Barak"
    user_password = "1010"
    playlist_name = "BPlay"
    song_title = "Millionaires19"

    # set conditions
    r, user_added = add_user(user_name, user_password)
    r, song_added = add_song_to_DB(song_genre, song_year, song_performer, song_title)
    r, playlist_added = add_playlist(user_name, user_password, playlist_name)
    r, song_added = add_song_to_PL(user_name, user_password, playlist_name, song_title)

    r = song_upvote(user_name, user_password, playlist_name, song_title)
    playlist = get_playlist(user_name, user_password, playlist_name)
    first_rating = get_song_rank(song_title, playlist)
    r = song_downvote(user_name, user_password, playlist_name, song_title)
    assert response_ok(r), r.json()["error"]
    playlist = get_playlist(user_name, user_password, playlist_name)
    assert get_song_rank(song_title, playlist) + 1 == first_rating


# There is a bug in the system. the system let the user vote twice.
def test_vote_twice(clearUsersDB, clearSongsDB):
    song_genre = "Mid"
    song_year = "2021"
    song_performer = "Omer Adam"
    user_name = "Barak"
    user_password = "1010"
    playlist_name = "BPlay"
    song_title = "Millionaires19"

    # set conditions
    r, user_added = add_user(user_name, user_password)
    r, song_added = add_song_to_DB(song_genre, song_year, song_performer, song_title)
    r, playlist_added = add_playlist(user_name, user_password, playlist_name)
    r, song_added = add_song_to_PL(user_name, user_password, playlist_name, song_title)

    playlist = get_playlist(user_name, user_password, playlist_name)
    first_rating = get_song_rank(song_title, playlist)
    r = song_upvote(user_name, user_password, playlist_name, song_title)
    r = song_upvote(user_name, user_password, playlist_name, song_title)
    assert response_ok(r), r.json()["error"]
    playlist = get_playlist(user_name, user_password, playlist_name)
    assert not get_song_rank(song_title, playlist) - 1 == first_rating


def test_get_songs_greater_than(clearSongsDB, clearUsersDB):
    song_genre = "Mid"
    song_year = "2021"
    song_performer = "Omer Adam"
    user_name = "Barak"
    user_password = "1010"
    playlist_name = "BPlay"
    song_title = "Millionaires19"
    rank = '1'
    op = "greater"
    # set conditions
    r, user_added = add_user(user_name, user_password)
    r, song_added = add_song_to_DB(song_genre, song_year, song_performer, song_title)
    r, playlist_added = add_playlist(user_name, user_password, playlist_name)
    r, song_added = add_song_to_PL(user_name, user_password, playlist_name, song_title)
    r = song_upvote(user_name, user_password, playlist_name, song_title)
    r = song_upvote(user_name, user_password, playlist_name, song_title)

    r, songs = get_songs_by_rank(rank, op)
    assert response_ok(r), r.json("error")
    assert check_ranks_of_songs(songs, rank, op)


def test_get_songs_less_than(clearSongsDB, clearUsersDB):
    song_genre = "Mid"
    song_year = "2021"
    song_performer = "Omer Adam"
    user_name = "Barak"
    user_password = "1010"
    playlist_name = "BPlay"
    song_title = "Millionaires19"
    rank = '1'
    op = "less"
    # set conditions
    r, user_added = add_user(user_name, user_password)
    r, song_added = add_song_to_DB(song_genre, song_year, song_performer, song_title)
    r, playlist_added = add_playlist(user_name, user_password, playlist_name)
    r, song_added = add_song_to_PL(user_name, user_password, playlist_name, song_title)

    r, songs = get_songs_by_rank(rank, op)
    assert response_ok(r), r.json("error")
    assert check_ranks_of_songs(songs, rank, op)

def test_get_songs_equal_to(clearSongsDB,clearUsersDB):
    song_genre = "Mid"
    song_year = "2021"
    song_performer = "Omer Adam"
    user_name = "Barak"
    user_password = "1010"
    playlist_name = "BPlay"
    song_title = "Millionaires19"
    rank = '1'
    op = "eq"
    # set conditions
    r, user_added = add_user(user_name, user_password)
    r, song_added = add_song_to_DB(song_genre, song_year, song_performer, song_title)
    r, playlist_added = add_playlist(user_name, user_password, playlist_name)
    r, song_added = add_song_to_PL(user_name, user_password, playlist_name, song_title)
    r = song_upvote(user_name, user_password, playlist_name, song_title)

    r,songs = get_songs_by_rank(rank,op)
    assert response_ok(r),r.json("error")
    assert check_ranks_of_songs(songs,rank,op)

def test_songs_rate_less_than_0(clearSongsDB,clearUsersDB):
    song_genre = "Mid"
    song_year = "2021"
    song_performer = "Omer Adam"
    user_name = "Barak"
    user_password = "1010"
    playlist_name = "BPlay"
    song_title = "Millionaires19"
    rank = '0'
    op = "less"
    # set conditions
    r, user_added = add_user(user_name, user_password)
    r, song_added = add_song_to_DB(song_genre, song_year, song_performer, song_title)
    r, playlist_added = add_playlist(user_name, user_password, playlist_name)
    r, song_added = add_song_to_PL(user_name, user_password, playlist_name, song_title)
    r, songs = get_songs_by_rank(rank, op)
    assert response_ok(r), r.json("error")
    assert  not songs

