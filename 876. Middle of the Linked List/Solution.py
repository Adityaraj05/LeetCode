# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # we will solve this porblem with the help of two pointer approach 
        slow, fast = head, head #fast pointer move 2x faster than slow pointer
        # Now we will traverse through while loop if linkedlist is empty or not with the help of fast pointer 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
