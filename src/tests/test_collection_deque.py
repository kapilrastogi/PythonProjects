#!/usr/bin/python

from collections import deque

# deque is generalization of stacks and queues (thread-safe), appends/pops are O(1)
# deque could be bounded to a length, that'd mean items will be discarded

# list is similar but the costs for pop(0) and insert(0,v) is O(n)
from src.stacks_and_queues import balance_parenthesis


def test_deque():
    print('')
    d = deque('ghi')
    for e in d:
        print(e.upper(), end=' ')

    assert d.pop() == 'i'  # pop from right side
    assert d.popleft() == 'g'  # pop from the left side

    d.append('j')  # append to right
    d.appendleft('f')  # append to left

    list(d)  # list conversion
    assert d[0] == 'f'
    assert d[-1] == 'j'


def test_deque_reverse_and_extend():
    my_list = [1, 5, 7, 3]
    d = deque(reversed(my_list))
    print('')
    assert d.popleft() == 3

    d.extend('ghi')  # add new iterable to queue (mixed types now integer & characters)
    print(d)
    assert d.pop() == 'i'
    d.reverse()
    print(d)
    assert d.pop() == 7
    assert d.popleft() == 'h'


def test_stack():
    assert balance_parenthesis("{([])}") is True
    assert balance_parenthesis("{(][)}") is False


def test_insert_and_index():
    print('')
    my_list = [1, 5, 1, 3]
    d = deque(reversed(my_list))  # reversed the list
    d.extend('ghi')
    print(d)  # deque([3, 1, 5, 1, 'g', 'h', 'i']) at this point

    assert d.index(1) == 1  # find index of value
    assert d.index(1, 2, 5) == 3  # find index of value after start and before end index


def test_remove_and_rotate():
    print('')
    my_list = [1, 5, 1, 3]
    d = deque(reversed(my_list))
    d.extend('ghi')
    d.reverse()  # reverse in place
    print(d)  # deque(['i', 'h', 'g', 1, 5, 1, 3]) at this point

    d.remove(1)  # removes the first instance of the value (other 1 will still be left)
    assert d.index(1) == 4

    d.rotate(1)  # rotate to right
    assert d.index(1) == 5
    d.rotate(-1)  # rotate to left
    assert d.index(1) == 4


def test_max_len():
    print('')
    my_list = [1, 5, 1, 3]
    d = deque(reversed(my_list), 5)
    d.extend('ghi')
    print(d)  # deque([5, 1, 'g', 'h', 'i'], maxlen=5) at this point

    d.append(10)
    assert d.pop() == 10
    assert d.popleft() == 1
