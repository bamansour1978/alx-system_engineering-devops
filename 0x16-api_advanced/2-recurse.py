#!/usr/bin/python3
"""Function 2"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code == 404:
        return None

    result = res.json().get("data")
    aft = result.get("after")
    count += result.get("dist")
    for i in result.get("children"):
        hot_list.append(i.get("data").get("title"))

    if aft is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
