#!/usr/bin/python3
"""Function 2"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """list_titles"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    parametrs = {
        "after": after,
        "count": count,
        "limit": 100
    }
    res = requests.get(url, headers=headers, params=parametrs, 
                       allow_redirects=False)
    if res.status_code == 404:
        return None

    result = res.json().get("data")
    aftr = result.get("after")
    count += result.get("dist")
    for c in result.get("children"):
        hot_list.append(c.get("data").get("title"))

    if aftr is not None:
        return recurse(subreddit, hot_list, aftr, count)
    return hot_list
