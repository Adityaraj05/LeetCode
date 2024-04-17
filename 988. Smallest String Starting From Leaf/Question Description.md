988. Smallest String Starting From Leaf


You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller.

For example, "ab" is lexicographically smaller than "aba".
A leaf of a node is a node that has no children.

 

Example 1:


![image](https://github.com/Adityaraj05/LeetCode/assets/118068294/1cdc26e0-8688-447c-a7b2-867af435f362)


Input: root = [0,1,2,3,4,3,4]
Output: "dba"


Example 2:


![image](https://github.com/Adityaraj05/LeetCode/assets/118068294/2eda34f4-5fc4-4206-b897-bf12d49b75d5)



Input: root = [25,1,3,1,3,0,2]
Output: "adz"


Example 3:


![image](https://github.com/Adityaraj05/LeetCode/assets/118068294/17ecd06f-ecef-410c-95e3-ebd957303308)




Input: root = [2,2,1,null,1,0,null,0]
Output: "abc"
 

Constraints:

The number of nodes in the tree is in the range [1, 8500].
0 <= Node.val <= 25
