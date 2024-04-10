class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # This line initializes an empty dictionary called count. This dictionary will be used to store the frequency of each unique element in the nums list.
        count = {}
        # Each inner list in IndexFrequency will hold elements based on their frequency. The index of the outer list represents the frequency of the elements it contains. for example at index 2 means the element have frequency of two will be store at index 2 and so on..
        IndexFrequency = [[] for i in range(len(nums)+1)]

        for i in nums:
            # for i in nums:: This iterates over each element i in the list nums.count[i] = ...: This assigns a value to a key i in the dictionary count.1 + count.get(i, 0): This part calculates the count for the current element i:count.get(i, 0): The get method of the dictionary checks if a key i exists in count.If i exists, get returns the corresponding value (the current count for i).If i doesn't exist, get returns the default value 0.1 + ...: We add 1 to the retrieved count (or 0 if it was new) to increment the count for the current element.
            count[i] = 1 + count.get(i, 0)
        
        # After counting the frequency of each element in the nums list, this loop iterates through the items of the count dictionary. For each item (where key is the element and val is its frequency), it appends the element key to the corresponding list in IndexFrequency at the index representing its frequency val.
        for key, val in count.items():
            IndexFrequency[val].append(key)

        result = []
        # This loop iterates backward through the IndexFrequency list, starting from the highest frequency. Within each frequency group, it iterates through the elements and appends them to the result list. It stops once the length of result reaches k, indicating that the top k most frequent elements have been found, and returns the result.
        for i in range(len(IndexFrequency) - 1, 0, -1):
            for number in IndexFrequency[i]:
                result.append(number)
                if len(result) == k:
                    return result
