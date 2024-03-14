# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # firstly we are going to check that is tree is empty or not
        if(root.left == None and root.right == None):
            return [root.val]
        # making a recursive function 
        def duplicates(root):
            # here we are checking that if root.val is already present mean key in the dict., if not then add it to the dictionary --> {1:1}
            if(root.val not in count):
                count[root.val] = 1  # add it to the dictionary 
            # if vlaue mean(key) is already present then increase it frequency by 1
            else:
                count[root.val] +=1
            # now we are checking root.left is None or not if not none then again function call 
            if (root.left != None):
                duplicates(root.left)
            # same we are checking root.right is None or not if not none then again function call 
            if (root.right != None):
                duplicates(root.right)
        # we have created an empty dictionary which will store key -- value :- key refer to node and value refer to frequency
        count ={}
        duplicates(root)
        result=[]
        maximum = max(count.values())   # {1:1,2:2} therefore count.values will be get {1,2} and mam of both is 2 the maximum will be 2
        for key, val in count.items():   # now in key -- val pair it will check 
            if (val == maximum):         # if 1 == 2 not then check further 2 == 2 then yes then append in the list.
                result.append(key)
        return result


        
