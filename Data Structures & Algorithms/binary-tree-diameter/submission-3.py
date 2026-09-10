# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def DFS(curr) :
            # if leaf
            if not curr.left and not curr.right :
                return 0, 0
            
            if not curr.left :
                right_depth, right_diam = DFS(curr.right)
                return right_depth + 1, max(right_depth + 1, right_diam)
            elif not curr.right :
                left_depth, left_diam = DFS(curr.left)
                return left_depth + 1, max(left_depth + 1, left_diam)
            else : 
                right_depth, right_diam = DFS(curr.right)
                left_depth, left_diam = DFS(curr.left)
                return max(right_depth, left_depth) + 1, max(2+left_depth+right_depth, left_diam, right_diam)

        _, res = DFS(root)
        return res