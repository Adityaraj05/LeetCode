# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # a new ListNode object named dummy is created with a value of 0 and its next pointer pointing to the original head of the linked list.
        dummy = ListNode(0, head)
        # wo pointers prev and curr are initialized to dummy and head, respectively.
        prev, curr = dummy, head
        #  iterates as long as both curr and curr.next are not None. This loop will continue until curr reaches the last node or the second to last node of the linked list.
        while curr and curr.next:
            #  line retrieves the node that comes after the next node of curr. It stores a reference to the next pair of nodes that will be swapped.
            nextPair = curr.next.next
            # stores a reference to the node that comes immediately after curr. This will be the second node in the pair that will be swapped.
            second = curr.next
            # the next pointer of second is updated to point to curr, effectively reversing the direction of the edge between the two nodes.
            second.next = curr
            # the next pointer of curr to point to the node that comes after the next pair of nodes. This effectively moves curr forward in the linked list.
            curr.next = nextPair
            # next pointer of the node pointed to by prev to point to second. This connects the previous part of the linked list to the swapped pair of nodes.
            prev.next = second
            #  update the prev and curr pointers for the next iteration of the loop. prev is moved forward to curr, and curr is moved forward to nextPair.
            prev = curr
            curr = nextPair
        return dummy.next

        
        
