def test_str_operations():
    foo = 'foo'
    bar = 'bar'
    foobar = foo + bar  # this is good as assigning to a new variable
    print(foobar)

    foo += 'ooo'  # this is not good, reassigning to the same string value
    foo = ".".join([foo, 'ooo'])  # this is better
    print(foo)


def test_format():
    foo = 'foo'
    bar = 'bar'
    foobar = '%s %s' % (foo, bar)  # this is okay but not preferred
    print(foobar)

    foobar = '{0} {1}'.format(foo, bar)  # this one is better
    print(foobar)

    foobar = '{x} {y}'.format(x=foo, y=bar)  # this is the best
    print(foobar)