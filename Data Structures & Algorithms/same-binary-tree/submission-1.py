# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # maybe recursively search through both trees 
        # at once, if at any point one node doesn't equal
        # another something is wrong

        # post-order explore tree self, left, right
        
        if not p or not q :  
            if p != q :  
                return False
            # if they are both none, you can't recurse 
            # any further so return True
            return True 
        elif p.val != q.val : 
            return False
            
        
        left = self.isSameTree(p.left, q.left)  
        right = self.isSameTree(p.right, q.right)

        if not (left and right) : 
            return False
        return True

