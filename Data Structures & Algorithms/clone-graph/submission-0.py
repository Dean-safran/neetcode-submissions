"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        queue = deque()
        mp = {}
        queue.append(node)
        
        if node == None :
            return

        while queue :
            curr = queue.popleft()
            if curr not in mp :
                curr_copy = Node(curr.val, None)
                mp[curr] = curr_copy

            for neighbor in curr.neighbors :
                if neighbor not in mp :
                    queue.append(neighbor)
                    neighbor_copy = Node(neighbor.val, None)
                    mp[neighbor] = neighbor_copy
                mp[curr].neighbors.append(mp[neighbor])
        return mp[node]
        

        # initialize a deque called queue (use .append and .popleft)

        # append intial node to queue
        # intialize mp that connects original nodes to copies 
        # to handle duplicates/cycles
        
        # while not queue : 
        
        # curr = popped node to be processed

        # create curr_copy 
        # mp[curr] = curr_copy 

        # curr_neighbors = node.neighbors

        # for neighbor in curr_neighbors :
        #   if neighbor not in mp : 
        #       create neighbor_copy
        #       mp[neighbor] = neighbor_copy
        #       and append to curr_copy.neighbors
        #       then append neighbor to queue
        #   else :
        #       append mp[neighbor] to curr.neighbors

        # once while loop ends return result


        