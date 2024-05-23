from typing import Optional


def selection_sort(a: list[int | float], desc: Optional[bool] = False):
    """
    Perform selection sort.

    Time complexity: O(n^2)
    Space complexity: O(1)

    Params:
    - a: unsorted input list
    - desc: bool flag to sort in descending order
    """
    if not a:
        return

    n = len(a)

    def compare(a, b):
        return a > b if desc else a < b

    for i in range(0, n - 1):
        min_index = i
        for j in range(i + 1, n):
            if compare(a[j], a[min_index]):
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]


def insertion_sort(a: list[int | float], desc: Optional[bool] = False):
    """
    Perform insertion sort.

    Time complexity: O(n^2)
    Space complexity: O(1)

    Params:
    - a: unsorted input list
    - desc: bool flag to sort in descending order
    """
    if not a:
        return

    n = len(a)

    def compare(a, b):
        return a < b if desc else a > b

    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and compare(a[j], key):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
