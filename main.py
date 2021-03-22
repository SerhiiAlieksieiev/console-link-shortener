import os

import dotenv
import requests


def shorten_link(token, url):
    request_url = "https://api-ssl.bitly.com/v4/shorten"
    try:
        response = requests.post(request_url, json=url, headers=token)
        response.raise_for_status()
        bitlink = response.json()['link']
        return bitlink
    except requests.exceptions.HTTPError as e:
        return ("Ошибка \n {}".format(e))


def count_clicks(token, url):
    request_url = f"https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks"
    try:
        response = requests.get(request_url, headers=token)
        response.raise_for_status()
        clicks_count = response.json()['link_clicks'][0]['clicks']
        return clicks_count
    except requests.exceptions.HTTPError as e:
        return ("Ошибка \n {}".format(e))


def check_bitlink(token, url):
    reqest_url = f"https://api-ssl.bitly.com/v4/bitlinks/{url}"
    try:
        response = requests.get(reqest_url, headers=token)
        response.raise_for_status()
        return True
    except requests.exceptions.HTTPError:
        return False


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
        print('Количество кликов: ', count_clicks(headers, link))
    else:
        print('Битлинк', shorten_link(headers, body))


if __name__ == '__main__':
    main()
