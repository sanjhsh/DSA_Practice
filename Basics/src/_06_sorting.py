"""
SORTING - DSA Foundations

THEORY:
Bubble Sort: O(n^2), simple, stable, good for nearly sorted
Insertion Sort: O(n^2) worst, O(n) best, good for small/nearly sorted
Merge Sort: O(n log n) guaranteed, divide & conquer, stable, O(n) space
Stable: Equal elements maintain relative order
In-place: Doesn't use extra space
When: Python's sort() uses Timsort (hybrid), use in production
"""

# ============================================================
# IMPLEMENTATION
# ============================================================

def bubble_sort(arr):
    """Bubble Sort - Compare adjacent elements"""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def insertion_sort(arr):
    """Insertion Sort - Build sorted array incrementally"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    """Merge Sort - Divide & Conquer"""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return _merge(left, right)


def _merge(left, right):
    """Helper: Merge two sorted arrays"""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ============================================================
# PROBLEMS  
# ============================================================

def problem_1(arr):
    """Sort Array with Bubble Sort"""
    for i in range(0,len(arr)):
        swapped=False
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break
    return arr
def problem_2(arr):
    """Sort Array with Insertion Sort"""
    # for i in range(1,len(arr)-1):
    #     key=arr[i]
    # while j<key & j<(len(arr)-1):





def problem_3(arr):
    """Sort Array with Merge Sort"""
    pass


def problem_4(arr):
    """Sort Colors - Partition array with three values (0, 1, 2)"""
    pass


def problem_5(arr1, arr2):
    """Merge Sorted Arrays - Combine two sorted arrays"""
    pass