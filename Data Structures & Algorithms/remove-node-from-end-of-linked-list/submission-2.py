# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if you remove the first from the end the window 
        # is length 1, second from the end the window 
        # is length 2, etc

        # if window is length 1 we scan through entire 
        # array so runtime is o(n), using pointers is 
        # o(1) space

        dummy = ListNode()
        dummy.next = head
        slow = fast = dummy
        for i in range(n) : 
            fast = fast.next
        while fast.next : 
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next


        
        
        
        
        
        
        
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

        


