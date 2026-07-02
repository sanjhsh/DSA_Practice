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
    #         if character>=0 and character<=0:
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
    num=0
    current=""
    stack=[]
    for character in s:
        if character.isdigit():
            num=num*10+int(character)
        elif character=="[":
            stack.append((current,num))
            current=""
            num=0 
        elif character=="]":
            prev_string,num=stack.pop()
            current=prev_string+num*current

        else:
            current+=character
    return current

def problem_4(heights):
    """Largest Rectangle in Histogram - Find max area rectangle"""
    # prev_smaller=-1
    # next_smaller=len(heights)-1
    # for i in range(0,len(heights)-1):
    #     while heights[i]>=prev_smaller:
    #         prev_smaller=heights[i]
    #     while heights[i]>=next_smaller:
    #         next_smaller=heights[i]
    #     area=max(max,heights[i]*next_smaller-prev_smaller-1)
    # return maxprev_smaller=-1
    # next_smaller=len(heights)-1
    # for i in range(0,len(heights)-1):
    #     while heights[i]>=prev_smaller:
    #         prev_smaller=heights[i]
    #     while heights[i]>=next_smaller:
    #         next_smaller=heights[i]
    #     area=max(max,heights[i]*next_smaller-prev_smaller-1)
    # return max
    # prev_stack=[]
    # next_stack=[]
    # prev_value=heights[0]
    # next_value=heights[len(heights)-1]
    # for i in range(0,len(heights)-1):
    #     prev_stack.append(0)
    #     for j in range(i,1,-1):
    #         if prev_value>j:
    #             prev_stack.append((i))
    #             prev_value=heights[i]
    #         else:
    #             stack.pop()
    #     next_stack.append(heights[len(heights)-1])
    #     for j in range(i,len(heights)-1):
    #         if next_value>j:
    #             next_stack.append((i))
    #             next_value=heights[i]   
    #         else:
    #             stack.pop()
    #     area=max(max,heights[i]*next_value-prev_value-1)
    # return area



    stack=[]
    max_area=0
    for i in range (0,len(heights)):

        if len(stack)==0:
            stack.append(i)
        elif heights[i]>=heights[stack[-1]]:
            stack.append(i)
        else:
            while stack and heights[i] < heights[stack[-1]]:
                j=stack.pop()
                height=heights[j]
                right=i
                left=stack[-1] if stack else -1
                width=right-left-1
                area=height*width
                max_area = max(max_area, area) 
            stack.append(i)

    while stack:             
        j = stack.pop()
        height = heights[j]
        right = len(heights)
        left = stack[-1] if stack else -1
        width = right - left - 1
        max_area = max(max_area, height * width)

    return max_area

def problem_5():
    """Queue using Stacks - Implement FIFO with two LIFO stacks"""
    
    class QueueOperations():
        def __init__(self):
            self.stack1=[]
            self.stack2=[]   
        def push(self,element):
            self.stack1.append(element)   

        def pop(self):
            if len(self.stack2)==0:
                while self.stack1:
                    j=self.stack1.pop()
                    self.stack2.append(j)
            if len(self.stack2)!=0:
                return self.stack2.pop()

        def peek(self):
            if len(self.stack2) == 0:
                while self.stack1:
                    j = self.stack1.pop()
                    self.stack2.append(j)

            if len(self.stack2) != 0:
                return self.stack2[-1]

            
    return QueueOperations()

def problem_6(temperatures):
    """Daily Temperatures - Find next warmer day for each day"""
    stack=[]
    for i in range(0,len(temperatures)):
        found=False
        for j in range(i+1,len(temperatures)):
            if temperatures[j]>temperatures[i]:
                stack.append(j-i)
                found=True
                break
        if found==False:
            stack.append(0)
    return stack


def problem_7():
    """Recent Calls Counter - Track function calls in time window"""
    from collections import deque
    class RecentCounter():
        def __init__(self):
            self.queue=deque()
        def ping(self,t):
            self.queue.append(t)
            while len(self.queue)!=0 and t-3000>=self.queue[0]:
                self.queue.popleft()
            return len(self.queue)
    return RecentCounter()      


def problem_8(height):
    """Trapping Rain Water - Calculate trapped water between bars"""
    pass                                                                                 