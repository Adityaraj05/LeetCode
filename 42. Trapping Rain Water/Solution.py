class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <1:
            return 0
        ans = 0
        leftmax = [0] * n
        rightmax = [0] * n
        # i am initializing first leftmax index val to height of the building first val 
        leftmax[0] = height[0]
        # starting the loop from index 1
        for i in range(1,n):
            leftmax[i] = max(leftmax[i-1], height[i])
        #  i am initializing last rightmax index val to height of the building last index val 
        rightmax[-1] = height[-1]
        # here loop will start form second last index to 0
        for i in range(n-2,-1,-1):
            rightmax[i] = max(rightmax[i+1],height[i])


        for i in range(n):
            ans += min(leftmax[i], rightmax[i])-height[i] 
        return ans
        
