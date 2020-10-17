#!/usr/bin/python

# sequence types in python - list & tuple

def test_list():
    my_list = ["apple", "banana", "mango"]
    print(my_list)

    # item access using index
    assert (my_list[1] == "banana")

    # slicing in my_list
    print(my_list[:])
    print(my_list[1:])  # starting at the index
    print(my_list[:1])  # ending one before the index (n-1)

    # updating the my_list
    my_list[1] = "potato"
    assert (my_list[1] == "potato")

    # delete an item in the my_list
    del my_list[1]
    assert (my_list[1] == "mango")

    # length of the my_list
    assert (len(my_list) == 2)

    for x in my_list:
        print(x)

    # concatenation to my_list
    my_list = my_list + [True, False]

    # appending to my_list
    my_list.append(2010)
    assert (len(my_list) == 5)

    # repetition
    my_list = my_list * 2
    assert (len(my_list) == 10)
    print(my_list)

    # membership
    assert ("apple" in my_list), "apple not found"

    old_list = ["a", "b", "c"]
    assert (min(old_list) == "a")
    assert (max(old_list) == "c")

    # convert a tuple to list
    t = ("a", "b", 200)
    new_list = list(t)
    print(new_list)

    # extend the list (essentially adding another list to existing list. append adds 'one' element not list
    old_list.extend(new_list)
    assert (len(old_list) == 6)

    # count finds out how many instances of the object appears in the list
    print(old_list)
    assert (old_list.count("a") == 2)

    # remove first occurrence of the value
    old_list.remove("a")
    assert (old_list.count("a") == 1)

    old_list.reverse()
    print(old_list)

    # copy & insert
    final_list = old_list.copy()
    final_list.insert(2, "wow")
    print(final_list)

    # clear
    old_list.clear()
    assert (len(old_list) == 0)

    # returns first index of the value
    assert (final_list.index('b', 2) == 5)
