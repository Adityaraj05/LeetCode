# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:

        # This line defines a function called dfs. The function takes two arguments: root and current_string. The root argument is a reference to the root node of a binary tree, and the current_string argument is a string that will be used to accumulate the characters visited during the depth-first search.
        def dfs (root, CurrentString):
            # checks if the root argument is None. If it is, the function returns an empty string (""). This is the base case of the recursion.
            if not root:
                return
  
            # This line constructs a string CurrentString by appending a character to it. The character is determined by adding the ASCII value of the character 'a' to the value of the current node root.val. This means if root.val is 0, the character will be 'a', if root.val is 1, the character will be 'b', and so on. The newly constructed character is appended to the beginning of CurrentString.
            CurrentString = chr(ord('a') + root.val) + CurrentString

            # This line checks if the current node root has both left and right children.
            if root.left and root.right:
                #  If they do, the function calls itself recursively on both children. The left child is explored by calling dfs(root.left, current_string), and the right child is explored by calling dfs(root.right, current_string). The min function is then used to return the lexicographically smallest string returned by the two recursive calls.
                return min(dfs(root.left, CurrentString), dfs(root.right, CurrentString))
            

            # This line checks if only the right child of the root node exists. If it does, the function calls itself recursively on the right child (dfs(root.right, current_string)) and returns the result.
            if root.right:
                return dfs(root.right, CurrentString)
            # This line checks if only the left child of the root node exists. If it does, the function calls itself recursively on the left child (dfs(left.root, current_string)) and returns the result. There seems to be a typo here, as it should be dfs(root.left, current_string).
            if root.left:
                return dfs(root.left, CurrentString)
            # This line is reached only if the node is a leaf node (i.e., it has no children). In this case, the function simply returns the current_string argument.
            return CurrentString
        # dfs function recursively with the root node of the binary tree and an empty string as the initial current_string. This starts the depth-first search traversal of the binary tree.
        return dfs(root, "")
