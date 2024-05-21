def insertion_sort(a: list[int | float]):
    """
    Perform insertion sort. This method does not return a new sorted list.
    Instead, it mutates the input list and sorts it in place.

    Time complexity: O(n^2)
    Space complexity: O(1)

    Params:
    - a: unsorted input list
    """
    if not a:
        return

    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key