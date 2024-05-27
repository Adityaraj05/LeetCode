class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        Hashmap = defaultdict(int)  #[a =0, b =0, c=0]
        for word in words:  #[abc, aabc,bc]
            for count in word: 
                Hashmap[count] +=1  #[a = 3, b=3, c=3]

        for character in Hashmap:
            if Hashmap[character] % len(words):   #here 0 mean flase and anynumber will be consider to be true
                return False
        return True


        
