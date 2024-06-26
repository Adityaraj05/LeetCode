# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.sortedArr = []
        self.inorderTraverse(root)
        return self.sortedArrayToBST(0, len(self.sortedArr) - 1)

    def inorderTraverse(self, root: TreeNode) -> None:
        # Checks if the current node root is None.
        if not root:
            return
        #  Recursively calls inorderTraverse on the left subtree.
        self.inorderTraverse(root.left)
        # Adds the current node root to self.sortedArr.
        self.sortedArr.append(root)
        # Recursively calls inorderTraverse on the right subtree.
        self.inorderTraverse(root.right)

    def sortedArrayToBST(self, start: int, end: int) -> TreeNode:
        #  Checks if the start index is greater than the end index.
        if start > end:
            return None
        mid = (start + end) // 2
        #  Sets root to be the middle element of the current subarray.
        root = self.sortedArr[mid]
        # Recursively constructs the left subtree from the left subarray.
        root.left = self.sortedArrayToBST(start, mid - 1)
        #  Recursively constructs the right subtree from the right subarray.
        root.right = self.sortedArrayToBST(mid + 1, end)
        return root
