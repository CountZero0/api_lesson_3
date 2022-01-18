import os
import argparse
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv

parser = argparse.ArgumentParser()
parser.add_argument('url')
args = parser.parse_args()


def shorten_link(url, token):
    bitly_url = f'https://api-ssl.bitly.com/v4/shorten'
    headers = {
        "Authorization": token,
    }
    payload = {
        "long_url": url,
    }
    response = requests.post(bitly_url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(url, token):
    bitly_url = f'https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary'
    headers = {
        'Authorization': token,
    }
    response = requests.get(bitly_url, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(url, token):
    bitly_url = f'https://api-ssl.bitly.com/v4/bitlinks/{url}'
    headers = {
        'Authorization': token,
    }
    response = requests.get(bitly_url, headers=headers)
    return response.ok


def main():
    load_dotenv()
    token = os.getenv('TOKEN')
    url = args.url
    parsed = urlparse(url)
    parsed_url = parsed.netloc + parsed.path
    if is_bitlink(parsed_url, token):
        try:
            print('Количество переходов по ссылке битли:', count_clicks(parsed_url, token))
        except requests.exceptions.HTTPError as error:
            exit(f"{error}")
    else:
        try:
            print(shorten_link(url, token))
        except requests.exceptions.HTTPError as error:
            exit(f"{error}")


if __name__ == '__main__':
    main()
