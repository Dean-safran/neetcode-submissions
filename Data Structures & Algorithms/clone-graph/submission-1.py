"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

""" 
Total Time/Work Done: o(v + e)
We process each node once when we enqueue and dequeue,
and we touch each edge twice (once from each end node), 

Space: o(v)
the map stores all nodes, the queue stores maximum all nodes but root
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:    
        if node == None :
            return

        queue = deque()
        mp = {node: Node(node.val)} # start the search by putting root in map
        # if it's in map it means node is visited
        queue.append(node)

        while queue :
            curr = queue.popleft()
            for neighbor in curr.neighbors :
                if neighbor not in mp :
                    queue.append(neighbor)
                    mp[neighbor] = Node(neighbor.val, None)
                mp[curr].neighbors.append(mp[neighbor])
        return mp[node]
        

        # initialize a deque called queue (use .append and .popleft)

        # append intial node to queue, and a copy of it to map
        # mp stores original nodes to their copies 
        # to handle duplicates/cycles
        
        # while not queue : 
        
        # curr = popped node to be processed

        # loop through curr's neighbors, if they're not in map, 
        # explore them by placing them in queue, if they are in map
        # they've been explored, and we only add the edge we found it 
        # by by appending the copy in map to curr_copy's neighbors

        # once while loop ends return result


        