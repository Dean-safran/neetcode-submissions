# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, lower, upper) : 
            if not node : 
                return True
            if not node.left and not node.right : 
                return True
            if node.left and (node.left.val >= node.val or not (lower < node.left.val and node.left.val < upper)) :
                return False
            if node.right and (node.right.val <= node.val or not (lower < node.right.val and node.right.val < upper)) :
                return False
            return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)
        return helper(root, -1001, 1001)   


    



        
