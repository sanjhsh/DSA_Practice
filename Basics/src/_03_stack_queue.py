"""
STACK & QUEUE - DSA Foundations

THEORY:
Stack (LIFO): Last in, first out. Push/pop from top. O(1) for all ops.
Queue (FIFO): First in, first out. Enqueue/dequeue. O(1) for deque.
Stack uses: Undo/redo, DFS, expression evaluation, bracket matching
Queue uses: BFS, task scheduling, message queues
Monotonic patterns: Stack for nearest greater/smaller, decreasing from bottom
"""

from collections import deque

# ============================================================
# IMPLEMENTATION
# ============================================================

class Stack:
    """Stack (LIFO) using list"""
    
    def __init__(self):
        self.items = []
    
    def push(self, val):
        """Add element to top"""
        self.items.append(val)
    
    def pop(self):
        """Remove and return top"""
        return self.items.pop() if self.items else None
    
    def peek(self):
        """View top without removing"""
        return self.items[-1] if self.items else None
    
    def is_empty(self):
        """Check if empty"""
        return len(self.items) == 0


class Queue:
    """Queue (FIFO) using deque"""
    
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, val):
        """Add to rear"""
        self.items.append(val)
    
    def dequeue(self):
        """Remove from front"""
        return self.items.popleft() if self.items else None
    
    def peek(self):
        """View front"""
        return self.items[0] if self.items else None
    
    def is_empty(self):
        """Check if empty"""
        return len(self.items) == 0


# ============================================================
# PROBLEMS
# ============================================================

def problem_1(s):
    """Valid Parentheses - Check if brackets are correctly matched"""
    if len(s)%2!=0:
        return False
    stack=[]
    # len_of_array=len(s)//2
    # forward_stack=[]
    # for i in range(0,len_of_array-1):
    #     forward_stack.append(i)
    # reverse_stack=[]
    # for i in range(len_of_array,len(s),-1):
    #     reverse_stack.append(i)
    # if forward_stack==reverse_stack:
    #     return True
    # return False
    for i in s:
        if i=="(":
           stack.append(")")
        elif i=="[":
            stack.append("]")
        elif i=="{":
            stack.append("}")
        elif i==")":
            if stack.pop()!=")":
                return False
        elif i=="]":
            if stack.pop()!="]":
                return False
        elif i=="}":
            if stack.pop()!="}":
                return False
    return True

def problem_2():
    """Min Stack - Track minimum element in O(1)"""
    class MinStack:
        def __init__(self):
            self.stack=[]
            self.minStack=[]

        def push(self,val):
            self.stack.append(val) 
            val=min(val,self.minStack[-1] if self.minStack else val)      
            self.minStack.append(val)
        def pop(self):
            return self.stack.pop()
            self.minStack.pop()
        def top(self):
            return self.stack[-1]

        def getMin(self):
            return self.minStack[-1]
    return MinStack()


def problem_3(s):
    """Decode String - Expand nested bracket patterns"""
    # current_state=0
    # stack=[]
    # char_count=0
    # result=""
    # poped_element=stack.pop()
    # if len(s)!=0:
    #     for character in s:
    #         if type(character) is int:
    #             current_state=current_state
    #         elif character=="[":
    #             stack.append("[")
    #         elif type(character) is char:
    #             stack.append(character)
    #             char_count+=1
    #         elif character=="]":
    #             for i in range(1,char_count):
    #                 for j in range(1,current_state-1):
    #                     result.append(poped_element+poped_element)
    #             char_count=0
    #     return result

    # return False


def problem_4(heights):
    """Largest Rectangle in Histogram - Find max area rectangle"""
    pass


def problem_5():
    """Queue using Stacks - Implement FIFO with two LIFO stacks"""
    pass


def problem_6(temperatures):
    """Daily Temperatures - Find next warmer day for each day"""
    pass


def problem_7():
    """Recent Calls Counter - Track function calls in time window"""
    pass


def problem_8(height):
    """Trapping Rain Water - Calculate trapped water between bars"""
    pass