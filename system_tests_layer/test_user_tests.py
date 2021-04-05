#import logics_layer.User_Handler,logics_layer.Responses_Handler
from logics_layer.User_Handler import *
from logics_layer.Responses_Handler import   *

def test_add_user(clearUsersDB):
    r,user_added=add_user("Barak","1010")
    assert response_ok(r),r.json()["error"]
    r,user_recived,message=get_user(user_added)
    #print(user_recived["data"]["user_name"])
    #print("Barak!!!!!!")
    assert user_added==user_recived["user_name"],message


def test_add_friend():
    r=add_friend("Barak","1010","Paz Davidov")
    assert response_ok(r),r.json()["error"]
    r,user_recived,message=get_user("Barak")
    assert "Paz Davidov" in  user_recived["friends"],message

