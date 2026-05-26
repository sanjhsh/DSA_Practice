"""
HASHMAP (HASH TABLE) - DSA Foundations

THEORY:
HashMap: Maps keys to values using hash function
Hash Function: Converts key to index, should distribute evenly
Collisions: Handle via chaining (list at each index)
Time: Access/Insert/Delete O(1) average, O(n) worst
Load Factor: When n/capacity > 0.7, resize (double capacity)
When to use: Fast lookup, frequency counting, caching, two sum patterns
"""

# ============================================================
# IMPLEMENTATION
# ============================================================

class HashMap:
    """HashMap using chaining for collision handling"""
    
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]
    
    def _hash(self, key):
        """Compute hash index"""
        return hash(key) % self.capacity
    
    def put(self, key, val):
        """Insert or update key-value pair"""
        if self.size / self.capacity > 0.7:
            self._resize()
        
        idx = self._hash(key)
        bucket = self.buckets[idx]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, val)
                return
        
        bucket.append((key, val))
        self.size += 1
    
    def get(self, key):
        """Retrieve value for key"""
        idx = self._hash(key)
        bucket = self.buckets[idx]
        
        for k, v in bucket:
            if k == key:
                return v
        return None
    
    def _resize(self):
        """Double capacity when load factor exceeds threshold"""
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        
        for bucket in old_buckets:
            for k, v in bucket:
                self.put(k, v)


# ============================================================
# PROBLEMS
# ============================================================

def problem_1(nums, target):
    """Two Sum - Find two indices whose values sum to target"""
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
    return None


def problem_2(s, t):
    """Valid Anagram - Check if strings are anagrams"""
    if len(s)!=len(t):
        return False
    for ch in s:
        if s.count(ch)!=t.count(ch):
            return False
    return True
            


def problem_3(strs):
    """Group Anagrams - Group strings that are anagrams"""
    pass


def problem_4(nums):
    """Contains Duplicate - Check if array has duplicates"""

    for ch in nums:
        if nums.count(ch)>1:
            return True
    return False


def problem_5(nums):
    """Majority Element - Find element appearing > n/2 times"""
    pass


def problem_6(ransom_note, magazine):
    """Ransom Note - Check if note can be formed from magazine letters"""
    pass


def problem_7(s, t):
    """Isomorphic Strings - Check if strings follow consistent mapping"""
    pass


def problem_8(s):
    """First Unique Character - Find first non-repeating character"""
    pass