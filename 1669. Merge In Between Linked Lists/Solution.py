# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # This line initializes a variable current to point to the head of list1. This variable will be used to traverse list1.
        current = list1
        # This line initializes a variable index to 0. It will be used to keep track of the current position while traversing the linked list.
        index = 0
        # This initiates a while loop that continues until the index is less than a-1. This loop is used to traverse list1 until just before the position a.
        while index < a-1:
            # Inside the loop, current is updated to point to the next node in list1.
            current = current.next
            # This line increments the index by 1 after each iteration of the loop.
            index +=1
        # After exiting the loop, this line sets head to the current node, which is the node just before the position a in list1.
        head = current

        # This initiates another while loop that continues until the index is less than or equal to b. This loop is used to traverse list1 until position b.
        while index <= b:
            # Inside the loop, current is updated to point to the next node in list1.
            current = current.next
            # This line increments the index by 1 after each iteration of the loop.
            index +=1
        # After exiting the loop, this line sets the next pointer of the node at position a-1 to point to the head of list2, effectively inserting list2 into list1.
        head.next = list2
        
        # This initiates a while loop that continues until the next pointer of list2 becomes None. This loop is used to traverse list2 to find its last node.
        while list2.next:
            # Inside the loop, list2 is updated to point to the next node in list2.
            list2=list2.next
        # After exiting the loop, this line sets the next pointer of the last node of list2 to point to current, which is the node at position b in list1.
        list2.next = current
        return list1

        
