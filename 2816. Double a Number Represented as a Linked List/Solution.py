# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If head is None, the method simply returns head as is, because there's nothing to modify.
        if head is None:
            return head
        # assigns the value of head (the first node) to a variable named cur. It's a pointer or reference that will be used to iterate through the linked list.
        cur = head
        #  initializes a variable named prev to None. It will be used to keep track of the previous node as cur iterates.
        prev = None
        # This while loop iterates through the linked list as long as cur is not None
        while cur is not None:
            #  calculates the doubled value of the current node's data (cur.val).
            new_val = cur.val * 2
            # If the doubled value is less than 10, it's simply assigned directly to cur.val, effectively doubling the value in-place.
            if new_val < 10:
                cur.val = new_val
            #  If the doubled value is 10 or greater
            else:
                # The remainder (%) after dividing by 10 is assigned to cur.val. This captures the digit in the ones place, essentially representing the units digit of the doubled value.
                cur.val = new_val % 10
                # hecks if it's the first node in the list (prev is None).
                if prev is None:
                    # If it's the first node, a new ListNode object with a value of 1 (representing the carry digit) is created and assigned to new_node.
                    new_node = ListNode(1)
                    # head of the list is updated to point to the new node, effectively creating a new head node to accommodate the carry.
                    head = new_node
                    # next pointer of the new head node is set to point to the original first node (cur).
                    head.next = cur
                # If it's not the first node
                else:
                    #  The value of the previous node (prev.val) is incremented by 1 to carry over the tens digit of the doubled value.
                    prev.val += 1
            # moving the pointer cur assign to prev and cur pointing to cur.next
            prev = cur
            cur = cur.next
        # at last returning the head of the linkedlist
        return head
        
