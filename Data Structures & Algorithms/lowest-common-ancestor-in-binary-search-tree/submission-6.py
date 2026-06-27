# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # you can use the fact that this is a binary 
        # search tree to rule things out

        # if p.val and q.val are both less than root.val
        # recurse on left child of root, if they are both greater 
        # then recruse on right
        
        # else return root

        # finding the ancestor takes log n time since
        # we're searching through a binary search tree, 
        # that means we have log n space aswell for the 
        # recursive call stack
            
        toReturn = root
        while True : 
            if p.val < toReturn.val and q.val < toReturn.val : 
                toReturn = toReturn.left
            elif p.val > toReturn.val and q.val > toReturn.val : 
                toReturn = toReturn.right
            elif toReturn.val == p.val : 
                return toReturn
            elif toReturn.val == q.val : 
                return toReturn
            else : 
                return toReturn
            



        
     

        