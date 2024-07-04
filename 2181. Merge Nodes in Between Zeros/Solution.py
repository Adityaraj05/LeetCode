# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        CurrentNode = head
        # dummy and temp are initialized to new ListNode objects with value 0. dummy is used to keep track of the head of the new list, while temp is used to build the new list.
        temp = dummy = ListNode(0)
        # loop iterates through the original list until it reaches the end.
        while CurrentNode.next:
            # initialized as a new ListNode with value 0. This node will accumulate the sum of consecutive nodes.
            node = ListNode(0)
            # loop iterates through the nodes of the original list, summing their values into node.val until it encounters a node with value 0.
            while CurrentNode.next.val !=0:
                # Adds the value of the current node to node.val.
                node.val += CurrentNode.next.val
                # Moves to the next node in the list.
                CurrentNode = CurrentNode.next
            # Once a 0 is encountered, node (which now contains the sum of values) is added to the new list.
            #  Links the new node to the list being built.
            temp.next = node
            #  Moves temp to the last node added, preparing for the next sum.
            temp = temp.next
            # After encountering a node with value 0, the loop skips this node to start summing from the next sequence of nodes.
            CurrentNode = CurrentNode.next
        return dummy.next

        
