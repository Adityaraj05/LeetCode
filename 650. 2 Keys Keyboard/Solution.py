class Solution:
    def minSteps(self, n: int) -> int:
        copy = 0
        paste = 1
        operation = 0

        while paste != n:

            if n % paste == 0:
                copy = paste
                operation += 1

            paste += copy
            operation += 1

        return operation
