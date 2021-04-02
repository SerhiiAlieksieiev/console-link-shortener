import argparse
import os
from urllib.parse import urlparse

import dotenv
import requests


def shorten_link(headers, payload):
    request_url = 'https://api-ssl.bitly.com/v4/shorten'
    response = requests.post(request_url, json=payload, headers=headers)
    response.raise_for_status()
    bitlink = response.json()['link']
    return bitlink


def count_clicks(headers, link):
    request_url = f'https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks'
    response = requests.get(request_url, headers=headers)
    response.raise_for_status()
    clicks_count = response.json()['link_clicks'][0]['clicks']
    return clicks_count


def check_bitlink(headers, link):
    reqest_url = f'https://api-ssl.bitly.com/v4/bitlinks/{link}'
    response = requests.get(reqest_url, headers=headers)
    return response.ok


def main():
    dotenv.load_dotenv('.env')
    bitly_token = os.environ['BITLY_TOKEN']

    parser = argparse.ArgumentParser(description="link shortener")
    parser.add_argument('url', help='print url')
    args = parser.parse_args()

    link_components = urlparse(args.url)
    netloc = link_components[1]
    path = link_components[2]
    link = f'{netloc}{path}'
    headers = {
        'Authorization': bitly_token
    }
    payload = {
        'long_url': args.url
    }

    try:
        if check_bitlink(headers, link):
            print('Количество кликов: ', count_clicks(headers, link))
        else:
            print('Битлинк', shorten_link(headers, payload))
    except requests.exceptions.HTTPError as http_error:
        print('Ошибка \n {}'.format(http_error))


if __name__ == '__main__':
    main()
