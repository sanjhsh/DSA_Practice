"""
ARRAYS & STRINGS - DSA Foundations

THEORY:
Arrays: Contiguous memory, O(1) access, O(n) insertion/deletion
Strings: Immutable sequences, similar to arrays
Key Patterns: Two-pointer, sliding window, in-place modifications
Time: Access O(1), Search O(n), Insert/Delete O(n), Append O(1) amortized
When to use: Ordered collections, fast random access, as foundation for other DS
"""

# ============================================================
# IMPLEMENTATION
# ============================================================

class DynamicArray:
    """Simple dynamic array implementation"""
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.array = [None] * self.capacity
    
    def append(self, value):
        """Add element, resize if needed"""
        if self.size == self.capacity:
            self.capacity *= 2
            new_array = [None] * self.capacity
            for i in range(self.size):
                new_array[i] = self.array[i]
            self.array = new_array
        
        self.array[self.size] = value
        self.size += 1
    
    def get(self, index):
        """Get element at index"""
        if 0 <= index < self.size:
            return self.array[index]
        return None
    
    def to_list(self):
        """Convert to Python list"""
        return self.array[:self.size]


# ============================================================
# PROBLEMS
# ============================================================

def problem_1(nums, target):
    """Two Sum - Find two indices that sum to target"""
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
    return None 


def problem_2(s):
    """Valid Palindrome - Check if string is palindrome (ignore spaces/case)"""
    cleaned_string=""
    for ch in s:
        if ch.isalnum():
            cleaned_string+=ch.lower()
    if len(s)==0:
        return False
    for i in range(len(s)//2):
            if cleaned_string[i]!=cleaned_string[len(cleaned_string)-1-i]:
                return False
    return True


def problem_3(s):
    """Reverse String - Reverse array in-place"""
    low=0
    array_len=len(s)
    high=len(s)-1
    mid=(low+high)//2

    for i in range(low,mid):
        s[i],s[array_len-1]=s[array_len-1],s[i]
        array_len-=1

    

def problem_4(nums):
    """Remove Duplicates - Remove duplicates from sorted array in-place"""
    if len(nums)==0:
        return False

    k=1
    for i in range(1,len(nums)):
        if nums[i]!=nums[i-1]:
            nums[k]=nums[i]
            k+=1
    return k


def problem_5(nums, k):
    """Rotate Array - Rotate array right by k positions"""
    if len(nums)==0:
        return False
    k=k%len(nums)
    for _ in range(k):
        temp=nums[-1]
        for j in range(len(nums)-1,0,-1):
            nums[j]=nums[j-1]

        nums[0]=temp
    