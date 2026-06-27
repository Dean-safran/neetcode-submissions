# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # like merge sort, scan through each list with two pointers, 
        # if one pointer is less than the other choose that pointer 
        # to be added next and increment, if they're equal choose pointer1
        # or something

        # scanning through each list takes o(n) time, where n 
        # is the amount of nodes in both lists total, the pointers take 
        # o(1) space and at each iteration there are constant checks 
        # and comparisons

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
        if list1 : 
            pointer.next = list1
        else : 
            pointer.next = list2          
        return result.next



       
            
    
        


        
