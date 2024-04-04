# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # This line defines a function named dfs. It takes two arguments:node: This represents a node in a binary tree. It's likely that the node object has attributes like val (the value stored in the node) and left and right (references to the left and right child nodes, respectively).curSum: This is an integer variable that keeps track of the current cumulative sum as the function traverses the tree.
        def dfs(node, curSum):
            # If the node is None, it means we've reached the end of a branch, and the function returns False
            if not node:
                return False
            # This line adds the value stored in the current node (accessed using node.val) to the curSum variable. This keeps track of the running total as the function recursively explores the tree.
            curSum += node.val
            # This line checks if the current node is a leaf node (i.e., it has no left or right children).
            if not node.left and not node.right:
                # If curSum is equal to targetSum, it means the path from the root to this leaf node has a sum that matches the target sum. In this case, the function returns True to indicate that the target sum has been found.
                return curSum == targetSum
                # The function calls dfs(node.left, curSum) to recursively explore the left subtree, passing the current curSum (including the value of the current node).It also calls dfs(node.right, curSum) to recursively explore the right subtree, again passing the current curSum.The or operator (|) combines the results of the left and right subtree explorations.
            return (dfs(node.left, curSum) or dfs(node.right, curSum))
            # it's outside the function definition, calls the dfs function with the root node of the binary tree and an initial curSum of 0.
        return dfs(root, 0)
        
