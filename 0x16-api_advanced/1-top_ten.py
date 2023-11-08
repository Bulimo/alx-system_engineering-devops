#!/usr/bin/python3
"""
Script that queries the Reddit API and prints the titles of the first 10 hot
posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
        return top ten titles for a given subreddit
        return None if invalid subreddit given
    """
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    r = requests.get(url, headers=headers).json()
    top_titles = r.get('data', {}).get('children', [])
    if not top_titles:
        print(None)
    for title in top_titles:
        print(title.get('data').get('title'))
