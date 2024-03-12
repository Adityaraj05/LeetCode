class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # A dummy node is created and its next node is set to the head of the original linked list
        dummy = ListNode(0)
        dummy.next = head
        # prefix_sum is initialized to 0, which will keep track of the running sum of node values.
        prefix_sum = 0
        # prefix_sums is initialized as a dictionary with a single entry {0:dummy}.
        prefix_sums = {0: dummy}
        # current pointer is pointing to head 
        current = head
        # The code iterates through the linked list.
        while current:
            # .At each node, it updates prefix_sum by adding the value of the current node.
            prefix_sum += current.val
            # It checks if prefix_sum exists in the prefix_sums dictionary.
            if prefix_sum in prefix_sums:
            # If prefix_sum already exists in prefix_sums, it implies that there's a subsequence of nodes whose values sum up to zero. In this case, it iterates from the node stored in prefix_sums[prefix_sum].next to the current node. It removes those nodes from prefix_sums and updates the next pointers accordingly to remove them from the linked list.
                to_delete = prefix_sums[prefix_sum].next
                temp_sum = prefix_sum + to_delete.val
                while to_delete != current:
                    del prefix_sums[temp_sum]
                    to_delete = to_delete.next
                    temp_sum += to_delete.val
                prefix_sums[prefix_sum].next = current.next
            else:
                prefix_sums[prefix_sum] = current
            current = current.next
        # Finally, it moves the current pointer to the next node and repeats the process until the end of the list is reached.


        return dummy.next
