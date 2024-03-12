# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # makea recursive function
        def recursive(node):
            # checking the edge cases if node is none mean it has not left and right child the we will return 0
            if node == None:
                return 0
            sum =0
            # if node left is true and if node.left.left is null and node.left.right is null then we will add the node.val into our sum
            if node.left and (node.left.left == None and node.left.right == None):
                sum += node.left.val
            # recursive call  9 + 0 + 15 = 24 
            return sum + recursive(node.left) + recursive(node.right)
        return recursive(root) 
        

   
   
        
        
        
        

        
