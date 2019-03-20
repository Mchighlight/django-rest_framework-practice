import os
from PIL import Image
import json
import requests

AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/"
AUTH_REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"
ENDPOINT = "http://127.0.0.1:8000/api/status/"


### Test Jwt authentication
post_header = {
    'content-type': 'application/json'
}

data = {
    'username' : 'Mchighlight@gmail.com',
    'password' : 'Mc110164'
}

r = requests.post(AUTH_ENDPOINT, data= json.dumps(data), headers=post_header)
token = r.json()['token']
print(token)
headers = {
    'Content-Type': 'application/json',
    'Authorization': "JWT " + token,
}

post_data = json.dumps({"content": "Some randome shit"})
posted_reponse = requests.post(ENDPOINT, data=post_data, headers=headers)
print(posted_reponse.text)
'''
print(token)
refresh_data = {
    'token': token
}
new_r = requests.post(AUTH_REFRESH_ENDPOINT, data= json.dumps(refresh_data), headers=post_header)
print(new_r.json())
'''
### Test Basic permission
'''
get_endpoint = ENDPOINT + str(3)
post_data = json.dumps({"content": "HAHAHA"})

r = requests.get(ENDPOINT)
print(r.status_code)

r_one = requests.get(get_endpoint)
print(r_one.text)



post_header = {
    'content-type': 'application/json'
}
post_response = requests.post(ENDPOINT, data=post_data, headers=post_header)
print(post_response.text)
'''

### Test Image
'''
# FIXME: form and framework update okay but request doesn't work
def do_img(method='get', data={}, is_json=True, img_path=None ):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data=json.dumps(data)
    if img_path is not None:
        with open(img_path, 'rb') as image_b:
            file_data = { 
                'image' :image_b
            }
            r = requests.post(ENDPOINT, data=data, files = file_data, headers=headers)
    else :
        r = requests.request(method, ENDPOINT, data=data, headers=headers)
    print(r.text)
    print(r.status_code)
    return r


img_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test.jpg")
do_img(method='post', data={'user':1, "content":"123"}, is_json=False, img_path=img_path )
'''

### TEST one endpoint CRUD
'''
def do(method='get', data={}, is_json=True ):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data=json.dumps(data)
    r = requests.request(method, ENDPOINT, data=data, headers=headers)
    print(r.text)
    print(r.status_code)
    return r




#do(method='delete', data={'id':'16'})
#do(data={'id': 16})
#do(method='put', data={'id':9, "content": "some cool69 new content", "user": "1"})
##do(method='post', data={"content": "some cool123 new content", 'user' : 1})
'''