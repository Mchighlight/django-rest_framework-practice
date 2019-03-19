import os
from PIL import Image
import json
import requests

ENDPOINT = "http://127.0.0.1:8000/api/status/one_endpoint/"

def do(method='get', data={}, is_json=True ):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data=json.dumps(data)
    r = requests.request(method, ENDPOINT, data=data, headers=headers)
    print(r.text)
    print(r.status_code)
    return r


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

#do(method='delete', data={'id':'16'})
#do(data={'id': 16})
#do(method='put', data={'id':9, "content": "some cool69 new content", "user": "1"})
##do(method='post', data={"content": "some cool123 new content", 'user' : 1})