"""
RECURSION - DSA Foundations

THEORY:
Recursion: Function calls itself with smaller instance
Base Case: When to stop recursion (critical!)
Recursive Case: Progress toward base case
Call Stack: Each call stored, limited by memory
Patterns: Linear recursion, binary recursion, divide & conquer, backtracking
Time: Often O(2^n) naive, O(n) with memoization
Use: Tree traversal, DFS, divide & conquer, backtracking, DP
"""

# ============================================================
# IMPLEMENTATION
# ============================================================

def factorial(n):
    """Example: Calculate n! recursively"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n, memo=None):
    """Example: Calculate nth Fibonacci with memoization"""
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


# ============================================================
# PROBLEMS
# ============================================================

def problem_1(x, n):
    """Power - Calculate x^n efficiently using divide & conquer"""
    power=1
    for i in range(n):
        if n==0:
            power*=n*1
        power*=problem_1(x,n)*problem_1(x,n)
        n=n//2
    return power


def problem_2(arr, index=0):
    """Sum of Array - Calculate total using linear recursion"""
    pass


def problem_3(arr, index=0):
    """Find Maximum - Recursively find largest element"""
    pass


def problem_4(arr, target, index=0):
    """Count Occurrences - Count element frequency recursively"""
    pass


def problem_5(nums):
    """Generate Permutations - Generate all orderings using backtracking"""
    pass