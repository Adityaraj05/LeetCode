class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        my_list = []
        for i, n in enumerate(nums): #[0: 991,1: 338,2: 38]
            mapped_n = 0
            base  = 1
            if  n == 0:
                mapped_n = mapping[n]
            while n >0:  # 991 ; 99 ; 9
                digit = n % 10  # 1 ; 1 ; 9
                n  = n // 10    # 99 ; 9 ; 0
                mapped_n += base * mapping[digit] # 0 + 1*9 = 9 ; 9 + 10*6 = 69 ; 69 + 100*6 = 669
                base *= 10 #10 ; 100 ; 1000

            my_list.append((mapped_n, i)) # [(669, 0), (7, 1), (7, 2)]
        my_list.sort() #[(7, 1), (7, 2), (669, 0)]
        return [nums[p[1]] for p in my_list]
    
        
