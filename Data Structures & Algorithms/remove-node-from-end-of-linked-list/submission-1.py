# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #if you remove the first from the end the window 
        # is length 1, etc

        pointer1 = head
        pointer2 = head
        for i in range(n-1) : 
            pointer2 = pointer2.next
        prev = None
        while pointer2.next : 
            prev = pointer1 
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        if not prev : 
            return head.next
        else : 
            prev.next = prev.next.next
            return head


        
        
        
        
        
        
        
        # two pass : o(n) time to scan through for length
        #            o(n) time to find node to start removal from
        #            o(1) space for pointers            
        # a two pass approach would be calculating 
        # the length of the list
        # toIterate = len(list) - n

        # if toIterate == 0 return pointer.next
        # else iterate toIterate - 1 times and remove
        # the nth node from end

        # pointer = head
        # lenOfList = 0
        # while pointer : 
        #     lenOfList += 1
        #     pointer = pointer.next
        
        # toIterate = lenOfList - n
        # if toIterate == 0 : 
        #     return head.next
        # else : 
        #     pointer = head
        #     for i in range(toIterate - 1) :
        #         pointer = pointer.next
        #     pointer.next = pointer.next.next
        #     return head

        


