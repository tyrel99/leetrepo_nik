# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        temp = []
        while curr:
            temp.append(curr.val)
            curr = curr.next
        temp.sort()
         
        dummy = curr = ListNode(0)
        for v in temp:
            curr.next = ListNode(v)
            curr = curr.next
            
        return dummy.next
            
            
        