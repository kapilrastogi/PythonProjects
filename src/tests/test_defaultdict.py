#!/usr/bin/python

# subclass of built-in dict class, makes use of default_factory
from collections import defaultdict


def test_defaultdict():
    # array of key-val pairs
    s = [('yellow', 1), ('blue', 2), ('yellow', 3)]
    d = defaultdict(list)  # this means that default values are "new" list
    print('')
    print(d)  # defaultdict(<class 'list'>, {})
    for k, v in s:
        d[k].append(v)  # since default factory is list, we can now use append
    print(d)  # defaultdict(<class 'list'>, {'yellow': [1, 3], 'blue': [2]})

    # equivalently we could use existing constructs for this
    d = {}
    for k, v in s:
        d.setdefault(k, []).append(v)
    print(d)  # {'yellow': [1, 3], 'blue': [2]}

    s = 'mississippi'
    d = defaultdict(int)
    for x in s:
        d[x] += 1
    print(d)  # defaultdict(<class 'int'>, {'m': 1, 'i': 4, 's': 4, 'p': 2})

    s = [('yellow', 1), ('blue', 2), ('yellow', 3)]
    s.append(['red', 1])
    s.append(['red', 5])
    d = defaultdict(set)
    for k, v in s:
        d[k].add(v)
    print(d)  # defaultdict(<class 'set'>, {'yellow': {1, 3}, 'blue': {2}, 'red': {1, 5}})
