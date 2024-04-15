# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # node: Represents the current node being traversed.path_sum: Represents the cumulative sum along the path from the root to the current node
        def dfs(node, path_sum):
            if not node:
                return 0
            # his line updates the path_sum by appending the current node's value to it. It multiplies the existing path_sum by 10 to shift its digits to the left and then adds the value of the current node.
            path_sum = path_sum * 10 + node.val
            # if not node.left and not node.right:: This line checks if the current node is a leaf node (i.e., it has no left or right child). If so, it returns the path_sum, as this represents a complete number along the current path.
            if not node.left and not node.right:
                return path_sum
            # This line recursively calculates the sum of numbers from the left and right subtrees. It calls the dfs function for the left and right children of the current node, passing the updated path_sum. It then returns the sum of the results from both recursive calls.
            return dfs(node.left, path_sum) + dfs(node.right, path_sum)

        return dfs(root, 0) 
        
