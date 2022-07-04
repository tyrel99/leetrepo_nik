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
            
        kgroup = []
        for i in range(0,len(arr),k):
            temp = arr[i:i+k]
            if len(temp) == k:
                kgroup += temp[::-1]        
            else:
                kgroup += temp
                
        res = ListNode(0)
        temp = res
        
        for i in kgroup:
            temp.next = ListNode(i)
            temp = temp.next
        
        return res.next
                
        
            
      
       
            
        
    
        