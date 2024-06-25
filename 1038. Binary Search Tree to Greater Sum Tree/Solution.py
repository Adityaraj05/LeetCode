# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        def solve(root, sum):
            if not root:
                return
            # The function first recursively traverses the right subtree. This ensures that the larger values are processed first.
            solve(root.right, sum)  # Traverse the right subtree
            # sum[0] (using a list to allow modification within the nested function) is updated by adding the current node's value. The current node's value is then updated to this new sum.
            sum[0] += root.val      # Update the sum with the current node's value
            root.val = sum[0]       # Update the current node's value to the sum
            # , the function recursively traverses the left subtree, updating the remaining nodes.
            solve(root.left, sum)   # Traverse the left subtree

        sum = [0]
        solve(root, sum)
        return root
