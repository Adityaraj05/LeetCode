# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def function(node):
            if node is None:
                return True
            if node.left is None and node.right is None:
                if node.val == 0:
                    return False
                else:
                    return True
            if node.val == 2:
                return function(node.left) or function(node.right)
            else:
                # node.val == 3:
                return function(node.left) and function(node.right)
        return function(root)
        
