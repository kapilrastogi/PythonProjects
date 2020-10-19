#!/usr/bin/python
import re


def test_str_processing():
    # length of string
    assert 5 == len(" foo ")

    # strip whitespaces
    s = ' foo '
    print('')
    assert s.lstrip() == 'foo '
    assert s.lstrip().rstrip() == 'foo'  # string is immutable
    print(s)
    assert " foo ".strip() == "foo"

    # count
    word = "this is a test statement"
    assert 6 == word.count('t')
    assert 1 == word.count('test')  # interesting way to find if the string exists

    # indexOf(character or string) returns index
    assert 8 == word.find('a')
    assert 2 == word.find('is')
    assert 5 == word.rfind('is')  # finds from the right
    assert 5 == word.find('is a')  # slightly longer substring
    assert 5 == word.find('is', 3)
    assert -1 == word.find('ta ta')  # no match, return value is -1

    # find & index are pretty similar, index will throw exception if no match found
    assert 5 == word.index('is a')

    # contains(character or string) returns boolean
    assert ("test" in word) is True

    # substring(index) or substring(startIndex, endIndex)
    # string[start:end:step] slicing (start is inclusive, end is NOT)
    assert "12" == "121212"[0:2]
    s = "121212"
    assert "111" == "121212"[0:len(s):2]
    assert "2" == "121212"[-1]  # last character
    assert "212" == "121212"[-3:]  # last three characters
    assert "22" == "121212"[1:-2:2]  # from 1st to 3rd last, with step 2
    assert "111" == "123123123"[::3]  # every third character

    # string equality
    assert "foo" == 'foo'

    # charAt(index) - returns character
    assert 't' == "returns"[2]

    # replace character in string (replace one/all)
    assert 'fat' == "rat".replace('r', 'f')
    assert 'rag gales' == "rat tales".replace('t', 'g')  # replace all matches
    assert 'rag tales' == "rat tales".replace('t', 'g', 1)  # replace count matches

    # concat strings
    assert "abc" == "a" + "bc"
    assert "a,b,c" == ','.join(['a', 'b', 'c'])

    # split the string on one/more delimiter
    assert ['a', 'b', 'c'] == "a,b,c".split(',')
    assert ['a,b', 'c'] == "a,b c".split()
    assert ['a', 'b c'] == "a b c".split(maxsplit=1)
    assert ['a', 'b', 'c'] == re.split("[,.]", "a,b.c")  # split on comma and dot

    # splits the string into three parts: part before the match, match & after match
    print("this is isla numbar".partition('is'))  # ('th', 'is', ' is isla numbar')

    # startsWith(string) or endsWith(string)
    assert "abc".startswith("ab") is True
    assert "abc".endswith("c") is True

    # test alphabetic numeric uppercase
    assert "ab17".isalpha() is False
    assert "17".isnumeric() is True
    assert "22".isdigit() is True
    assert "ABC" == "abc".upper()

    # reverse a string using slicing
    assert "cba" == "abc"[::-1]

    # convert string value to int (or int to string)
    assert 15 == int("15")
    assert "15" == str(15)


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
