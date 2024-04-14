class Solution:
    def toHex(self, num: int) -> str:
        result = []
        # This dictionary maps integer values 10 to 15 to their corresponding hexadecimal characters. This is used later to convert decimal numbers 10 to 15 to their hexadecimal representations 'a' to 'f'.
        HashMap = {10:"a",11:"b",12:"c",13:"d",14:"e",15:"f"}
        if num ==0:
            return "0"
            # If the input number num is negative, this code adds 2^32 (which is equivalent to shifting a 32-bit integer to the left by 32 bits, effectively wrapping around negative numbers in a 32-bit system) to make it positive
        if num <0:
            num +=2**32
            # This loop iterates until num becomes zero. Within each iteration, it calculates the remainder of num divided by 16, which gives the least significant hexadecimal digit. Then, it updates num to remove this least significant digit by performing integer division by 16.
        while num >0:
            digit = num % 16
            num //= 16
            # If the remainder (digit) is greater than 9 (i.e., it represents a value from 10 to 15), it replaces digit with its corresponding hexadecimal character from the HashMap. Otherwise, it converts digit to a string.
            if digit > 9 and digit <16:
                digit = HashMap[digit]
            else:
                # The resulting digit (either a string representing a digit from 0 to 9 or a letter representing a digit from 10 to 15) is then appended to the result list.
                digit = str(digit)
            result.append(digit)
            #  this line joins the elements of the result list together into a single string, effectively reversing the order of the hexadecimal digits because they were appended to the list in reverse order. The reversed order is necessary because the algorithm processes the hexadecimal digits from the least significant to the most significant, but the resulting string needs to display the digits from most significant to least significant.
        return "".join(result[::-1])
        
