from instrafucture_layer import RestSender
import json
import pytest


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