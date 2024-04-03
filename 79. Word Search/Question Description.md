79. Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:

![image](https://github.com/Adityaraj05/LeetCode/assets/118068294/36509577-790e-471b-8e69-0e39da0f63f3)






Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:

![image](https://github.com/Adityaraj05/LeetCode/assets/118068294/f616b4b5-acf5-403c-8260-d9dfb553cd1e)







Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:

![image](https://github.com/Adityaraj05/LeetCode/assets/118068294/2b9b6a5e-86e8-4423-9f52-97ae532d982c)






Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?
