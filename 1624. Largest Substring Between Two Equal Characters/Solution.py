class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # char -> first index
        Hashmap = {}
        result = -1

        for index, char in enumerate(s): #[index-->char] ex- (0 - a); (1->b);(2->c);(3->a)
            if char in Hashmap:
                # current index - Hashmap[char] (first time indxe) -1
                result = max(result, index - Hashmap[char]-1) 
            else:
                Hashmap[char] = index  #[a->index]



        return result

        
