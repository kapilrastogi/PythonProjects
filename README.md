# Python projects

Any python (.py) file is a module, and a bunch of module in a directory is a package (need a __init__.py file in directory)

Top level package can have __main__.py file, this is the file that runs with python -m "collection"

## Imports
python packages don't have knowledge about their siblings but they can reference their parent by (..)

# Java to python mapping
| Java             |  Python       |
| ---------------- | ------------- |
| map              | dict, defaultdict, Counter|
| LinkedHashMap    | OrderedDict |
| set              | set|
| stacks & queues  | deque |
| array            | list|
| PriorityQueue    | heapq, PriorityQueue (thread-safe)|

# Notes
* Difference between PriorityQueue and heapq - PriorityQueue is a thread-safe class which wraps heapq (which is not thread-safe). 

# References
* Import system https://docs.python.org/3/reference/import.html
* Relative vs absolute imports https://realpython.com/absolute-vs-relative-python-imports/
* Style guide https://www.python.org/dev/peps/pep-0008/
* Zen of python https://www.python.org/dev/peps/pep-0020/
* Implicit namespace package https://www.python.org/dev/peps/pep-0420/

* Package structuring https://dev.to/codemouse92/dead-simple-python-project-structure-and-imports-38c6
* Package structuring https://docs.python-guide.org/writing/structure/

* Anti pattern http://docs.quantifiedcode.com/python-anti-patterns/correctness/not_using_get_to_return_a_default_value_from_a_dictionary.html

# Run
python -m <module-name> e.g. python -m src 

## Testing
https://docs.pytest.org/en/stable/
Python testing including test runners https://realpython.com/python-testing/

python -m pytest test_mutable_immutable.py

# TODO
* heapq custom comparator
* Matrix (2D array)
* Sorting using comparator
* Text processing services https://docs.python.org/3/library/text.html
* What is --system-site-package
* Decorator, context manager, dynamic typing
* ChainMap & OrderedDict https://docs.python.org/3/library/collections.html
* itertools https://docs.python.org/3/library/itertools.html
* functools https://docs.python.org/3/library/functools.html
* map, filter & reduce https://book.pythontips.com/en/latest/map_filter.html