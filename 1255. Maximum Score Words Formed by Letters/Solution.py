class Solution:
    def maxScoreWords(self, words: List[str], available_letters: List[str], score: List[int]) -> int:
        letter_counts = [0] * 26
        
        for letter in available_letters:
            letter_counts[ord(letter) - ord('a')] += 1
        
        max_score = 0
        num_words = len(words)
        
        for subset in range(1, 1 << num_words):
            word_counts = [0] * 26
            
            for word_index in range(num_words):
                if subset & (1 << word_index):
                    for char_index in range(len(words[word_index])):
                        word_counts[ord(words[word_index][char_index]) - ord('a')] += 1
            
            is_valid_subset = all(word_counts[char_index] <= letter_counts[char_index] for char_index in range(26))
            
            if is_valid_subset:
                total_score = sum(word_counts[char_index] * score[char_index] for char_index in range(26))
                max_score = max(max_score, total_score)
        
        return max_score
