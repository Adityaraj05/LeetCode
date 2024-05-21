# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # we are creating a dummy two  linked list node one : left and right and these will serve as the heads of two separate linked lists.
        left, right = ListNode(), ListNode()
        # nitializes two variables, left_tail and right_tail, and sets them equal to the heads of the respective linked lists (left and right). These variables will be used to keep track of the tails (i.e., the last nodes) of the left and right linked lists.
        left_tail, right_tail = left, right

        while head:
            # checks if the value of the current node (head.val) is less than a given threshold value x.
            if head.val < x:
                left_tail.next = head
                left_tail = left_tail.next
            else:
                right_tail.next = head
                right_tail = right_tail.next
            # moves the head pointer to the next node in the original linked list, effectively advancing the iteration to the next node.
            head = head.next
        #  this line sets the next attribute of the last node in the right list (which is currently pointing to the last node of the original list) to None. 
        right_tail.next = None
        # sets the next attribute of the last node in the left list to the head of the right list, effectively appending the right list to the end of the left list.
        left_tail.next = right.next
        # returns the head of the left list, which now contains all the nodes less than x followed by all the nodes greater than or equal to x.
        return left.next

        


        
