class UnionFind : 
    def __init__(self, n) :
        self.parent = list(range(n))
        self.size = [1] * n


    def find(self, node) :
        if self.parent[node] != node :
            #compress as we traverse up the component
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2) :
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 == root2 :
            return 
        if self.size[root1] >= self.size[root2] :
            self.parent[root2] = root1
            self.size[root1] = self.size[root1] + self.size[root2]
        else : 
            self.parent[root1] = root2
            self.size[root2] = self.size[root1] + self.size[root2]

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1 :
            return False
        unionFind = UnionFind(n)
        for u,v in edges :
            #if two nodes are a part of the same component, there's a cycle
            if unionFind.find(u) == unionFind.find(v) : 
                return False
            unionFind.union(u,v)
        return True

            
        




#DFS VERSION 
# VVVVVVVVV

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
"""







        