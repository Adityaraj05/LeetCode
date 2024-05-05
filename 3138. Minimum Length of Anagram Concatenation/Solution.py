class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        # frequency = Counter(s) will give Counter({'a': 2, 'b': 2}), which means 'a' occurs 2 times, 'b' occurs 2 times in the string.
        frequency = Counter(s)
        for i in range(1, n+1):
            # Inside the loop, if n % i == 0: checks if n is divisible by i without remainder, meaning i is a potential length for the substring.
            if n % i == 0:
                # For each character frequency freq, this expression checks if the frequency is divisible by n // i without leaving a remainder.
                # n // i represents the length of the substring we're currently testing. If the frequency of a character is evenly divisible by the length of the substring, it means that character can be evenly distributed into the substring.

                # This iterates over the character frequencies of the string, which are [2, 2]
                if all((freq % (n // i) == 0) for freq in frequency.values()):
                    # If the conditions in the inner if statement are met, it returns i, which is the length of the smallest substring where characters have equal frequency.all([True, True]) checks if all elements are True
                    return i
        # If no such substring is found, it returns n as the default length, which means the whole string s itself satisfies the condition.
        return n
        
