# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # creating a dummy node with val = 0 and next.node pointing to head of the original linkedlist
        dummy = ListNode(0, head)
        # taken two variable leftPrev which is currently pointing dummy node and curr pointing to head node
        leftPrev, curr = dummy, head
        for i in range(left-1):
            leftPrev, curr = curr, curr.next
        # Now curr = "left" , leftPrev = "node before left"
        # here we are reversing from left to right
        prev = None
        for i in range(right-left+1):
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
        # update pointer
        leftPrev.next.next = curr  # current is node after "right"
        leftPrev.next = prev # prev is right
        return dummy.next


        
