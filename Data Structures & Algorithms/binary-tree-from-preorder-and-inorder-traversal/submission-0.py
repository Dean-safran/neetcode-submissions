# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    preorderIndex = 0
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # find root in preorder

        # find it's index in in-order using hashmap

        # everything to the left is in the left branch 
        # everything to the right is the right branch 

        # call helper on preorder[1:] since 
        # we just processed a root, then 
        # on left/right side of root in in-order
        
        #create index hashmap for inorder
        inorderMap = defaultdict(int)
        for i in range(len(inorder)) : 
            inorderMap[inorder[i]] = i

        #write helper function with pointers as paramters
        # we need pointers to increment preorder EVERY time, 
        # no matter the branch? and we need pointers for in order
        self.preorderIndex = 0
        def helper(self, preorder, inorder, l, r) :
            #base case
            if l > r :
                return None
            if r - l == 0 :
                self.preorderIndex += 1
                return TreeNode(inorder[l])
            
            root_val = preorder[self.preorderIndex]
            self.preorderIndex += 1
            
            root = TreeNode(root_val)
            
            rootIndexInorder = inorderMap[root_val]
           
            root.left = helper(self, preorder, inorder, l, rootIndexInorder - 1 )   #left side if it exists
            root.right = helper(self, preorder, inorder, rootIndexInorder + 1, r)  #right side if it exists
            return root  
            
        return helper(self, preorder, inorder, 0, len(inorder) - 1)

