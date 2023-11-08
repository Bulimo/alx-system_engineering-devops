#!/usr/bin/python3
"""
Script function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after="tmp"):
    """
    recursive function that returns all hot articles for a given subreddit
    return None if invalid subreddit given
    """
    # Define headers to mimic a web browser request
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    # Reddit API endpoint for fetching hot articles in a subreddit
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    if after != "tmp":
        url = url + "?after={}".format(after)
    response = requests.get(url, headers=headers, allow_redirects=False)

    # append top titles to hot_list
    results = response.json().get('data', {}).get('children', [])
    if not results:
        return hot_list
    for title in results:
        hot_list.append(title.get('data').get('title'))

    # get next param "after" else nothing else to recurse
    after = response.json().get('data').get('after')
    if not after:
        return hot_list
    return (recurse(subreddit, hot_list, after))
