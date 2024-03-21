# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # In this line, two variables prev and curr are initialized. prev is set to None, indicating that initially, there's no previous node. curr is set to the head of the linked list, indicating the current node that we're processing.
        prev, curr = None, head
        # This line starts a while loop that continues until curr becomes None. Since curr represents the current node being processed, when it becomes None, it means we've reached the end of the linked list and there are no more nodes to process.
        while curr:
            # Here, we store the next node of the current node curr in the variable nxt. This step is important because when we modify the curr.next pointer in the next line, we'll lose access to the next node if we don't store it beforehand.
            temp = curr.next
            # This line is where the actual reversal happens. We set the next pointer of the current node curr to point to the prev node. This effectively reverses the direction of the pointer of curr, making it point to the previous node.
            curr.next = prev
            # After reversing the pointer of curr, we need to move prev and curr pointers one step forward for the next iteration. Here, we set prev to the current node curr, preparing it to become the previous node for the next iteration.
            prev = curr
            # Finally, we update curr to point to the next node, which we stored earlier in the variable temp. This step progresses the traversal of the linked list to the next node for the next iteration of the loop.
            curr = temp
            # Once the loop finishes, prev will be pointing to the last node of the original linked list, which is now the head of the reversed list. So, we return prev, which is the new head of the reversed linked list.
        return prev
