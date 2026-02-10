import requests
from requests.exceptions import HTTPError
from requests.auth import HTTPBasicAuth
import json

response = requests.get('https://api.github.com')
if response.status_code == 200:
    print("API call success")
else:
    raise Exception(f"exception occurred during API call {response.status_code}")

print('===================================================================================')

URLS = ['https://api.github.com', 'https://api.github.com/invalid']

for url in URLS:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP Error occurred : {http_err}')
    except Exception as ex:
        print(f'Other exception occurred: {ex}')
    else:
        print('API call success')

print('===================================================================================')

response = requests.get('https://api.github.com')
#print(f'Response in bytes: {response.content}')
#print(f'Response in string: {response.text}')
#print(f'Response in json format: {response.json()}')
#print(f'Parse items from json formatted response: {response.json()['gists_url']}')

print('===================================================================================')
#print(type(response.text))

response_dict = json.loads(response.text)
#print(response_dict['gists_url'])

print('===================================================================================')
#print(response.headers['Content-Type']) # can also be 'content-type' because it is case insensitive Dictionary

print('===================================================================================')
# PASSING PARAMS TO GET METHOD

# passing as dictionary
response = requests.get("https://api.github.com/search/repositories",
                        params={"q": "language:python", "sort": "stars", "order" : "desc"},
                        headers={"Accept": "application/vnd.github.text-match+json"})

# passing as tuple
# response = requests.get("https://api.github.com/search/repositories",
#                         [("q", "language:python"), ("sort", "stars"), ("order", "desc")])

# customise request headers


response_json = response.json()
popular_repos = response_json['items']

for repo in popular_repos[:3]:
    print(f"Repository name: {repo['name']}")
    print(f"Description: {repo['description']}")
    print(f"Stars: {repo['stargazers_count']}\n")

print('===================================================================================')

# other HTTP methods supported
# requests.get("https://httpbin.org/get")
# requests.post("https://httpbin.org/post", data={"key": "value"})
# requests.put("https://httpbin.org/put", data={"key": "value"})
# requests.delete("https://httpbin.org/delete")
# requests.head("https://httpbin.org/get")
# requests.patch("https://httpbin.org/patch", data={"key": "value"})
# requests.options("https://httpbin.org/get")

# passing HTTP method as param
#requests.request("GET", "https://httpbin.org/get")

print('===================================================================================')
# Sending request data

# dictionary - application/x-www-form-urlencoded
#requests.post("https://httpbin.org/post", data={"key": "value"})

# tuple - application/x-www-form-urlencoded
#requests.post("https://httpbin.org/post", data=[("key", "value")])

# json
#requests.post("https://httpbin.org/post", json={"key": "value"})

print('===================================================================================')

# Inspect the Prepared Request
#response = requests.post("https://httpbin.org/post", data={"name": "guru"})
#print(response.request.headers)
#print(response.request.body)

print('===================================================================================')
# USE AUTHORIZATION
response = requests.get("https://httpbin.org/basic-auth/user/passwd", 
                        # auth=("user", "passwd"))          by default HTTP Basic Auth
                        auth=HTTPBasicAuth('user', 'passwd'))
print(response.request.headers['Authorization'])

print('===================================================================================')
# PASS TOKEN IN AUTHORIZATION HEADER

from requests.auth import AuthBase

class TokenAuth(AuthBase):
    """Implements a token authentication scheme."""

    def __init__(self, token):
        self.token = token

    def __call__(self, request):
        """Attach an API token to the Authorization header."""
        request.headers["Authorization"] = f"Bearer {self.token}"
        return request
    
requests.get("https://api.github.com/user",
             auth=TokenAuth("YOUR_TOKEN_HERE"))

print('===================================================================================')
# SSL/TLS REQUESTS
requests.get("https://internal-api.company.com",
             verify="/path/to/company-ca.pem")
            #verify=False   to disable in Dev testing

print('===================================================================================')
# IMPROVE PERFORMANCE
# requests doesn’t support asynchronous HTTP requests directly. 
# If you need async support in your program, then you should try out HTTPX.

# set request timeout
from requests.exceptions import Timeout
requests.get("https://api.github.com", timeout=0.5) # in seconds
try:
    requests.get("https://api.github.com", timeout=(1, 3))   # (connection timeout, read timeout)
except Timeout as timeout:
    print(f"Timeout for API call {timeout}")
else:
    print('API successfully executed without timeout')


# RE-USE CONNECTIONS WITH SESSION OBJECTS
# Sessions are used to persist parameters across requests. 
# For example, if you want to use the same authentication across multiple requests

# from custom_token_auth import TokenAuth

# TOKEN = "<YOUR_GITHUB_PA_TOKEN>"

# with requests.Session() as session:
#     session.auth = TokenAuth(TOKEN)

#     first_response = session.get("https://api.github.com/user")
#     second_response = session.get("https://api.github.com/user")

# print(first_response.headers)
# print(second_response.json())


# RETRY FAILED REQUESTS
# from requests.adapters import HTTPAdapter
# from requests.exceptions import RetryError
# from urllib3.util.retry import Retry

# retry_strategy = Retry(
#     total=2,
#     status_forcelist=[429, 500, 502, 503, 504]
# )
# github_adapter = HTTPAdapter(max_retries=retry_strategy)

# with requests.Session() as session:
#     session.mount("https://api.github.com", github_adapter)
#     try:
#         response = session.get("https://api.github.com/")
#     except RetryError as err:
#         print(f"Error: {err}")

print('===================================================================================')