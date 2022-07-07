# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        n = len(arr)  
        
        kgroups = []
        for i in range(0,n,k):
            temp = arr[i : i+k]
            
            if len(temp) == k:
                kgroups += (temp[::-1])
            else:
                kgroups += (temp)
        
        dummy = temp = ListNode(0)
        for k in kgroups:
            temp.next = ListNode(k)
            temp = temp.next
        print(dummy.next)
        return dummy.next
            
                             
           
        
        