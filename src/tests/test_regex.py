#!/usr/bin/python
import re


def test_regex():
    # matches
    matches = re.match("a*b", "aaabcd ab cde")
    if matches:
        print(matches.group())
        # print(matches.group(1))
    else:
        print("no match")

    seraches = re.search("a*b", "aaabcd ab cde")
    if seraches:
        print(seraches.group())
        # print(seraches.group(1))
    else:
        print("no match")
