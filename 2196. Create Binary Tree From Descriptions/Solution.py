# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {} # Hashmap
        children = set() # beacuse children node can be multiple so we will not every time create it if it already exist .
        for par, child , is_left in descriptions:
            children.add(child)  #{15, 17, 20, 80, 19}
            if par not in nodes:
                nodes[par] = TreeNode(par) # {20, 50, 80}
            if child not in nodes:
                nodes[child] = TreeNode(child) #{15, 17, 20, 80 ,19}

            if is_left:
                nodes[par].left = nodes[child]
            else:
                nodes[par].right = nodes[child]

        
        # Here we are finding the root node , and we will able to find the root node by looking into children set, root node is the one that is not a child of any other node.
        
        for parent, child, left in descriptions:
            if parent not in children:
                return nodes[parent]

            


