class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pairs(s, a, b, points):
            stack = []
            local_points = 0
            for char in s:
                if char == b and stack and stack[-1] == a:
                    stack.pop()
                    local_points += points
                else:
                    stack.append(char)
            return ''.join(stack), local_points
        
        max_point = 0
        if x > y:
            s, points = remove_pairs(s, 'a', 'b', x)
            max_point += points
            s, points = remove_pairs(s, 'b', 'a', y)
            max_point += points
        else:
            s, points = remove_pairs(s, 'b', 'a', y)
            max_point += points
            s, points = remove_pairs(s, 'a', 'b', x)
            max_point += points

        return max_point

