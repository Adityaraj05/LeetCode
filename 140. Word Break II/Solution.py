class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # This line initializes an empty dictionary memo. This dictionary is going to be used for memoization, which means storing the results of previous computations to avoid redundant work in recursive calls.
        memo = {}
        #  aims to break down the input string into words from the provided dictionary.
        def dfs(string):
            #  if the current string is already in the memoization dictionary. If it is, it means that we have already computed the results for this string before, so we return the stored result directly.
            if string in memo:
                #  returns the stored result for that string without further computation.
                return memo[string]
            # If the string is empty, it means we have successfully broken down the input string into valid words. In this case, we return a list containing an empty string as the only element. 
            if not string:
                return [""]
            # This list will be used to store the possible word break combinations for the current string.
            local_result = []
            for word in wordDict:
                #  if the current string starts with the current word from the dictionary. If it does, it means we can potentially use this word as a prefix for the word break.
                if string.startswith(word):
                    # recursively calls the dfs function with the remaining part of the string after removing the current word        
                    sub_words = dfs(string[len(word):])
                    #  iterates over each possible word break combination for the remaining part of the string obtained from the recursive call.
                    for sub_word in sub_words:
                        # constructs a word break combination by concatenating the current word, a space character (if sub_word is not empty), and the sub_word. It then appends this combination to the local_result list.
                        local_result.append(word + (" " if sub_word else "") + sub_word)
            #  stores the computed local_result in the memoization dictionary for the current string. This is done to avoid redundant computations for the same string in future recursive calls.
            memo[string] = local_result
            # returns the local_result, which contains all possible word break combinations for the current string.
            return local_result
        # eturns the result of the DFS algorithm applied to the input string s, which contains all possible word break combinations for the entire input string.
        return dfs(s)
