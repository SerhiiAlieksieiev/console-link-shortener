import requests

headers = {
    "Authorization": "Bearer bbf5c519e9eb62def990efcdd45fd4493ec3f468"
}
request_body = {
    "long_url": "https://dvmn.org/referrals/OvAywtzW0kcxmIhjzmTwreLGC4ouzEFjJfgcOUbo/"
}

url = "https://api-ssl.bitly.com/v4/shorten"
response = requests.post(url, json=request_body, headers=headers)
response.raise_for_status()

print(response.json())