# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)  # Convert list to set for O(1) look-up
        result = []

        def dfs(node):
            if not node:
                return None
            
            # Recurse on the left and right children
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            
            if node.val in to_delete_set:
                # If current node is to be deleted, add its children to result (if they exist)
                if node.left:
                    result.append(node.left)
                if node.right:
                    result.append(node.right)
                # Return None to parent because this node is deleted
                return None
            
            return node

        # hanlding critical part adding root forest as well 

        if root and root.val not in to_delete_set:
            result.append(root)
        
        dfs(root)
        
        return result
