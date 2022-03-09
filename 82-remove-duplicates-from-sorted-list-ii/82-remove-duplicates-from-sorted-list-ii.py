# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        curr = head
        dummy = prev = ListNode(0,curr)
        
       
        
        while curr:
            if curr.next and curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next
                
            
            elif prev.next:
                
                prev.next = curr
                prev = prev.next
                
                
                
            
            curr = curr.next
        return dummy.next
        