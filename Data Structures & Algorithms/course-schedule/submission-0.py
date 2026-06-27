"""
Test/edge cases : 
(1) no classes
(2) one class
(3) a small, normal chain of classes
(4) a small cycle with a lone class with 
no prereqs or classes requiring it

"""

"""
Toplogical sort: 

    Create Node class that has a .class_number and .neighbors attribute 

    initialize incoming edge mp and classes mp :
        for i in range(num_courses) :
            initialize node with val i
            inEdge_map[node] = 0
            classes_map[node.val] = node
    create edges : 
        for edge in prerequisites :
            node2 = classes[edge[0]]
            node1 = classes[edge[1]]   #find second node in classes map
            inEdge_map[node2] += 1
            node1.neighbors += node2
        
    for i in range(num_courses) : 
        #if node with value i has no incoming edges (is a root)
        if inEdge_map[i] == 0 : 
            enqueue classes[i] (the root node) to process

    while queue : 
        to_process = queue.pop()
        mp.remove(to_process)
        for neighbor in to_process.neighbors :
            inEdge_map[neighbor] -= 1
            if inEdge_map[neighbor] == 0 :
                enqueue neighbor

    # if the queue is empty and the map has elements, there's a cycle
    if inEdge_map : 
        return false
    return True
"""
class Node :
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inEdge_mp = {}
        classes_mp = {}
        queue = deque()

        for i in range(numCourses) :
            node = Node(i, [])
            inEdge_mp[node] = 0
            classes_mp[i] = node

        for edge in prerequisites :
            node1 = classes_mp[edge[1]]
            node2 = classes_mp[edge[0]]
            inEdge_mp[node2] += 1
            node1.neighbors += [node2]

        for i in range(numCourses) :
            if inEdge_mp[classes_mp[i]] == 0 :
                queue.append(classes_mp[i])
        
        while queue : 
            to_process = queue.popleft()
            del inEdge_mp[to_process]
            for neighbor in to_process.neighbors :
                inEdge_mp[neighbor] -= 1
                if inEdge_mp[neighbor] == 0:
                    queue.append(neighbor)
                
        if inEdge_mp :
            return False
        return True






         