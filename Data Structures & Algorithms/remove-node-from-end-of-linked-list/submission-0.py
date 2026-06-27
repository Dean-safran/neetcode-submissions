# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # a two pass approach would be calculating 
        # the length of the list
        # toIterate = len(list) - n

        # if toIterate == 0 return pointer.next
        # else iterate toIterate - 1 times and remove
        # the nth node from end

        pointer = head
        lenOfList = 0
        while pointer : 
            lenOfList += 1
            pointer = pointer.next
        
        toIterate = lenOfList - n
        if toIterate == 0 : 
            return head.next
        else : 
            pointer = head
            for i in range(toIterate - 1) :
                pointer = pointer.next
            pointer.next = pointer.next.next
            return head

        


