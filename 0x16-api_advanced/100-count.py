#!/usr/bin/python3
"""
Script that queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords .
"""
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    returns sorted count list title of all hot articles from given keywords
    return None if f no posts match or the subreddit is invalid
    """
    if after is None:
        word_count = {}
    # Define headers to mimic a web browser request
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    response = requests.get(url, headers=headers, params={"after": after})
    if response.status_code != 200:
        return
    data = response.json()
    for post in data['data']['children']:
        title = post['data']['title']
        for word in word_list:
            if word.lower() in title.lower():
                if word.lower() in word_count:
                    word_count[word.lower()] += 1
                else:
                    word_count[word.lower()] = 1
    after = data['data']['after']
    if after is None:
        sorted_word_count = sorted(
            word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_word_count:
            print(f"{word}: {count}")
    else:
        count_words(subreddit, word_list, after, word_count)
