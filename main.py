import os

import dotenv
import requests


def shorten_link(token, url):
    request_url = "https://api-ssl.bitly.com/v4/shorten"
    response = requests.post(request_url, json=url, headers=token)
    response.raise_for_status()
    bitlink = response.json()['link']
    return bitlink


def count_clicks(token, url):
    request_url = f"https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks"
    response = requests.get(request_url, headers=token)
    response.raise_for_status()
    clicks_count = response.json()['link_clicks'][0]['clicks']
    return clicks_count


def check_bitlink(token, url):
    reqest_url = f"https://api-ssl.bitly.com/v4/bitlinks/{url}"
    response = requests.get(reqest_url, headers=token)
    return response.ok

def main():
    dotenv.load_dotenv('.env')
    bitly_token = os.environ['BITLY_TOKEN']
    link = input()
    headers = {
        "Authorization": bitly_token
    }
    body = {
        "long_url": link
    }

    if check_bitlink(headers, link):
        try:
            print('Количество кликов: ', count_clicks(headers, link))
        except requests.exceptions.HTTPError as e:
            print("Ошибка \n {}".format(e))
    else:
        try:
            print('Битлинк', shorten_link(headers, body))
        except requests.exceptions.HTTPError as e:
            print("Ошибка \n {}".format(e))


if __name__ == '__main__':
    main()
