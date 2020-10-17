import re
from src.IteratorExample import IteratorExample


def test_iterator():
    print('\n')
    my_list = ["a", "b", "c"]
    for x in IteratorExample(my_list):
        print(x, end=' ')

    example = IteratorExample(["a", "b", "c"])
    myit = iter(example)
    while True:
        try:
            item = next(myit)
            print(item, end=' ')
        except StopIteration:
            break


def test_iter():
    my_tuple = ("banana", "mango", "apple")
    myit = iter(my_tuple)
    while True:
        try:
            item = next(myit)
            print(item)
        except StopIteration:
            break
