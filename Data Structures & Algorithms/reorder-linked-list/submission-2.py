# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import math 

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

       # find len of linked list by iterating 
       # with counter o(n)

       # create list1 by setting the ceiling(n // 2)
       # node.next = None, but right before create 
       # pointer of the node.next for the head of 
       # list2    o(n)

       # reverse list2 o(n)

       # recurse until i == ceiling(n // 2) :
       # create temp for first.next
       # connect first to second
       # increment first by setting first equal to temp
       # create temp for second.next
       # connect second to first
       # increment second by setting second equal to temp   o(n)

    #    4 o(n) operations total to o(n) runtime with o(1) space
    #    since the original list is being manipulated with 
    #    constant pointers

        pointer = head
        lenOfList = 0
        while pointer : 
            lenOfList += 1
            pointer = pointer.next

        if lenOfList < 3 : 
            return
        
        #finding split point
        mid = head
        for i in range(math.ceil(lenOfList / 2) - 1): 
            mid = mid.next
        #splitting
        head2 = mid.next
        mid.next = None

        #reversing second list
        prev = None
        while head2 : 
            next = head2.next
            head2.next = prev
            prev = head2
            head2 = next
        

        pointer1 = head
        pointer2 = prev
        for i in range(lenOfList // 2) :      
            temp1 = pointer1.next
            temp2 = pointer2.next
            pointer1.next = pointer2
            pointer2.next = temp1
            pointer1 = temp1
            pointer2 = temp2
        if temp2 : 
            temp2.next = None
        return


            
            
    

    