class Solution:
    def nthUglyNumber(self, n: int) -> int:
        l = [1]
        p2, p3, p5 = 0, 0, 0
    
        for i in range(1, n):
			# get the next number
            next_num = min(2*l[p2], min(3*l[p3], 5*l[p5]))
            l.append(next_num)
			# increase pointer for which the number matches [see above explanation]
            if next_num == 2 * l[p2]:
                p2 += 1
            if next_num == 3 * l[p3]:
                p3 += 1
            if next_num == 5 * l[p5]:
                p5 += 1

        return l[n-1]
