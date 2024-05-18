# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        #  If the current node root is None (i.e., it doesn't exist), the function returns 0, indicating that there are no steps from this point.
        def CountSteps(root):
            if root is None:
                return 0
            # Recursively calculates the number of steps needed to reach the left subtree from the current node.
            leftSteps=CountSteps(root.left)
            # Recursively calculates the number of steps needed to reach the right subtree from the current node.
            rightSteps=CountSteps(root.right)
            self.moves += abs(leftSteps) + abs(rightSteps)
            return leftSteps + rightSteps + root.val - 1
        CountSteps(root)
        return self.moves
        
