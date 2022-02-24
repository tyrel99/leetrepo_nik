# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def midPoint(self):
            slow, fast = head, head
            
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
                
            mid = slow.next
            slow.next = None
            return mid
        
        def mergesort(self,left,right):
            dummy= curr = ListNode(0)
            
            while left and right:
                if left.val < right.val:
                    curr.next = left
                    curr = curr.next
                    left = left.next
                else:
                    curr.next = right
                    curr = curr.next
                    right = right.next
            
            curr.next = left or right
            return dummy.next
        if not head or not head.next: return head
        mid = midPoint(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return mergesort(self,left,right)
        