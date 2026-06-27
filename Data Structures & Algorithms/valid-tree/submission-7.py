"""
Tests : 
(1) no node, n = 0
(2) one node, n = 1
(3) a simple three node chain and cycle
"""

"""
This is another cycle detection problem, the catch is we 
now have undirected edges, so we use DFS instead of topological sort

create node class with .val and .neighbors attributes

create node map(val: node)

create tree set

for i in range(n) :
    create node with val i
    node_map(i) = node

if n == 1 :
    return True


for node1_val, node2_val in edges : 
    node1 = node_map[node1_val]
    node2 = node_map[node2_val]
    node1.neighbors += [node2]
    node2.neighbors += [node1]
    if node1 not in tree_set :
        tree_set.add(node1)
    if node2 not in tree_set : 
        tree_set.add(node2)

if len(tree_set) < n :
    return False   #there are nodes with no edges, which means
                   #they cannot form a tree with the other nodes

start DFS (detect_cycle) on node_map[0]

detect_cycle should have two parameters the node to process and its value, when we
visit a node we mark that it's visited by changing
its value to #, when we backtrack, we change it back to the
val parameter of that call (which is the value of the node)

base case : if the value of the current node is #, 
return True

for neighbor in node.neighbors :
    if detect_cycle(neighbor, neighbor.val) : 
        return False #cycle detected, so not a valid tree
return True



"""

"""
time : o(v+e) = o(v)
We process every node once, changing it's value to #,
We process every outgoing edge of a node once in the direction 
we're exploring (we don't visit nodes we just visited)
Also, e is actually o(v) here since we do a constant check at the
beginning, if the amount of edges is greater than (or less than)
v-1 then the graph cannot be a tree

space : o(v+e) = o(v)
We store every node and its adjacencies (edges) with our node class, 
but for the same reasoning as the time complexity, e is o(v)
"""
class Node :
    def __init__(self, val=0, neighbors=None) :
        self.val = val;
        if not neighbors :
            self.neighbors = []
        else :
            self.neighbors = neighbors

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1 : 
            return False
        
        node_map = {}
        #it's best practice to use a visited set 
        visited = set()

        #create nodes
        for i in range(n) : 
            node_map[i] = Node(i, None)
        
        #connect edges
        for node1_val, node2_val in edges : 
            node1 = node_map[node1_val]
            node2 = node_map[node2_val]
            node1.neighbors += [node2]
            node2.neighbors += [node1]
    
        def detectCycle(node, just_visited) : 
            if node in visited : 
                return True 

            visited.add(node)
            for neighbor in node.neighbors : 
                if neighbor == just_visited : 
                    continue
                if detectCycle(neighbor, node) :
                    return True
            #node.val = node_val  #you visit every node once so backtracking isn't needed?
            return False
        
        return (not detectCycle(node_map[0], None))








        