#!/bin/python3

import math
import os
import random
import re
import sys
import requests


#
# Complete the 'topArticles' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts INTEGER limit as parameter.
# base url for copy/paste:
# https://jsonmock.hackerrank.com/api/articles?page=<pageNumber>
#

def topArticles(limit):
    # Write your code here
    articles = list()
    page_number = 1
    while True:
        resp = requests.get(
            f"https://jsonmock.hackerrank.com/api/articles?page={page_number}")

        body = resp.json()
        articles.extend(body["data"])

        if page_number >= body["total_pages"]:
            break

        # Improvements: once you know the total_pages,
        # you can requests the next pages in concurrency.
        # this would decrease O(total_pages) to ~O(2)

        page_number += 1

    articles.sort(key=lambda art: (art["num_comments"] or 0,
                                   art["title"] or art["story_title"] or ""),
                  reverse=True)

    for art in articles[:20]:
        print(art["num_comments"], art["title"] or art["story_title"])

    return list(map(lambda art: art["title"] or art["story_title"] or next,
                    articles[:limit]))


if __name__ == '__main__':
    for limit in [7]:
        res = topArticles(limit)
        # print("\n".join(res))
