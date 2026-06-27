# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# time is o(n) because we scan through the array and do constant 
# pointer and .next attribute operations
# pointers are o(1) space 

class Solution:
     def reverseList(self, head):
        if head == None or head.next == None : 
            return head
        
        
        pointer1 = head
        pointer2 = head.next
        
        if pointer2.next == None : 
            pointer1.next = None
            pointer2.next = pointer1
            return pointer2
        
        pointer3 = head.next.next
    
        while pointer3 :
            if pointer1 == head : 
                pointer1.next = None
            pointer2.next = pointer1
            pointer1 = pointer2
            pointer2 = pointer3
            if not pointer3.next :
                pointer2.next = pointer1
                return pointer3
            else : 
                pointer3 = pointer3.next
        


        
        

        