# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """ take max(self + l, self + r, self + r + l) 
        if this local value is greater than the global value,
        update the global value
        """
        # at each node, we do constant max comparisons to update 
        # result and local, totaling o(1) per node, so o(n) total

        # recursion depth is o(h) space where h is the height of the 
        # tree
        
        result = -1001
        def helper(root) :
            nonlocal result

            if root == None :
                return 0

            l = helper(root.left)
            r = helper(root.right)
            result = max(result, root.val, root.val + l, root.val + r, root.val + l + r)
            local = max(root.val, root.val + l, root.val + r)
            return local

        helper(root)
        return result
