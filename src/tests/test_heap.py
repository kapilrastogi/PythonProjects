#!/usr/bin/python

import heapq


def print_heap_items(pq):
    while pq:
        print(heapq.heappop(pq), end=' ')


def test_heap():
    # building the heap one item at a time
    customers = []
    heapq.heappush(customers, (2, "Tom"))
    heapq.heappush(customers, (3, "Duck"))
    heapq.heappush(customers, (1, "Harry"))

    print("\n")

    data = [heapq.heappop(customers) for i in range(len(customers))]
    print(data)

    # building the heap from a given set of items
    pq = ["mango", "banana", "pineapple"]
    heapq.heapify(pq)
    print_heap_items(pq)

    # heappushpop pushes the specifies element into heap
    # and at the same time pops the top element from heap
    list_one = [5, 7, 12, 8, 4]
    heapq.heapify(list_one)
    assert heapq.heappushpop(list_one, 2) == 2
    assert heapq.heappushpop(list_one, 9) == 4

    # nlargest
    # nsmallest
    list_two = [6, 7, 9, 4, 3, 5, 8, 10, 1]
    heapq.heapify(list_two)
    assert [10, 9] == heapq.nlargest(2, list_two)
    assert [1, 3] == heapq.nsmallest(2, list_two)

    # heapreplace vs. heappushpop
    # heapreplace removes the item before adding
    # heappushpop adds the item before removing
    list_four = list_three = [5, 8, 12, 4]
    heapq.heapify(list_three)
    assert heapq.heapreplace(list_three, 3) == 4
    heapq.heapify(list_four)
    assert heapq.heappushpop(list_three, 3) == 3

    # merge
    first_list = [3, 7]
    second_list = [1, 10]
    assert [1, 3, 7, 10] == list(heapq.merge(first_list, second_list))

    from queue import PriorityQueue
    pq_customers = PriorityQueue()
    pq_customers.put(12)
    pq_customers.put(32)
    pq_customers.put(4)

    while pq_customers:
        print(pq_customers.get())
