# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """

        each node returns its depth and balanced (boolean)
        if either left or right's balanced value is False, return false
        else return abs(left_depth - right_depth) <= 1

        """

        def DFS(curr) :
            if not curr.left and not curr.right :
                return 0, True
            
            if not curr.left :
                r_depth, balanced = DFS(curr.right)
                r_depth += 1
                if r_depth > 1 :
                    return r_depth, False
                else :
                    return r_depth, True
            
            elif not curr.right :
                l_depth, balanced = DFS(curr.left)
                l_depth += 1
                if l_depth > 1 :
                    return l_depth, False
                else :
                    return l_depth, True
            
            else :
                r_depth, r_balanced = DFS(curr.right)
                l_depth, l_balanced = DFS(curr.left)
                if not r_balanced or not l_balanced :
                    return max(r_depth, l_depth) + 1, False
                return max(r_depth, l_depth) + 1, abs(r_depth - l_depth) <= 1
        if not root :
            return True
        else :
            _, balanced = DFS(root)
        return balanced

            

                    
