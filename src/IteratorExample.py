#!/usr/bin/python


class IteratorExample:
    def __init__(self, input):
        self.data = input
        self.length = len(input)

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index = self.index + 1
        if self.index >= self.length:
            print('\n')
            raise StopIteration
        return self.data[self.index]
