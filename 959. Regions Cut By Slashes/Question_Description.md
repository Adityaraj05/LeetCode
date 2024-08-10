959. Regions Cut By Slashes

An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.

Given the grid grid represented as a string array, return the number of regions.

Note that backslash characters are escaped, so a '\' is represented as '\\'.

 

Example 1:
![image](https://github.com/user-attachments/assets/f566c898-b7fb-47d5-a467-609ccce12cec)


Input: grid = [" /","/ "]
Output: 2
Example 2:
![image](https://github.com/user-attachments/assets/3ccc0ef5-51aa-4e85-899f-5210b6379f65)


Input: grid = [" /","  "]
Output: 1
Example 3:
![image](https://github.com/user-attachments/assets/a71a5b4b-a465-4dbd-b61a-9694e695ab67)


Input: grid = ["/\\","\\/"]
Output: 5
Explanation: Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.
 

Constraints:

n == grid.length == grid[i].length
1 <= n <= 30
grid[i][j] is either '/', '\', or ' '.
