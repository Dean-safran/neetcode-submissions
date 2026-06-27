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

        pointer1 = list1
        pointer2 = list2
        result = ListNode()
        pointer3 = result

        while pointer1 or pointer2 :
            if not pointer1 : 
                while pointer2 : 
                    pointer3.next = pointer2
                    pointer2 = pointer2.next
                    pointer3 = pointer3.next
                return result.next
            elif not pointer2 : 
                while pointer1 : 
                    pointer3.next = pointer1
                    pointer1 = pointer1.next
                    pointer3 = pointer3.next
                return result.next
            elif pointer1.val < pointer2.val : 
                pointer3.next = pointer1 
                pointer1 = pointer1.next
                pointer3 = pointer3.next 
            elif pointer2.val < pointer1.val : 
                pointer3.next = pointer2 
                pointer2 = pointer2.next
                pointer3 = pointer3.next 
            elif pointer1.val == pointer2.val : 
                pointer3.next = pointer1 
                pointer1 = pointer1.next
                pointer3 = pointer3.next 
        return result.next



       
            
    
        


        
