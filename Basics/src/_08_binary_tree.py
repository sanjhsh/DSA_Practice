"""
BINARY TREE - DSA Foundations

THEORY:
Binary Tree: Each node has 0-2 children, hierarchical structure
Traversals: DFS (inorder, preorder, postorder), BFS (level order)
Height: Longest root-to-leaf path, O(log n) for balanced, O(n) unbalanced
BST: Left < Node < Right, enables efficient search
Patterns: Recursive DFS, level order with queue, path problems, LCA
Types: Full, complete, perfect, balanced, BST, degenerate
"""

from collections import deque

# ============================================================
# IMPLEMENTATION
# ============================================================

class TreeNode:
    """Single node in binary tree"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    """Binary Tree operations"""
    
    def __init__(self, root=None):
        self.root = root
    
    def inorder(self, node=None):
        """DFS: Left → Root → Right"""
        if node is None:
            node = self.root
        if not node:
            return []
        
        result = []
        result.extend(self.inorder(node.left))
        result.append(node.val)
        result.extend(self.inorder(node.right))
        return result
    
    def level_order(self):
        """BFS: Level-by-level"""
        if not self.root:
            return []
        
        result = []
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            result.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right: 
                queue.append(node.right)
        
        return result
    
    def height(self, node=None):
        """Calculate tree height"""
        if node is None:
            node = self.root
        if not node:
            return -1
        
        return 1 + max(self.height(node.left), self.height(node.right))


# ============================================================
# PROBLEMS
# ============================================================

def problem_1(root):
    """Maximum Depth - Find maximum distance from root to leaf"""
    if root is None:
        return 0
    left= problem_1(root.left)
    right=problem_1(root.right)
    
    return 1+ max(left,right)



def problem_2(root):
    """Invert Binary Tree - Mirror the tree structure"""
    if root is None:
        return 
    problem_2(root.left)
    problem_2(root.right)
    root.left,root.right=root.right,root.left
    return root

def problem_3(p, q):
    """Same Tree - Check if two trees are identical"""
    if p or q is None:
        return
    array_1=[]
    array_2=[]
    node_1=problem_1(p.left)
    array_1.push(node_1)
    node_2=problem_2(q.left)




def problem_4(root):
    """Symmetric Tree - Check if tree is mirror image of itself"""
    pass


def problem_5(root):
    """Level Order Traversal - BFS returning levels as separate lists"""
    pass


def problem_6(root, target_sum):
    """Path Sum - Find if root-to-leaf path sums to target"""
    pass


def problem_7(root, p, q):
    """Lowest Common Ancestor in BST - Find LCA using BST properties"""
    pass


def problem_8(root):
    """Validate BST - Check if tree satisfies BST properties"""
    pass