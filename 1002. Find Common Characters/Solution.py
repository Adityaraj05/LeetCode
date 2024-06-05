class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # count will be a Counter dictionary that holds the count of each character in the first word "bella":({'b': 1, 'e': 1, 'l': 2, 'a': 1}) ; after first loop iterate {'b': 1, 'e': 1, 'l': 2, 'a': 1} ; {'b': 0, 'e': 1, 'l': 2, 'a': 0}
        count = Counter(words[0])


        for word in words: # loop will start with first word but if we do the intersection with same word then there will no change .
            Hashmap = Counter(word) #({'l': 2, 'a': 1, 'b': 1, 'e': 1}); ({'r': 2, 'o': 1, 'l': 2, 'e': 1}); 
            # Compare the counts of each character in count with those in Hashmap, and keep the minimum count for each character.
            for char in count: 
                count[char] = min(count[char], Hashmap[char])   # No changes, as counts match
        result = []

        for key in count: #{'b': 0, 'e': 1, 'l': 2, 'a': 0}
            for i in range(count[key]): # b-> 0 ; e->1 ; l=>2 and for a=>0
                result.append(key) # ['e', 'l', 'l']
        return result
        
