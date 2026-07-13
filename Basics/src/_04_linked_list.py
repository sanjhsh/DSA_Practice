"""
LINKED LIST - DSA Foundations

THEORY:
Linked List: Nodes linked via pointers, no contiguous memory
Types: Singly (next only), Doubly (next+prev), Circular (last→first)
Operations: Insert/Delete head O(1), middle O(n), Search O(n)
Patterns: Two pointers (slow+fast, dummy node, reverse)
Use: Frequent insertion/deletion, unknown size, when no random access needed
"""

# ============================================================
# IMPLEMENTATION
# ============================================================

class Node:
    """Single node in linked list"""
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    """Singly Linked List"""
    
    def __init__(self):
        self.head = None
    
    def insert_at_head(self, val):
        """Insert at beginning - O(1)"""
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_tail(self, val):
        """Insert at end - O(n)"""
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
    
    def traverse(self):
        """Get list as array"""
        result = []
        curr = self.head
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result
    
    def reverse(self):
        """Reverse in-place - O(n)"""
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev


# ============================================================
# PROBLEMS
# ============================================================

def problem_1(head):
    """Reverse Linked List - Reverse nodes in-place"""
    prev=None
    curr=head
    while curr:
        nxt=curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
        

def problem_2(head):
    """Detect Cycle - Check for circular reference"""
    result=[]
    curr=head
    
    while curr!=None:
        if curr not in result:
            result.append(curr)
        else:
            return True
        curr=curr.next
    return False

def problem_3(head):
    """Find Middle - Find center node using two pointers"""
    slow=head
    fast=head
    length=0
    # while head:
    #     length+=1
    #     head=head.next
    # while fast and fast.next:
    #     slow=slow.next
    #     fast=fast.next.next
    # if length%2==0:
    #     return slow,slow.next
    # return slow
    while fast and fast.next:
         slow=slow.next
         fast=fast.next.next
    return slow

def problem_4(head1, head2):
    """Merge Sorted Lists - Combine two sorted lists"""
    curr1=head1
    curr2=head2
    merged_list=Node(0)
    # while curr1.next:
    #     curr1=curr1.next
    #     last1=curr1
    # last1=curr2
    # while curr1:
    #     if curr1>curr1.next:
    #         curr1.head,curr1.next=curr1.next,curr1.head
    # return curr1

    while curr1 and curr2:
        if curr1.val<curr2.val:
            merged_list.next=curr1.val

            curr2=curr2.next
        curr1=curr2.next
    return merged_list
def problem_5(head, n):
    """Remove Nth Node From End - Delete node n positions from end"""   
    pass


def problem_6(head, x):
    """Partition List - Split around pivot value"""
    pass


def problem_7(head):
    """Palindrome Linked List - Check if reads same forwards/backwards"""
    pass


def problem_8(head):
    """Swap Nodes in Pairs - Swap adjacent nodes"""
    pass