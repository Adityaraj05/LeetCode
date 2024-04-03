class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 is greater than the length of the second string s2. If it is, it returns False, implying that the two strings cannot be anagrams because s1 is longer.
        if len(s1)>len(s2):
            return False
        # dic1 and dic2, each containing 26 zeros. These lists are intended to represent counts of occurrences for each lowercase letter in the English alphabet (a-z). dic1 will hold the counts for characters in the first string s1, and dic2 will hold the counts for characters in the second string s2.
        dic1, dic2 = [0]*26 , [0]*26
        # These lines iterate over each character in the first string s1 and the second string s2 simultaneously. For each character, it calculates its position in the alphabet (by subtracting the ASCII value of 'a' from the ASCII value of the character) and increments the corresponding count in dic1 and dic2.
        for i in range(len(s1)):
            dic1[ord(s1[i]) - ord('a')] += 1
            dic2[ord(s2[i]) - ord('a')] += 1
        # This block iterates over each index in the lists dic1 and dic2 (representing each letter of the alphabet). It increments matches by 1 if the counts at the same index in both dic1 and dic2 are equal. matches will ultimately represent the number of letters that have equal counts in both strings.
        matches = 0
        for i in range(26):
            matches += (1 if dic1[i] == dic2[i] else 0)
        # This loop starts from the index len(s1) up to the end of s2. It's basically a sliding window technique where it checks if the number of matches (letters with equal counts in both strings) is equal to 26, meaning that all letters have been matched. If so, it returns True, indicating that s2 contains an anagram of s1.
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True
            # These lines update the counts in dic2 for the character at the right pointer r. If the count becomes equal in both dic1 and dic2, matches is incremented. If dic2's count exceeds dic1's count by one, it means an extra occurrence of a character from s2 is added, and matches is decremented.
            index = ord(s2[r]) - ord('a')
            dic2[index] += 1
            if dic1[index] == dic2[index]:
                matches += 1
            elif dic1[index] + 1 == dic2[index]:
                matches -= 1
            # These lines update the counts in dic2 for the character at the left pointer l as it moves forward. Similar to the previous block, it checks if the counts become equal or differ by one and updates matches accordingly. Then, it increments l to move the left pointer forward.
            index = ord(s2[l]) - ord('a')
            dic2[index] -= 1
            if dic1[index] == dic2[index]:
                matches += 1
            elif dic1[index] - 1 == dic2[index]:
                matches -= 1
            l += 1
            #  the function returns True if matches is equal to 26, meaning that all letters in s1 have been matched in s2, thus s2 is an anagram of s1. Otherwise, it returns False.
        return matches == 26
