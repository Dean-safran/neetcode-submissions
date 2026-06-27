# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #todo : implement heap approach
        heap = []
        for i in range(len(lists)) : 
            heapq.heappush(heap, (lists[i].val, i, lists[i] ))
        result = ListNode()
        pointer = result
        while len(heap) != 0 : 
            popped = heapq.heappop(heap)
            popped_index = popped[1]
            
            pointer.next = ListNode(popped[2].val, None)
            pointer = pointer.next
            
            if not popped[2].next : 
                continue
            nextNode = popped[2].next

            heapq.heappush(heap, (nextNode.val, popped_index, nextNode))
        return result.next


             
            

            

        
        
        
        
        
        
        
        
        
        
        
        
        # brute force would be for every node added, 
        # you find the min head in the list of lists
        
        # to optimize a bit, if the min is repeated 
        # multiple times, remove a few heads at once

        # had to lookup using a heap to minimize 
        # min lookups

        # create a heap of tuples in the form of 
        # (head.val, index, node_reference)
        # if two head.vals are mins, then python 
        # in heappop(your_heap) compares the next elements 
        # in the tuple. If you only had node_reference, you 
        # can't compare two listNode objects, i.e. 
        # your code breaks. 

        # the heap is always size k, the amount of heads 
        # in the original list. You extract and insert 
        # N nodes, N being the total amount of nodes. 
        # Time is O(N logk) and space is o(k)

        