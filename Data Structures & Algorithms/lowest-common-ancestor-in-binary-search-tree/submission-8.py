# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if p.val and q.val are both less than root.val
        # recurse on left child of root, if they are both greater 
        # then recruse on right

        # finding the ancestor takes log n time since
        # we're searching through a binary search tree, 
        # with iterative DFS we use o(1) space

        # The main idea is to use a 
        # pointer to find the node where 
        # p and q are not on the same branch,
        # this is where we should stop traversing 

        # p or q being this split node, or p and q being 
        # direct children of this split node are all 
        # covered in an else statement, no matter what 
        # you return this splitting node
        
            
        toReturn = root
        while True : 
            if p.val < toReturn.val and q.val < toReturn.val : 
                toReturn = toReturn.left
            elif p.val > toReturn.val and q.val > toReturn.val : 
                toReturn = toReturn.right
            else : 
                return toReturn
            



        
     

        