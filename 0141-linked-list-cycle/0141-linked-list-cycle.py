# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head or not head.next:
            return False
        
        firstPoin=head
        secondPoin=head
        
        
        while(secondPoin.next and secondPoin.next.next):
            firstPoin=firstPoin.next
            secondPoin=secondPoin.next.next
            
            if(firstPoin==secondPoin):
                return True
        return False    