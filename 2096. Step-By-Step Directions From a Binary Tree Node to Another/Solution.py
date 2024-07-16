

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], src: int, dest: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.val == src or root.val == dest:
            return root

        left = self.lowestCommonAncestor(root.left, src, dest)
        right = self.lowestCommonAncestor(root.right, src, dest)

        if left is not None and right is not None:
            return root

        return left if left is not None else right

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
        LCA = self.lowestCommonAncestor(root, startValue, destValue)

        lcaToStart = []
        lcaToDest = []

        self.findPath(LCA, startValue, lcaToStart)
        self.findPath(LCA, destValue, lcaToDest)

        result = ['U'] * len(lcaToStart) + lcaToDest

        return ''.join(result)
