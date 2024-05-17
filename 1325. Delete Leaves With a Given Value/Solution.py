# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# I have use here post order traversal in this problem to solve.
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # checks if the current node is None. If it is, it means we've reached the end of the tree or a leaf node, so the function returns without doing anything.
        def helper(node):
            if node == None:
                return 
            # recursively call the helper function on the left and right children of the current node
            node.left = helper(node.left)
            node.right = helper(node.right)
            # checks if the current node is a leaf node (i.e., it has no left or right children) and if its value (node.val) matches the target value. If both conditions are met, it returns None, effectively removing this node from the tree.
            if node.left == None and node.right == None and node.val == target:
                return None
            #  If the current node is not a leaf node or does not match the target value, it returns the node unchanged.
            return node
        return helper(root) 





