class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """

        use topological sort 

        """

        incoming_edges = dict()
        for i in range(numCourses) : 
            incoming_edges[i] = 0
        for course, _ in prerequisites :
            incoming_edges[course] += 1

        adj_list = dict()
        for course, prereq in prerequisites :
            if prereq not in adj_list :
                adj_list[prereq] = [course]
            else : 
                adj_list[prereq].append(course)
    

        res = []
        while incoming_edges : 
            to_add = []
            for course in incoming_edges :
                if incoming_edges[course] == 0 :
                    to_add.append(course)
            if incoming_edges and not to_add :
                return []
            for course in to_add :
                if course in adj_list :
                    for next_course in adj_list[course] :
                        incoming_edges[next_course] -= 1
                res.append(course)
                del incoming_edges[course]
        return res
            