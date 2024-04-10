class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # This line initializes a list named result with a length equal to the number of elements in the deck list, where each element is initialized to 0. This result list will eventually hold the sorted elements of the deck.
        result = [0] * len(deck)
        # This line sorts the deck list in ascending order. It sorts the elements of the list in place.
        deck.sort()
        # This line creates a deque object named queue, containing integers from 0 to len(deck) - 1. The deque is essentially a double-ended queue, which will be used to keep track of indices during the sorting process.
        queue = deque(range(len(deck)))

        for i in deck:
            # This line removes and returns the leftmost (first) element from the queue, assigning it to the variable index. This index represents the position in the result list where the next sorted element from deck will be placed.
            index =  queue.popleft()
            # This line assigns the current element i from the sorted deck list to the position in the result list determined by the index obtained from the queue.
            result[index] = i
            # This line checks if the queue is not empty.
            if  queue:
                # If the queue is not empty, this line removes and returns the leftmost element from the queue (which was the index used for the current element in deck) and then appends it to the right end of the queue. 
                queue.append(queue.popleft())
        return result
        
