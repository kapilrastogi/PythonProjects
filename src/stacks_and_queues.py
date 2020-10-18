from collections import deque


def balance_parenthesis(line):
    print('')
    d = deque()
    for i in line:
        if i == '{':
            d.appendleft('}')
        elif i == '[':
            d.appendleft(']')
        elif i == '(':
            d.appendleft(')')
        elif i == ')' or i == '}' or i == ']':
            if i != d.popleft():
                return False
    return True
