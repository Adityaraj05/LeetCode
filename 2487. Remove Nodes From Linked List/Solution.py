# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # checking the linkedlist is empty or not
        if not head:
            return head
        # setting self.maxValue to -infinity
        self.maxValue = float("-inf")

        # Using the recursive function we are going at the end of the linkedlist 
        def traverse(node):
            # if only one node present simply return that node as a answer
            if not node:
                return node
            # if node are present then traverse till the end using recursive call
            node.next = traverse(node.next)

            # we reach to the last node of the linkedlist now we are storing maxvalue( -∞ , 8 )
            self.maxValue = max(self.maxValue, node.val)
            # if self.maxValue > node.val (8>8) false then return node.next which will be 13 else return node (current node)
            if self.maxValue > node.val:
                return node.next  
            return node  #8, 13
        # at last we are returning node(13->8)
        return traverse(head)
