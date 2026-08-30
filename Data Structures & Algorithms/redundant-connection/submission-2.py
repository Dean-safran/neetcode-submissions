class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(node) :
            if parent[node] == node :
                return parent[node]
            else : 
                parent[node] = find(parent[node])
                return parent[node]
        
        def union(root1, root2) :
            if rank[root1] > rank[root2] :
                parent[root2] = root1
                if rank[root2] + 1 > rank[root1] :
                    rank[root1] += rank[root2]
            else : 
                parent[root1] = root2
                if rank[root1] + 1 > rank[root2] :
                    rank[root2] += rank[root1]

        parent = dict()
        rank = dict()
        for i in range(1, len(edges)+1) : 
            parent[i] = i 
            rank[i] = 1
        
        for u, v in edges : 
            root1 = find(u)
            root2 = find(v)
            if root1 == root2 :
                return [u,v]
            else : 
                union(root1, root2)
            




        

