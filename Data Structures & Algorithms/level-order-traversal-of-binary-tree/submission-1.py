# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

# deque.append() adds to the back
# deque.popleft() removes from the front

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS, at each level add to a accumulator
        # list, then add to result list 

        # BFS is o(n), the queue and accumulator are 
        # o(n) space

        q = deque()
        q.append(root)
        result = []


        while q : 
            accum = []
            for i in range(len(q)):
                node = q.popleft()
                if not node : 
                    continue
                accum += [node.val]
                q.append(node.left)
                q.append(node.right)
            if accum : 
                result += [accum]
        return result
            






