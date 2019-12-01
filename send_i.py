import requests

my_url = "http://35.173.150.151:5000/post"

data = {
    "username": "user1",
    "tweet": "msg1",
    "image": open('test.png', 'rb')
}
r = requests.post(url=my_url, data=data)