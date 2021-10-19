import requests

def send_data(URL: str, my_data: dict):
    return requests.post(URL, data=my_data)