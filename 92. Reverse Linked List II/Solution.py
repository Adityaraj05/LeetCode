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

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# README FILE:-

dummy = ListNode(0, head): This line creates a dummy node with a value of 0 and its next node pointing to the head of the original linked list. This dummy node serves as a placeholder and helps handle cases where the reversal needs to start from the very beginning of the linked list.

leftPrev, curr = dummy, head: This line initializes two pointers, leftPrev and curr. leftPrev initially points to the dummy node, and curr points to the head of the linked list. These pointers will be used to keep track of the nodes before and at the left position respectively.

for i in range(left-1):: This loop advances the leftPrev and curr pointers to reach the node before the left position in the linked list.

prev = None: This line initializes the prev pointer, which will be used to keep track of the previous node during the reversal process.

for i in range(right-left+1):: This loop iterates over the nodes that need to be reversed, from left to right, both inclusive.

temp = curr.next: This line stores the reference to the next node of curr in a temporary variable temp to prevent loss of reference during the reversal.

curr.next = prev: This line reverses the direction of the next pointer of the curr node, making it point to the previous node (prev). This effectively reverses the direction of the pointer for the current node.

prev, curr = curr, temp: This line updates the prev pointer to the current node (curr) and advances the curr pointer to the next node (temp) in preparation for the next iteration.

leftPrev.next.next = curr: This line updates the next pointer of the node before the left position (leftPrev) to point to the node after the right position (curr). This reconnects the linked list after the reversal.

leftPrev.next = prev: This line updates the next pointer of the node before the left position (leftPrev) to point to the node at the right position (prev). This effectively connects the left position to the right position after the reversal.

return dummy.next: This line returns the next node of the dummy node, which effectively returns the head of the modified linked list after the reversal.

Overall, this code performs an in-place reversal of a portion of the linked list specified by the left and right indices.###
        
