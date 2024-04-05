class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # Hashset will be used to store previously encountered substrings.Sets are unordered collections of unique elements.resultset will store the final set of unique 10-character substrings.
        Hashset, resultset = set(), set()
        #  creates a sequence of numbers from 0 (inclusive) to len(s) - 10 (exclusive).This ensures that the loop doesn't go out of bounds when creating substrings.The variable left will take on each index value in this range during each iteration.
        for left in range(len(s)-9):
            # The length of the substring will always be 10 characters.
            current= s[left:left+10]
            # This line checks if the current substring (current) is already present in the Hashset.
            if current in Hashset:
                # then we add in resulset we found repeated substring
                resultset.add(current)
                # If the current substring (current) is not found in Hashset (i.e., it's unique so far):
            else:
                Hashset.add(current)
        return list(resultset)

        
