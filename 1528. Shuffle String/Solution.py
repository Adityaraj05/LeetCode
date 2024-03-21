class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # created a empty string 
        ans = ""
        # traversing through for loop till the lenght of the indices
        for i in range(len(indices)):
        #indices.index(i): This part finds the index of the current loop variable i within the list indices. It effectively retrieves the index value from indices corresponding to the current iteration of the loop , s[indices.index(i)]: This part uses the index value obtained above to access the character at that index in the string s. 
            ans+=s[indices.index(i)]
        return ans

