# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
         if root == None : 
            return "1#"
         return f"{len(str(root.val))}{root.val}{self.serialize(root.left)}{self.serialize(root.right)}"

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        pointer = 0
        def helper(data) : 
            nonlocal pointer
            
            toMove = int(data[pointer])
            pointer += 1

            if data[pointer] == "#" :
                pointer += 1
                return None
            
            value = ""
            for _ in range(toMove) :
                 value += data[pointer]
                 pointer += 1
            value = int(value)
            root = TreeNode(value)

            root.left = helper(data)
            root.right = helper(data)
            return root
        return helper(data)
        

