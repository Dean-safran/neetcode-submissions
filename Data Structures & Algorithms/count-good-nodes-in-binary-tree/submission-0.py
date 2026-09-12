# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def DFS(curr, MAX) :
            if not curr.left and not curr.right :
                if curr.val >= MAX :
                    res.append(curr.val)
            else :
                if curr.val >= MAX :
                    MAX = curr.val
                    res.append(curr.val)

                if curr.left :
                    DFS(curr.left, MAX)
                
                if curr.right :
                    DFS(curr.right, MAX)
        
        res = []
        DFS(root, -float('inf'))
        return len(res)