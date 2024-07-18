# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0

    def helper(self, root, distance):
        if root is None:
            return [0]
        
        # Leaf node
        if root.left is None and root.right is None:
            return [1]
        
        left = self.helper(root.left, distance)
        right = self.helper(root.right, distance)
        
        # Processing
        for x in left:
            for y in right:
                if x > 0 and y > 0 and x + y <= distance:
                    self.count += 1

        ans = []
        for x in left:
            if 0 < x < distance:
                ans.append(x + 1)
        for x in right:
            if 0 < x < distance:
                ans.append(x + 1)
        
        return ans

    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.helper(root, distance)
        return self.count
