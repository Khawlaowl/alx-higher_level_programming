#!/usr/bin/python3
class MyList(list):
    """A subclass of the list base class"""

    def print_sorted(self):
        """Print the list sorted in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
        return sorted_list  # If you want to return the sorted list
