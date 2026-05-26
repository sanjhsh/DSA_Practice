"""
BINARY SEARCH - DSA Foundations

THEORY:
Binary Search: Efficient search for sorted arrays, O(log n)
Eliminates half per iteration using divide & conquer
Variants: Exact value, first/last occurrence, closest value, insertion point
Key: Must have sorted data, careful with boundaries, mid = left + (right-left)//2
Mistakes: Off-by-one errors, integer overflow, not handling edge cases
When: Fast lookup needed, monotonic property exists
"""

# ============================================================
# IMPLEMENTATION
# ============================================================

def binary_search_iterative(arr, target):
    """Standard binary search (iterative)"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def find_first_occurrence(arr, target):
    """Find leftmost occurrence (handles duplicates)"""
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


# ============================================================
# PROBLEMS
# ============================================================

def problem_1(arr, target):
    """Search in Sorted Array - Standard binary search"""
    low=0
    high=len(arr)
    mid=low+high//2
    if arr[mid]>target:
        high=mid-1
    elif arr[mid]<target:
        low=mid+1
    elif arr[mid]==target:
        return mid
    for i in range(low,high):
        if arr[i]==target:
            return i
    return -1
    
        


def problem_2(arr, target):
    """Find First and Last Position - Find range of target occurrence"""
    low=0
    high=len(arr)-1

    left_index=-1
    right_index=-1
    
    while low<=high:
        mid=(low+high)//2
        if arr[mid]<target:
            low=mid+1
        elif arr[mid]>target:
            high=mid-1
        else:
            left_index=mid
            high=mid-1

    low=0
    high=len(arr)-1

    while low<=high:
        mid=(low+high)//2
        if arr[mid]>target:
            high=mid-1
        elif arr[mid]<target:
            low=mid+1
        else:
            right_index=mid
            low=mid+1

    return [left_index,right_index]

def problem_3(arr, target):
    """Search Insert Position - Find target or insertion point"""
    low=0
    high=len(arr)-1

    while low<=high:
        mid=high+low//2
        if arr[mid]==target:
            return mid

        elif arr[mid]>target:
            high=mid-1

        else:
            low=mid+1

    return low



def problem_4(arr):
    """Peak Element - Find mountain peak efficiently"""
    low=0
    high=len(arr)-1
    while low<high:
        mid=(low+high)//2
        if arr[mid]<arr[mid+1]:
            low=mid+1

        else:
             high=mid 
    return low

def problem_5(arr, target):
    """Count Occurrences - Count frequency using binary search"""
    """for first element"""
    low=0
    high=len(arr)-1
    mid=(low+high)//2
    first_index

    if target<arr[mid]:
        high=mid-1
    elif target>arr[mid]:
        low=mid+1
    else:
        first_index=mid
    first_index=low
    
    last_index
    if target<arr[mid]:
        high=mid-1
    elif target>arr[mid]:
        low=mid+1
    else:
        last_index=mid
    last_index=low

    count = last_index-first_index+1
    return count