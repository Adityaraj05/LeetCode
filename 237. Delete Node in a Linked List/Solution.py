# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # node will given , and after the next node we have to delete so simpliy do this and it is mentiod that after deletion of node the next node will not be null  :-
        node.val, node.next=node.next.val, node.next.next
        
