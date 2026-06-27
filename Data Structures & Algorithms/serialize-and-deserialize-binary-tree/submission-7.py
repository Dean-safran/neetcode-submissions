# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# time and space analysis is at the end
class Codec:
    """todo : implement delimited version with commas (a list) and 
    review neetcode solns """

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


#each node value is at most 4 chars long, 
    # plus a prefix of max length 3,
    # so the output space string for serialize is o(n)
    # recursion depth for serialize is also o(n) space
    
    # each node is processed once in constant time, so 
    # overall o(n) time

    # using pointers to scan the serialized 
    # tree string for deserialize is o(1) space, recursion 
    # is o(tree_height) space, output tree is o(n) space, n being 
    # number of nodes

    # As we scan through the list we recursively build 
    # the tree. Since we only do one pass of the list 
    # with constant operations at each char, time is o(n) 

    # overall time and space for both functions together is 
    # o(n) 


    # Encodes a tree to a single string.
        

