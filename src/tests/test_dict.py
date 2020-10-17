#!/usr/bin/python


def test_dict():
    my_dict = {"k1": "v1", "k2": "v2", "k3": "v3"}
    # clone = my_dict.fromkeys()
    # for x in clone.keys():
    #     print(x)

    # iterating over keys
    for x in my_dict.keys():
        print(x)

    # iterating over values
    for x in my_dict.values():
        print(x)

    # does dictionary contains key
    assert (("k2" in my_dict) is True)
    assert (my_dict.get("k1") == "v1")
    assert (my_dict.get("k5") is None)  # non-existent key
    assert (my_dict.get("k5", "v5") == "v5")  # non-existent key returning default value

    # iterating over key/value tuple
    for x in my_dict.items():
        print(x)
    for x in my_dict.keys():
        print(x + "<->" + my_dict.get(x))

    # add/update a value
    # if the key doesn't exist then add key & default value
    assert (my_dict.setdefault("k6", "v6") == "v6")
    # if the key exist then return the existing value but don't update
    assert (my_dict.setdefault("k6", "v7") == "v6")
    assert (my_dict.get("k6") == "v6")

    # add one dictionary to add to another
    dict1 = {"Ticker": "MSFT", "Price": 134.34}
    dict2 = {"Zip": 98052}
    dict1.update(dict2)

    # create a new dictionary from the keys of an existing dictionary and default value
    print(dict1)
    seq = ('Ticker', 'Price', 'Zip')

    new_dict = dict1.fromkeys(seq, 5)  # default value
    print(new_dict)

    assert dict1.pop("Ticker") == "MSFT"  # pop the item given the key and returns value
    print(new_dict.popitem())  # pops the last item added to dictionary
