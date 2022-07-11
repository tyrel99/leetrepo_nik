# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = dummy = ListNode(0,head)
        slow = head
        fast = head 
        while n > 0:
            fast = fast.next
            n -= 1
            
        
        while fast != None:
            prev = slow
            slow = slow.next
            fast = fast.next
        
        print(prev.val)
        prev.next = slow.next
        
        while prev != None:
            
            prev = prev.next
        
        return dummy.next
            
        
            
        
        