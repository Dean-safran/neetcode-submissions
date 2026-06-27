# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head.next == None : 
            return False
        
        fastPointer = head
        pointer = head

        while fastPointer : 
            pointer = pointer.next
            fastPointer = fastPointer.next.next
            if pointer == fastPointer : 
                return True
        return False
        