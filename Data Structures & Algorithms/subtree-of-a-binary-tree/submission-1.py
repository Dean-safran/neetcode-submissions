# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # traverse original tree, once a node 
        # with same value as subtreeRoot check if 
        # it has the same structure as subtree with 
        # a helper function, otherwise continue the search
        
        # this is o(n * m), where 
        # m is the amount of nodes in subRoot,
        # if every node in root 
        # has same value as subRoot
        if not root : 
            if not subRoot : 
                return True
            return False
        if self.isSame(root, subRoot) : 
            return True
        else : 
            return False or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    
    def isSame(self, p, q) : 
        if not p and not q : 
            return True 
        if p and q and p.val==q.val : 
            return self.isSame(p.left, q.left) and self.isSame(p.right, q.right)
        else : 
            return False

