class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findPath(self, node: Optional[TreeNode], target: int, path: list) -> bool:
        if node is None:
            return False

        if node.val == target:
            return True

        path.append('L')
        if self.findPath(node.left, target, path):
            return True
        path.pop()

        path.append('R')
        if self.findPath(node.right, target, path):
            return True
        path.pop()

        return False

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        rootToSrc = []
        rootToDest = []

        self.findPath(root, startValue, rootToSrc)
        self.findPath(root, destValue, rootToDest)

        # Find the first divergence point
        i = 0
        while i < len(rootToSrc) and i < len(rootToDest) and rootToSrc[i] == rootToDest[i]:
            i += 1

        # Steps to move up from the startValue to the common ancestor
        result = ['U'] * (len(rootToSrc) - i)
        
        # Steps to move down from the common ancestor to the destValue
        result.extend(rootToDest[i:])

        return ''.join(result)
