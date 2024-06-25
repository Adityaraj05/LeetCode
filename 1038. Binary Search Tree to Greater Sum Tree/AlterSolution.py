# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # Declare a global variable
        curSum = 0
        
        def dfs(node):
            # The nonlocal keyword is used to indicate that curSum in the dfs function refers to the curSum variable declared in the nearest enclosing scope, which is the bstToGst method.This allows the dfs function to modify the curSum variable declared in the bstToGst method, ensuring that the cumulative sum is correctly maintained and updated across recursive calls.
            nonlocal curSum
            if not node:
                return
            
            dfs(node.right)  # Traverse the right subtree
            curSum += node.val  # Update the sum with the current node's value
            node.val = curSum   # Update the current node's value to the sum
            dfs(node.left)   # Traverse the left subtree

        dfs(root)
        return root
