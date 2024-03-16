class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # zero and one are initialized to 0. These variables are used to keep track of the count of zeros and ones encountered so far in the nums list.
        zero, one = 0,0
        # result is initialized to 0. This variable will store the maximum length of contiguous subarray with equal number of zeros and ones.
        result = 0
        # HashMap is initialized as an empty dictionary. This dictionary will be used to store the difference between the count of ones and zeros encountered so far in the nums list.
        HashMap = {}
         # This is a loop that iterates through the elements of the nums list along with their indices using the enumerate function.
        for i, n in enumerate(nums):
        # Inside the loop, if the current element (n) is 0, increment the zero counter; otherwise, increment the one counter.
            if n==0:
                zero +=1
            else:
                one +=1
            # Check if the difference between the count of ones and zeros encountered so far (one - zero) is not already present in the HashMap. If not, store this difference along with its corresponding index (i) in the HashMap.
            if one - zero not in HashMap:
                HashMap[one-zero] = i
            # If the count of ones is equal to the count of zeros encountered so far (one == zero), update the result to the sum of one and zero. This is done to handle the case where the entire subarray from the beginning up to the current index has equal number of ones and zeros.
            if one == zero:
                result = one + zero
            # If the counts of ones and zeros are not equal, it means there's a subarray with equal numbers of ones and zeros in between the current index and the index stored in the HashMap for the corresponding difference. Calculate the length of this subarray (i - index) and update result to the maximum of its current value and this length.
            else:
                index = HashMap[one-zero]
                result = max(result, i-index)
        return result
