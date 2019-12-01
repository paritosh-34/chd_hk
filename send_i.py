import requests

my_url = "http://127.0.0.1:5000/post"

data = {
    "username": "user1",
    "tweet": "msg1",
    "image": open('test.png', 'rb'),
    "files" : [('media', ('test.png', open('test.png', 'rb'), 'png'))]
}
#files = {'media': open('test.png', 'rb')}
r = requests.post(url=my_url, data=data)