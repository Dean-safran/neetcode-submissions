class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        time complexity -> 0(v + e * log(v))
            we add v if there are no edges or there
            are more nodes than edges

        space complexity -> O(nodes)

        """
        
        # because of flattening and ranking, 
        # this is an o(log n) operation
        def find(node) :
            if parent[node] == node :
                return parent[node]
            else : 
                parent[node] = find(parent[node])
                return parent[node]
        
        # in order to increase ranking 
        # by 1 you'd have to double the amount of nodes
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
            




        

