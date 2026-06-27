# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # traverse left, self, right 
        # keeping track of count with a parameter 
        # in a helper function, when you reach the smallest 
        # incrememnt count till k-1 and return that value

        def helper(root, counter, k) : 
            
            if not root : 
                return counter, None

            #explore left
            counter, result = helper(root.left, counter, k)
            
            #explore self
            counter += 1
            if counter == k : 
                return counter, root.val
    
            if result :
                return counter, result

            #explore right
            return helper(root.right, counter, k)

        toReturn = helper(root, 0, k)
        return toReturn[1]
            
            
            # if right : 
            #     return right
           
            
            
                
            


        

        

