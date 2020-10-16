# mutable types allow in place modification of content like list & dictionary
# immutable types do not allow in place changes, types like int are immutable types
def test_mutable():
    list = [1, 2, 3]
    list[0] = 4  # same list was modified --  mutable
    print(list)
    assert True


def test_immutable():
    x = 1
    x = x + 1  # now we've a new x since we're updating the value
    print(x)

    tuple = ("a", "b", "c")  # a tuple is immutable
    str = "foo"  # string is immutable too
    print(tuple)
    print(str)


def test_inefficient_to_better_to_best():
    # this is inefficient since string is immutable and we're assigning a new value for each iteration of for loop
    nums = ""  # empty string
    for n in range(20):
        nums += str(n)
    print(nums)

    # this is a better version
    nums = []  # now a mutable list
    for n in range(20):
        nums.append(str(n))
    print("".join(nums))

    # and this is the best option
    nums = [str(n) for n in range(20)]
    print("".join(nums))
