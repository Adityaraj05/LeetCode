# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # function named add that takes four parameters: root (the root of the binary tree), val (the value to be inserted), depth (the target depth at which to insert the new nodes), and curr (the current depth while traversing the tree).
        def add(root, val, depth, curr):
            #  if the current node root is None. If it is, it means we've reached a leaf node, and hence we return None.
            if not root:
                return None
            #  if the current depth curr is equal to depth - 1, indicating that we've reached the depth just before the target depth.
            if curr == depth - 1:
                #  left and right children of the current node root in leftTemp and rightTemp, respectively. This is done to preserve the existing subtree structure before adding new nodes.
                leftTemp = root.left
                rightTemp = root.right
                # These lines create new nodes with the value val and assign them as the left and right children of the current node root, effectively adding new nodes at the target depth.
                root.left = TreeNode(val)
                root.right = TreeNode(val)
                #  reconnect the existing left and right subtrees (leftTemp and rightTemp) to the newly added nodes. This ensures that the existing structure is preserved while adding new nodes at the target depth.
                root.left.left = leftTemp
                root.right.right = rightTemp
            
                return root
            # recursively call the add function to add the new nodes at the target depth depth while traversing the left and right subtrees of the current node root. The curr + 1 parameter indicates that the depth of the next level is incremented by 1.
            root.left = add(root.left, val, depth, curr + 1)
            root.right = add(root.right, val, depth, curr + 1)
            
            return root
        # This block of code checks if the target depth is 1. If it is, it creates a new root node with the value val, with the original root as its left child. This effectively inserts a new root at the top of the tree.
        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot
        # If the target depth is not 1, it calls the add function to add new nodes at the specified depth. The function is called with the original root, the value to be inserted, the target depth, and a starting depth of 1.
        return add(root, val, depth, 1)
