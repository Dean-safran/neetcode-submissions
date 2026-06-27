# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # each node gets processed once, with constant 
        # child swaps, recursion stack is maximum 
        # o(n) if the tree is imbalanced, meaning each 
        # node only has a left child or something

        # o(n) time and space complextiy 
        
        #recursively go down self, left, right
        if root == None : 
            return None

        # If even one child exists, don't do this block.
        # Only do if both children don't exist.
        if not (root.left or root.right) : 
            return root

        left = self.invertTree(root.left)
        right = self.invertTree(root.right) 
        root.left = right
        root.right = left
        return root 





