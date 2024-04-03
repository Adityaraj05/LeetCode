class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # This line calculates the number of rows and columns in the board 2D array. len(board) gives the number of rows, and len(board[0]) gives the number of columns by assuming that all rows have the same length.
            rows, cols = len(board), len(board[0])
            # This line initializes an empty set called path. This set will be used to keep track of visited cells during the DFS (Depth First Search) traversal.
            path = set()
            # These parameters represent the current position in the board (i and j) and the current character index in the word being searched.

            def dfs(i, j, currChar):
                # checks if we have traversed the entire word. If the currChar is equal to the length of the word, it means we have found the word on the board, and thus, the function returns True.
                if currChar == len(word):
                    return True
                #  It checks if the current position is within the boundaries of the board (i < 0 or j < 0 or i >= rows or j >= cols), if the character in the board matches the expected character in the word (word[currChar] != board[i][j]), and if the current cell has already been visited ((i, j) in path). If any of these conditions are met, the function returns False.
                if i < 0 or j < 0 or i >= rows or j >= cols or word[currChar] != board[i][j] or (i, j) in path:
                    return False
                # This line adds the current cell (i, j) to the path set, indicating that it has been visited.
                path.add((i, j))
                # This line recursively calls the dfs function for the adjacent cells (up, down, left, right) and checks if any of those calls return True. It does this by trying each direction and combining the results using logical OR (or operator).
                result = (dfs(i + 1, j, currChar + 1) or dfs(i - 1, j, currChar + 1) or dfs(i, j + 1, currChar + 1) or dfs(i, j - 1, currChar + 1))
                # This line removes the current cell (i, j) from the path set after exploring all possible paths from it.
                path.remove((i, j))
                return result
            # This loop iterates over each cell in the board and calls the dfs function to search for the word starting from that cell. If dfs returns True, it means the word is found starting from that cell, and the function returns True.
            for i in range(rows):
                for j in range(cols):
                    if dfs(i, j, 0):
                        return True
            return False
