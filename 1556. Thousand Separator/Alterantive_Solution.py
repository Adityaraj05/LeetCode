class Solution:
    def thousandSeparator(self, n: int) -> str:
        string = str(n)
        l = len(string)
        if l < 4 :
            return string
        result = ""
        string = string[::-1]
        for i in range(l) :
            if not i % 3 and i != 0 :
                result += "."
            result += string[i]
        return result[::-1]
