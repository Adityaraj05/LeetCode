class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # This line initializes an empty dictionary named cache. This dictionary is intended to store the results of previously computed function calls to avoid redundant computations.
        cache = {}
        # This line defines a function named helpher that takes two arguments, r and k.
        def helpher (r, k):
            # This line checks if the value of k is equal to the length of a variable key. This condition checks if we have traversed the entire key string.
            if k == len(key):
                return 0
                # This line checks if the tuple (r, k) is present in the cache dictionary. If it is, it means that the result for this combination of r and k has been computed before and stored in the cache
            if (r, k) in cache:
                # If the result for the combination (r, k) is found in the cache, it is returned directly. This avoids redundant computation and improves performance.
                return cache[(r, k)]
            # This line initializes the variable result with positive infinity. This value will be used to store the minimum distance found in subsequent iterations.
            result = float("inf")
            # This line iterates over the characters in the ring string, along with their corresponding indices. The enumerate() function provides both the index (i) and the character (c) for each iteration.
            for i, c in enumerate(ring):
                # This line checks if the current character c in the ring string matches the character at index k in the key string. If there's a match, it means we have found a potential match for the next character in the key.
                if c == key[k]:
                    # This line calculates the minimum distance to move from the current index r to the index i in the ring string. It considers both clockwise and counterclockwise distances by taking the minimum of the absolute difference between r and i, and the length of the ring string minus that difference.
                    mid_dist = min(abs(r-i),len(ring)-abs(r-i))
                    # This line calculates the minimum distance to complete the remaining characters of the key string, starting from the index k+1, recursively calling the helpher function. It adds 1 to mid_dist to account for moving from the current character to the next character in the ring.
                    result = min(result,mid_dist+1+ helpher(i, k+1))
            # his line stores the computed result for the combination (r, k) in the cache dictionary to avoid redundant computation in future calls.
            cache[(r, k)] = result
            # returns the computed result for the current combination of r and k back to the caller of the function.
            return result
            # calling the helpher function with ring and key at 0 indeces
        return helpher (0, 0)
