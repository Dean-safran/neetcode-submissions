# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p == q : 
            return p
            
        
        # you can use the fact that this is a binary 
        # search tree to rule things out

        # if p.val and q.val are both less than root.val
        # recurse on left child of root, if they are both greater 
        # then recruse on right
        
        # else return root

        if p.val < root.val and q.val < root.val : 
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val : 
            return self.lowestCommonAncestor(root.right, p, q)
        else : 
            if p.left == q or p.right == q :
                return p
            if q.left == p or q.right == p :
                return q
            return root
     

        