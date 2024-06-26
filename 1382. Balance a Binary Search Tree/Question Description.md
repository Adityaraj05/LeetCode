1382. Balance a Binary Search Tree

1383. Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

 

Example 1:

![image](https://github.com/Adityaraj05/LeetCode/assets/118068294/c546cdb9-8c56-4cad-9c4b-88e5828ec304)


Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
Example 2:

![image](https://github.com/Adityaraj05/LeetCode/assets/118068294/3cd9dc77-0ae1-4f45-a6e0-61b23ef8a5c3)


Input: root = [2,1,3]
Output: [2,1,3]
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 105
