class Solution(object):
    def wonderfulSubstrings(self, word):
        #  initializes a list named count with 1024 elements, all initialized to 0. This list is used to store the count of XOR values encountered during the loop
        count = [0] * 1024  
        # initializes a variable named result to 0. This variable is used to accumulate the final result.
        result = 0
        # initializes a variable named prefix_xor to 0. This variable is used to keep track of the cumulative XOR value as we iterate through the characters of the word.
        prefix_xor = 0
        # This line sets the count of the initial XOR value (which is 0) to 1. This is done because initially, there is one occurrence of XOR value 0.
        count[prefix_xor] = 1
        # tarts a loop that iterates over each character in the variable word.
        for char in word:
            # alculates the index of the character in the alphabet. For example, if char is 'a', char_index will be 0; if char is 'b', char_index will be 1, and so on.
            char_index = ord(char) - ord('a')
            # This line updates the prefix_xor variable by performing a bitwise XOR operation with the value obtained by shifting 1 to the left by char_index positions. This effectively toggles the bit corresponding to the character in the alphabet.
            prefix_xor ^= 1 << char_index
            # ncrements the result variable by the count of occurrences of the current prefix_xor value stored in the count list.
            result += count[prefix_xor]
            for i in range(10):
                # This line increments the result variable by the count of occurrences of the XOR value obtained by toggling the ith bit of prefix_xor.
                result += count[prefix_xor ^ (1 << i)]
                #  This line increments the count of occurrences of the current prefix_xor value stored in the count list.
            count[prefix_xor] += 1
        
        return result
