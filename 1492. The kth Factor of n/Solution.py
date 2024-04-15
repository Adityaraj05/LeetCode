class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # This line initializes two empty lists, bigfactor and smallfactor.
        bigfactor, smallfactor = [] , []
        # This line starts a loop that iterates through numbers from 1 to the square root of n (inclusive), using the range function. It uses math.sqrt() to calculate the square root of n and then adds 1 to ensure that the loop includes the integer square root of n.
        for num in range(1, int(math.sqrt(n)+1)):
            # This line checks if n is divisible by num with no remainder, indicating that num is a factor of n.
            if n % num == 0:
                # This line checks if num is equal to the integer division of n by num, which indicates that num is the square root of n and thus n is a perfect square.
                if num == n //num:   #checking for perfect square
                # If num is a factor of n and it's the square root (i.e., n is a perfect square), num is added to the smallfactor list.
                    smallfactor.append(num)
                else:
                    # If num is a factor of n but not the square root, this block appends the smaller factor to smallfactor and the larger factor to bigfactor.
                    smallfactor.append(min(num, n // num))
                    bigfactor.append(max(num, n // num))
        # This line reverses the order of elements in the bigfactor list.
        
        all_factor = smallfactor + bigfactor

        if len(all_factor) >= k:
            # If there are at least k factors of n, this line returns the kth factor from the all_factor list (note that list indices start from 0, hence the k-1).
            return all_factor[k-1]  # k-1 beacure index of list will start at 0 and k will start at 1 that's why
        return -1
    
