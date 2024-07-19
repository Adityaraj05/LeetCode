class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:

        row = len(matrix)
        col = len(matrix[0])
        row_min = set()
        result = []

        for r in range(row):
            row_min.add(min(matrix[r]))

        col_max = set()
        for c in range(col):
            cur_max = matrix[0][c]
            for r in range(row):
                cur_max = max(cur_max, matrix[r][c])
            if cur_max in row_min:
                result.append(cur_max)

        for n in col_max:
            if n in row_min:
                result.append(n)
        return result


