class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # initialize a emtpy string
        result = ""
        # initialize a counter method which will store the element in the keys- value pair
        frequency = Counter(s)
        # traversing through loop to order string char is present in the frequency or not
        for char in order:  #c b a
            if char in frequency: # ("abcd")a -> 1, b->1, c->1, d->1(c in frequency yes then append in the result string with its frequency count)
                result +=  char * frequency[char]   # c * 1= c   , b *1=b, a*1=a  --->"cba"
                # after adding to the result string we have to pop the string from the frequency dictionary
                frequency.pop(char)
        if frequency:  #dictionary in not empty
            for char in frequency: #d
                result += char * frequency[char] # "cbad"
        return result
