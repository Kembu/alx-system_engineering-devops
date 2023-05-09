#!/usr/bin/python3

""" get top 10 hot topics from reddit """
import requests


def top_ten(subreddit):
    """ function to get the top 10 topics """

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": 'Chrome-book'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json()

        for post in posts['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
