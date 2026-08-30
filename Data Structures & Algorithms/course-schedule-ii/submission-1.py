from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """

        use topological sort 

        """

        incoming_edges = dict()
        # O(n) time and space
        for i in range(numCourses) : 
            incoming_edges[i] = 0
        # O(m) time and space
        for course, _ in prerequisites :
            incoming_edges[course] += 1

        # O(m) time and space
        adj_list = dict()
        for course, prereq in prerequisites :
            if prereq not in adj_list :
                adj_list[prereq] = [course]
            else : 
                adj_list[prereq].append(course)
    
        # worst case we process every edge
        # in a graph where all nodes are connected
        # which is O(m) or O(n^2)
        res = []
        q = deque()
        for course in incoming_edges :
                if incoming_edges[course] == 0 :
                    q.append(course)
        while q : 
            curr = q.popleft()
            res.append(curr)
            if curr in adj_list :
                for course in adj_list[curr] :
                    incoming_edges[course] -= 1
                    if incoming_edges[course] == 0 :
                        q.append(course)
            del incoming_edges[curr]
        if incoming_edges :
            return []
        return res
            