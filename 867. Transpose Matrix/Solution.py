class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        # range(cols): This generates a sequence of numbers from 0 to cols-1 (excluding cols). This represents the number of columns in the result.for _ in range(cols): The underscore (_) is often used as a throwaway variable in such constructs. It indicates that we're not interested in the loop counter variable itself, but only in iterating the specified number of times (determined by range(cols)).
[0]*rows: Inside the loop, this creates a list of rows zeros. This will be repeated for each column, building up the rows of the result.
        result = [[0]*rows for _ in range(cols)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result[j][i] = matrix[i][j]
        return result
             
        -------------------------------------------------------------------------------------------------------------------------------------

Example:-
Original Matrix (matrix):

[[1, 2, 3],
 [4, 5, 6]]
Step-by-step breakdown:

Dimensions:

rows = len(matrix) = 2 (2 rows)
cols = len(matrix[0]) = 3 (3 columns)
result creation:

result = [[0, 0, 0], [0, 0, 0]] (a 2x3 list filled with zeros)
Transposition loop:

Outer loop (i):
i = 0:
Inner loop (j):
j = 0: result[0][0] = matrix[0][0] (becomes 1)
j = 1: result[1][0] = matrix[0][1] (becomes 2)
j = 2: result[2][0] = matrix[0][2] (becomes 3)
i = 1:
Inner loop (j):
j = 0: result[0][1] = matrix[1][0] (becomes 4)
j = 1: result[1][1] = matrix[1][1] (becomes 5)
j = 2: result[2][1] = matrix[1][2] (becomes 6)
Return value:

After the loops complete, result becomes:
[[1, 4],
 [2, 5],
 [3, 6]]
