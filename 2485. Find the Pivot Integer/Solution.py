# Approach -1 

class Solution:
    def pivotInteger(self, n: int) -> int:
        numbers=[]
        for i in range(1,n+1):
            numbers.append(i)
        for p in range(n//2,n):
            pb = sum(numbers[:p+1])
            pa = sum(numbers[p:])
            if pb == pa:
                return p +1
        return -1


        

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Approach -2 (better approach)

class Solution:
    def pivotInteger(self, n: int) -> int:
        # firstly we calculating total sum of n till 1 t on 
        total_sum = n*(n+1)//2
        # taking one variable called sum
        sum = 0
        # calculating the sum one by one --> 1,2,3,4 then sum = 0 + 1=1, 1+2=3,  and compare each time in if block
        for i in range(1+n+1):
            sum += i
            # comparing sum = total + i //2 basic math formula
            if  2*sum == total_sum + i:
                # if got the then return the index element
                return i
        return -1
