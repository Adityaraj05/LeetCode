2816. Double a Number Represented as a Linked List

You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

Return the head of the linked list after doubling it.

 

Example 1:


![image](https://github.com/Adityaraj05/LeetCode/assets/118068294/bd7c124a-4dc9-4faf-8273-43fbe863bbbd)


Input: head = [1,8,9]
Output: [3,7,8]
Explanation: The figure above corresponds to the given linked list which represents the number 189. Hence, the returned linked list represents the number 189 * 2 = 378.
Example 2:


![image](https://github.com/Adityaraj05/LeetCode/assets/118068294/699a9ef4-fa9a-4afb-ae86-ea9c2943f8cc)


Input: head = [9,9,9]
Output: [1,9,9,8]
Explanation: The figure above corresponds to the given linked list which represents the number 999. Hence, the returned linked list reprersents the number 999 * 2 = 1998. 
 

Constraints:

The number of nodes in the list is in the range [1, 104]
0 <= Node.val <= 9
The input is generated such that the list represents a number that does not have leading zeros, except the number 0 itself.
