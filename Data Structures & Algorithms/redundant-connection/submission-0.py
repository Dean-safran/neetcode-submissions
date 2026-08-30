class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def DFS(curr_node, parent) : 
            if curr_node in visited : 
                return True
            visited.add(curr_node)
            for v in adj_list[curr_node] :
                if v == parent : 
                    continue
                elif DFS(v, curr_node) :
                    return True
            return False

        adj_list = dict()
        for i in range(0, len(edges)) :
            u, v = edges[i]
            if u > v :
                temp = v
                v = u
                u = temp
            if u not in adj_list :
                adj_list[u] = [v]
            else : 
                adj_list[u].append(v)
            if v not in adj_list :
                adj_list[v] = [u]
            else : 
                adj_list[v].append(u)
            visited = set()
            possible_edge = DFS(u, None)
            if possible_edge :
                return [u,v]


        

