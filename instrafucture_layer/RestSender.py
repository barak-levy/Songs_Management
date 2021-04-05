import requests

def send_post_message(path,message):
    try:
        r= requests.request('POST',url=path,json=message)
        return r
    except requests.exceptions.RequestException as e:
        print("exception:" , e)


def send_get_message(path):
    try:
        r=requests.request('GET',url=path)
        return r
    except requests.exceptions.RequestException as e:
        print(e)


def send_delete_message(path):
    try:
        r= requests.request('DELETE',url=path)
        return r
    except requests.exceptions.RequestException as e:
        print(e)


def send_put_message(path,message):
    try:
        r = requests.request('PUT',url=path,json=message)
        return r

    except requests.exceptions.RequestException as e:
        print(e)

