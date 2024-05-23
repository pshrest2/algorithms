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


def merge(a, left, mid, right):
    left_temp = a[left : mid + 1]
    right_temp = a[mid + 1 : right + 1]

    i = 0
    j = 0
    index = left
    while i < len(left_temp) and j < len(right_temp):
        if left_temp[i] <= right_temp[j]:
            a[index] = left_temp[i]
            i += 1
        else:
            a[index] = right_temp[j]
            j += 1

        index += 1

    while i < len(left_temp):
        a[index] = left_temp[i]
        index += 1
        i += 1

    while j < len(right_temp):
        a[index] = right_temp[j]
        index += 1
        j += 1
