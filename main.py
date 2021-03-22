import requests

def shorten_link(token, url):
    headers = {
        "Authorization": token
    }
    request_body = {
        "long_url": url
    }
    request_url = "https://api-ssl.bitly.com/v4/shorten"
    try:
        response = requests.post(request_url, json=request_body, headers=headers)
        response.raise_for_status()
        bitlink = response.json()['link']
        return bitlink
    except requests.exceptions.HTTPError as e:
        print("Ошибка \n {}".format(e))


def count_clicks(token, url):
    headers = {
        "Authorization": token
    }
    params = {
        "units" : -1
    }
    request_url = f"https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks"
    response = requests.get(request_url, params=params, headers=headers)
    response.raise_for_status()
    clicks_count = response.json()['link_clicks'][0]['clicks']
    return clicks_count

def main():
    #long_url = input()
    bitly_token = "Bearer bbf5c519e9eb62def990efcdd45fd4493ec3f468"
    bitlink = input()

    #print('Битлинк', shorten_link(bitly_token, long_url))
    print('Количество кликов: ', count_clicks(bitly_token, bitlink))

if __name__ == '__main__':
    main()