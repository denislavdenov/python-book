#!/usr/bin/env python3

from typing import Any

def linear_search_while(lst: list, value: Any) -> int:
    """Return the index of the first occurrence of value in lst, or return -1 if value is not in lst.
    >>> linear_search([2, 5, 1, -3], 5)
    1
    >>> linear_search([2, 4, 2], 2)
    0
    >>> linear_search([2, 5, 1, -3], 4)
    -1
    >>> linear_search([], 5)
    -1
    """
    # examine the items at each index i in lst, starting at index 0:
    #    is lst[i] the value we are looking for?  if so, stop searching.
    i = 0
    while i != len(lst) and lst[i] != value: 
        i=i+1
    if i == len(lst): 
        return -1
    else:
        return i


def linear_search_for(lst: list, value: Any) -> int: 
    for i in range(len(lst)): 
        if lst[i] == value:
            return i 
    return -1


def linear_search_sentinel(lst: list, value: Any) -> int: 
    # Add the sentinel.
    lst.append(value)
    i=0
    # Keep going until we find value.
    while lst[i] != value: 
        i=i+1
    # Remove the sentinel.
    lst.pop()
    # If we reached the end of the list we didn't find value.
    if i == len(lst): 
        return -1
    else:
        return i




import time
from typing import Callable, Any

def time_it(search: Callable[[list, Any], Any], L: list, v: Any) -> float: 
    t1 = time.perf_counter() 
    search(L, v)
    t2 = time.perf_counter() 
    return (t2 - t1) * 1000.0


def print_times(v: Any, L: list) -> None:

    # Get list.index's running time.
    t1 = time.perf_counter()
    L.index(v)
    t2 = time.perf_counter()
    index_time = (t2 - t1) * 1000.0
    # Get the other three running times.
    while_time = time_it(linear_search_while, L, v)
    for_time = time_it(linear_search_for, L, v)
    sentinel_time = time_it(linear_search_sentinel, L, v)
    print("{0}\t{1:.2f}\t{2:.2f}\t{3:.2f}\t{4:.2f}".format(v, while_time, for_time, sentinel_time, index_time))


L = list(range(10000001))
print_times(10, L) # How fast is it to search near the beginning? 
print_times(5000000, L) # How fast is it to search near the middle? 
print_times(10000000, L) # How fast is it to search near the end?



def binary_search(L: list, v: Any) -> int:
    """Return the index of the first occurrence of value in L, or return -1 if value is not in L.
    >>> binary_search([1, 3, 4, 4, 5, 7, 9, 10], 1)
    0
    >>> binary_search([1, 3, 4, 4, 5, 7, 9, 10], 4)
    2
    >>> binary_search([1, 3, 4, 4, 5, 7, 9, 10], 5)
    4
    >>> binary_search([1, 3, 4, 4, 5, 7, 9, 10], 10)
    7
    >>> binary_search([1, 3, 4, 4, 5, 7, 9, 10], -3)
    -1
    >>> binary_search([1, 3, 4, 4, 5, 7, 9, 10], 11)
    -1
    >>> binary_search([1, 3, 4, 4, 5, 7, 9, 10], 2)
    -1
    >>> binary_search([], -3)
    -1
    >>> binary_search([1], 1)
    0
    """
    # Mark the left and right indices of the unknown section.
    i=0
    j = len(L) - 1
    while i != j + 1:
        m = (i + j) // 2
        if L[m] < v: 
            i=m+1
        else: 
            j=m-1
    if 0 <= i < len(L) and L[i] == v: 
        return i
    else:
        return -1



def find_largest(n: int, L: list) -> list:
    """Return the n largest values in L in order from smallest to largest.
    >>> L = [3, 4, 7, -1, 2, 5]
    >>> find_largest(3, L)
    [4, 5, 7]
    """
    copy = sorted(L) 
    return copy[-n:]