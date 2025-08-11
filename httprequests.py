import requests
import json

# HTTP GET
getRes = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print ('------------------')
print ('GET RESPONSE')
print (getRes.json())
print ('------------------')

# HTTP POST
postRes = requests.post('https://jsonplaceholder.typicode.com/todos', 
            data={"userId": 1, "id": 1, "title": "Jogging", "completed": False},
            #headers={"Content-type": "application/json; charset=UTF-8"}
            )
print ('------------------')
print ('POST RESPONSE')
print(postRes.json())
print ('------------------')

# HTTP PUT
putRes = requests.put('https://jsonplaceholder.typicode.com/posts/1',
                      data=json.dumps({"title": "new foo", "body": "new bar", "userId": 1}),
                      headers={"Content-type": "application/json; charset=UTF-8"})
print ('------------------')
print ('PUT RESPONSE')
print(putRes.json())
print ('------------------')

# HTTP PATCH
patchRes = requests.patch('https://jsonplaceholder.typicode.com/posts/1',
                      data={'"title": "new foo", "body": "new bar", "userId": 1'})
print ('------------------')
print ('PATCH RESPONSE')
print(patchRes.json())
print ('------------------')

# HTTP DELETE
delRes = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
print ('------------------')
print ('DEL RESPONSE')
print(delRes.json())
print ('------------------')

# FILTERING RESOURCES - GET REQUEST PARAMS
filterRes = requests.get('https://jsonplaceholder.typicode.com/posts',
             params={"userId":1, "id":1})
print ('------------------')
print ('FILTER RESPONSE')
jsonObject = filterRes.json()[0]
print(jsonObject['title'])
print ('------------------')