# we can leverage the Trie (prefix tree) data structure. A Trie allows us to efficiently store the dictionary and perform prefix searches. Here's how you can use a Trie to solve this problem:

# Build a Trie: Insert all the dictionary words into the Trie.
# Search for Prefixes: For each word in the sentence, search for the shortest prefix in the Trie.
# This approach ensures efficient prefix search, leading to an optimal solution.

# Why This Approach is Optimal:
# 1. Efficient Insertions and Searches: Building and querying the Trie are both efficient operations, making this approach suitable for large dictionaries and sentences.
# 2. Minimal Prefix Checks: The Trie structure ensures that we stop as soon as we find the shortest prefix, avoiding unnecessary checks.
# 3 .Clean and Readable Code: The separation of Trie construction and word replacement logic makes the code easier to understand and maintain.




class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search_shortest_prefix(self, word):
        node = self.root
        prefix = ""
        for char in word:
            if char not in node.children:
                break
            node = node.children[char]
            prefix += char
            if node.is_end_of_word:
                return prefix
        return word

class Solution:
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        
        words = sentence.split()
        for i in range(len(words)):
            words[i] = trie.search_shortest_prefix(words[i])
        
        return ' '.join(words)

# Example usage
sol = Solution()
dictionary = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
print(sol.replaceWords(dictionary, sentence))
# Output: "the cat was rat by the bat"
