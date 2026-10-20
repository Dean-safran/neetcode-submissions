# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b) :
            if b == 0 :
                return a
            return gcd(b, a % b)
        
        curr = head 
        while curr.next != None :
            new_val = gcd(curr.val, curr.next.val)
            new_node = ListNode(new_val, curr.next)
            curr.next = new_node
            curr = curr.next.next
        return head