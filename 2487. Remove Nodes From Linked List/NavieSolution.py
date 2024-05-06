# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        stack = []
        while cur:
            # checks if the stack is not empty and if the value of the last node in the stack (top of the stack) is less than the value of the current node cur. If true, pop nodes from the stack until the condition is not met.
            while stack and stack[-1].val < cur.val:
                a = stack.pop()
            stack.append(cur)
            cur = cur.next

        # IN stack we left with the [13, 8]

        nxt = None
        while stack:
            cur = stack.pop()
            cur.next = nxt
            nxt = cur

        return cur
