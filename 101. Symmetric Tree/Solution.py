# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            # Recursively check the left subtree of the left node with the right subtree of the right node and the right subtree of the left node with the left subtree of the right node.
            return left.val == right.val and check(left.left, right.right) and check(left.right, right.left)

        if not root:
            return True
        return check(root.left, root.right)
