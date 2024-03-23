143. Reorder List

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:

![image](https://github.com/Adityaraj05/LeetCode/assets/118068294/e964b5b5-dbc3-4162-b0de-e6b954c55a02)


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:

![image](https://github.com/Adityaraj05/LeetCode/assets/118068294/2e5157c9-c048-47e6-9e98-a2b282ff0edb)


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
