Python offers a variety of built-in data structures to help you organize and manipulate data efficiently. Here are some of the most commonly used data structures in Python:

Lists:

Lists are ordered collections of items. They can hold elements of different data types.
Example: my_list = [1, 2, 3, 'apple', 'banana']
Tuples:

Tuples are similar to lists, but they are immutable, meaning their elements cannot be modified after creation.
Example: my_tuple = (1, 2, 3, 'apple', 'banana')
Sets:

Sets are unordered collections of unique elements. They are useful for tasks like removing duplicates from a list.
Example: my_set = {1, 2, 3, 4, 4}
Dictionaries:

Dictionaries store key-value pairs, allowing you to access values by their associated keys.
Example: my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
Strings:

Strings are sequences of characters. They can be indexed and sliced just like lists or tuples.
Example: my_string = "Hello, World!"
Arrays (from the array module):

Arrays are similar to lists but can only hold elements of the same data type for improved performance.
Example: import array; my_array = array.array('i', [1, 2, 3, 4, 5])
Stacks and Queues (using lists or collections.deque):

Stacks and queues are abstract data types that can be implemented using lists or the collections.deque class.
Example: Stack using a list: my_stack = [], Queue using collections.deque: from collections import deque; my_queue = deque()
Linked Lists (custom implementation or using libraries):

Linked lists can be implemented as a custom data structure or by using libraries like collections.deque.
Heaps (using the heapq module):

Heaps are binary trees used for priority queues and can be implemented using the heapq module.
Example: import heapq; my_heap = [3, 1, 4, 1, 5, 9, 2]
Dictionaries (using the collections.defaultdict):

A specialized dictionary from the collections module that allows default values for missing keys.
Example: from collections import defaultdict; my_dict = defaultdict(int)
Ordered dictionaries (using the collections.OrderedDict):

A dictionary that maintains the order of keys based on their insertion order.
Example: from collections import OrderedDict; my_ordered_dict = OrderedDict({'a': 1, 'b': 2, 'c': 3})
Sets (using the set data structure):

The built-in set data structure can be used to perform set operations like union, intersection, and difference.
Example: set1 = {1, 2, 3}, set2 = {3, 4, 5}
These are some of the fundamental data structures in Python. Depending on your specific needs, you can choose the appropriate data structure to efficiently manage and manipulate your data.
