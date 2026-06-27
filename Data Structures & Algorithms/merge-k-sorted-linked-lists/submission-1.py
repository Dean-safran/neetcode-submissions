# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # call on two sides of list, breaking up problem 
        # until you reach base case of 1 or 2 lists, then 
        # merge up 
        
        if len(lists) == 0 : 
            return None
        l = 0
        r = len(lists) - 1
        return self.split(l, r, lists)

        
    def split(self, l, r, lists) :
        if r - l == 0 : 
            return lists[l]

        mid = l + ((r-l) // 2)
        left = self.split(l, mid, lists)
        right = self.split(mid + 1, r, lists)
        return self.merge(left, right)

       

    def merge(self, list1, list2) : 
        result = ListNode()
        pointer = result
        
        while list1 and list2 : 
            if list1.val < list2.val : 
                pointer.next = list1
                list1 = list1.next
            else : 
                pointer.next = list2
                list2 = list2.next
            pointer = pointer.next
        
        pointer.next = list1 or list2
        return result.next
        
        
        
        
        
        
        
        
        
        #todo : implement heap approach
        # heap = []
        # for i in range(len(lists)) : 
        #     heapq.heappush(heap, (lists[i].val, i, lists[i] ))
        # result = ListNode()
        # pointer = result
        # while len(heap) != 0 : 
        #     popped = heapq.heappop(heap)
        #     popped_index = popped[1]
            
        #     pointer.next = ListNode(popped[2].val, None)
        #     pointer = pointer.next

        #     if not popped[2].next : 
        #         continue
        #     nextNode = popped[2].next

        #     heapq.heappush(heap, (nextNode.val, popped_index, nextNode))
        # return result.next


             
            

            

        
        
        
        
        
        
        
        
        
        
        
        
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

        