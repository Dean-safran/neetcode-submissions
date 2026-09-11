# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """

        BFS, when we reach a new level, return the right most element (the one processed last)

        When adding new elements to the queue, add (element, level), if queue.next[1]==curr_level+1
        add element to res
        
        """

        if not root : 
            return []
        
        q = deque()
        q.append((root, 0))
        res = []

        while q :
            curr, level = q.popleft()
            if curr.left :
                q.append((curr.left, level + 1))
            if curr.right : 
                q.append((curr.right, level + 1))

            # if this is the last node on this level
            if not q or q[0][1] > level :
                res.append(curr.val)
        
        return res