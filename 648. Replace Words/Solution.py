class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """

        # Convert the list dictionary into a set s. Sets provide O(1) average-time complexity for membership tests, making it faster to check if a prefix exists in the dictionary.
        s = set(dictionary)
        # split() divides the sentence at each space, resulting in a list of words.
        words = sentence.split()  #["the", "cattle", "was", "rattled", "by", "the", "battery"].
        ans = []
        
        # : Iterate over each word in the list words.
        for word in words:
            # temp as an empty string to build prefixes and found as a boolean flag to indicate if a prefix is found.
            temp = ""
            found = False
            #  Iterate over each character in the current word.This nested loop builds prefixes one character at a time.
            for char in word:
                # Append the current character char to temp, gradually building the prefix. Example: If word is "cattle", temp becomes "c", then "ca", and so on.
                temp += char
                # Check if the current temp (prefix) exists in the set s (dictionary)
                if temp in s:
                    #  If temp is found in the set s, Append temp to the ans list. Set the found flag to True.Break out of the inner loop as the shortest prefix is found.
                    ans.append(temp)
                    found = True
                    break
            #  if no prefix was found (found is False
            if not found:
                # Append the original word to the ans list.
                ans.append(word)
        # Join the list ans into a single string with spaces between the words and return it. join() combines all elements in ans into a single string with spaces separating each element.
        return ' '.join(ans)
