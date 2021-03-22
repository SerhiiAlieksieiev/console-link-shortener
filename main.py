import requests

def shorten_link(token, url):
    headers = {
        "Authorization": token
    }
    request_body = {
        "long_url": url
    }
    request_url = "https://api-ssl.bitly.com/v4/shorten"
    response = requests.post(request_url, json=request_body, headers=headers)
    response.raise_for_status()
    bitlink = response.json()['link']
    return bitlink

def main():
    long_url = input()
    bitly_token = "Bearer bbf5c519e9eb62def990efcdd45fd4493ec3f468"

    try:
        print('Битлинк', shorten_link(bitly_token, long_url))
    except requests.exceptions.HTTPError as e:
        print("Ошибка \n {}".format(e))

if __name__ == '__main__':
    main()