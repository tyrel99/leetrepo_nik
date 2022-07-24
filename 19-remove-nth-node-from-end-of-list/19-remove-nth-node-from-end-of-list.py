# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast= head
        while n > 0:
            fast = fast.next
            n -= 1
        
        while fast:
            slow = slow.next
            fast = fast.next
            
        prev = dummy = ListNode(0,head)
        
        while prev.next != slow:
            prev = prev.next
        prev.next = slow.next
        
        return dummy.next
            
            
        