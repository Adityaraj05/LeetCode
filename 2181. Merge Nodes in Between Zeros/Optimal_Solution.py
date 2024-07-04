# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        originalHead = head
        current = head.next
        sum = 0

        while current is not None:
            if current.val == 0:
                head.val = sum
                sum = 0
                if current.next is not None:
                    head = head.next
            else:
                sum += current.val
            
            current = current.next

        head.next = None
        return originalHead







      
        


        
