#!/usr/bin/python
from collections import Counter


# Counter object have dictionary interface except it returns zero count for missing keys

# https://docs.python.org/3/library/collections.html
def test_collection_counter():
    print('')
    c = Counter()
    print(c)
    c = Counter('tequila')
    print(c['tequila'])
    c = Counter({'read': 4, 'blue': 2})
    print(c['blue'])
    c = Counter(cats=4, dogs=8)
    print(c['cats'])


def test_counter_as_frequency_map():
    print('')
    my_list = ["a", "b", "c", "a"]
    c = Counter(my_list)
    assert c['a'] == 2


def test_counter():
    print('')
    my_list = ["b", "a", "c", "a"]
    c = Counter(my_list)

    # find the most common elements (key & value pair), input is how many elements to return
    assert c.most_common(1) == [('a', 2)]
    assert c.most_common(2) == [('a', 2), ('b', 1)]

    # elements() returns all the elements (keys) one by one
    for x in sorted(c.elements()):
        print(x, end=',')
    print('')
    cnt1 = Counter(["b", "a", "c", "a"])
    cnt2 = Counter(b=1, a=1, c=2)
    cnt1.subtract(cnt2)
    print(cnt1)
    print(cnt2)
    for x in sorted(cnt1.elements()):
        print(x, end=',')


def test_counter_common_patterns():
    print('')
    cnt = Counter(["b", "a", "c", "a"])
    assert 4 == sum(cnt.values())
    print(cnt)
    print(list(cnt))  # list "unique" elements
    print(set(cnt))  # set "unique" elements
    print(dict(cnt))  # "dictionary with key/value (value is the count of individual keys)
    cnt.clear()
    assert 0 == sum(cnt.values())
    print(cnt)
