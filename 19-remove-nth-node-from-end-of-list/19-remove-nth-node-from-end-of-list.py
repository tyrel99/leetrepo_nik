# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        
        while head:
            arr.append(head.val)
            head = head.next
            
        i = len(arr)
        
        while n > 0:
            i -= 1
            n -= 1
        del(arr[i])
        
        dummy = curr = ListNode(0)
        
        for i in arr:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next
        
        
            
            
            
            
        