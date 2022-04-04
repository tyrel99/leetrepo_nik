# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
            
        N = len(arr)
        ind = N-k+1
        if ind != k:
            arr[ind-1], arr[k-1] = arr[k-1], arr[ind-1]
            
        dummy = curr = ListNode(0)
        for i in arr:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next
            
        
       
        