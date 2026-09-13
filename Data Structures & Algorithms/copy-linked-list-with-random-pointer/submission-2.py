"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """

        step through original list in order to instantiate all nodes

        to copy random pointers -> 
            for the current node being processed, 
            keep curr_copy and original_curr's random node in a vars

            step through both lists at same time, 
            if original_curr is original_random_node, set
            copy_node_to_be_processed.random = curr.copy

        """
        if not head :
            return None

        random_node = dict()
        node_randIdx = dict()
        i_nodeCopy = dict()

        head_copy = Node(0)
        curr_copy = head_copy
        curr = head

        # make copy_list and random_node dict
        while curr :
            curr_copy.val = curr.val
            if curr.next :
                curr_copy.next = Node(0)

            if curr.random :
                if curr.random not in random_node :
                    random_node[curr.random] = [curr]
                else :
                    random_node[curr.random].append(curr)

            curr = curr.next
            curr_copy = curr_copy.next
        
        # make node_randIdx dict
        rand_curr = head
        i = 0
        while rand_curr :
            if rand_curr in random_node :
                for curr in random_node[rand_curr] :
                    node_randIdx[curr] = i
            rand_curr = rand_curr.next
            i += 1

        # create i_nodeCopy map
        curr_copy = head_copy
        i = 0
        while curr_copy :
            i_nodeCopy[i] = curr_copy
            curr_copy = curr_copy.next
            i += 1


        curr = head
        curr_copy = head_copy

        while curr :
            if curr.random is None :
                curr = curr.next
                curr_copy = curr_copy.next
                continue
            else : 
                curr_copy.random = i_nodeCopy[node_randIdx[curr]]

                # after random node found
                # move on to next element
                curr = curr.next
                curr_copy = curr_copy.next
        return head_copy





