# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# we DFS through the tree, each node gets checked with 
# BST rules in constant time, recursive callstack is 
# o(log n) at best and o(n) at worst in case of a degenerate
# tree, all nodes having one child

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, lower, upper) : 
            if not node : 
                return True
            if not (lower < node.val and node.val < upper) :
                return False
            return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)
        return helper(root, -1001, 1001)   


    



        
