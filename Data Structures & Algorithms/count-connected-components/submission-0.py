"""

First approach :
time: o(e) to call union on all edges, we keep track of 
number of components as we go

space: o(v) for parent and size array backing UnionFind class
----------------
We use/implement a UnionFind class

We should start with an integer attribute for the class 
that's equal to n for n components, we then union all of 
the nodes that have edges between them, subtracting one 
from self.components for each union. We return self.components 
at the end
"""


class UnionFind : 
    def __init__(self, n) : 
        self.comps = n
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, node) :
        if self.parent[node] != node :
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
        self.comps -= 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        unionFind = UnionFind(n)
        for u,v in edges : 
            unionFind.union(u,v)
        return unionFind.comps
            




        