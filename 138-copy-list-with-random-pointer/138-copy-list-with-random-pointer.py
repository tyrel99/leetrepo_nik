"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        hashh = defaultdict(int)
        dummy = temp = Node(0)
        
        while curr:
            temp.next = Node(curr.val)
            hashh[curr] = temp.next
            curr, temp = curr.next, temp.next
            
        curr = head 
        temp = dummy.next
        
        while curr:
            temp.random = hashh[curr.random] if curr.random else None
            curr, temp = curr.next, temp.next
        return dummy.next
        