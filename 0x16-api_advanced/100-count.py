#!/usr/bin/python3
"""Function 100"""
import requests
from collections import Counter


def count_words(subreddit, word_list, instances=None, after="", count=0):
    """function .

    Args:
        subreddit :str
        word_list :list
        instances :obj
        after :str
        count :int
    """
    if instances is None:
        instances = Counter()

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête : {e}")
        return

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")

    for c in results.get("children"):
        title = c.get("data").get("title").lower().split()
        for word in word_list:
            times = title.count(word.lower())
            instances[word] += times

    if after is None:
        if not instances:
            print("")
            return

        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print(f"{k}: {v}") for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
