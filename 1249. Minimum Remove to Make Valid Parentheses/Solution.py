class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Initializes an empty list named result which will store processed characters.
        result = []
        #  Initializes a variable count to keep track of the number of open parentheses encountered. It starts at 0.
        count = 0 # it will keep the count of open parenthese "(".
        #  Begins a loop that iterates through each character i in the input string s
        for i in s:
            if i == "(":
                result.append(i)
                count +=1
                #  If i is a closing parenthesis ")" and there are still unmatched open parentheses (i.e., count > 0), this condition is checked.
            elif i ==")" and count > 0:
                result.append(i)
                count -=1
            elif i != ")":   # mean a character then just append in the result list.
                result.append(i)
        # Initializes an empty list named array
        array = []
        # Begins a loop that iterates through each character i in the result list in reverse order.
        for i in result[::-1]:
            # Checks if the current character i is an open parenthesis "(" and if there are still unmatched open parentheses (i.e., count > 0).
            if i =="(" and count >0:
            # If the condition is met, decrements the count variable to indicate that one open parenthesis has been matched.
                count -=1
            else:
                array.append(i)
            #  the function returns a string formed by joining the characters in the array in reverse order. 
        return "".join(array[::-1])
