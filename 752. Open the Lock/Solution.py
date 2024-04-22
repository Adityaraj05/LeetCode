class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # This line checks if the starting combination "0000" is among the deadends (combinations that cannot be used). If it is, the function immediately returns -1 indicating that it's impossible to reach the target.
        if "0000" in deadends:
            return -1
        # This line defines a function called children that generates all the possible combinations that can be reached from a given lock combination.
        def children(lock):
            # This line initializes an empty list to store the generated combinations.
            result = []
            # This line starts a loop that iterates over each digit position (0 to 3) in the lock combination.
            for i in range(4):
                # This line calculates the digit obtained by incrementing the digit at position i in the lock combination by 1, wrapping around to 0 if the result is 10.
                digit = str((int(lock[i])+1) % 10)  
                # This line constructs a new combination by replacing the digit at position i in the lock combination with the incremented digit and appends it to the result list.
                result.append(lock[:i] + digit + lock[i+1:])
                # This line calculates the digit obtained by decrementing the digit at position i in the lock combination by 1, wrapping around to 9 if the result is -1.
                digit = str((int(lock[i])-1+10) % 10)  
                # This line constructs a new combination by replacing the digit at position i in the lock combination with the decremented digit and appends it to the result list.
                result.append(lock[:i] + digit + lock[i+1:])
            return result
        # This line creates a deque, a double-ended queue, which will be used to perform breadth-first search.
        q = deque()
        # This line adds a tuple containing the starting lock combination "0000" and the number of turns taken (0) to the deque. This represents the initial state of the search.
        q.append(("0000", 0))  # (lock, turns)
        # This line creates a set called visit containing the combinations in deadends, which have already been visited and should be avoided during the search.
        visit = set(deadends)
        # This line starts a while loop that continues as long as the deque q is not empty, indicating that there are still combinations to explore.
        while q:
            # This line dequeues a combination lock and the corresponding number of turns turns from the left end of the deque q for exploration.
            lock, turns = q.popleft()
            if lock == target:
                # This line checks if the current combination lock is equal to the target combination. If it is, it means we have reached the target, so the function returns the number of turns taken.
                return turns
                # This line iterates over each possible combination generated from the current combination lock.
            for child in children(lock):
                # This line checks if the child combination has not been visited before. If it hasn't, it means it's a valid combination to explore.
                if child not in visit:
                    # This line adds the child combination to the set visit, marking it as visited to avoid revisiting it.

                    visit.add(child)
                    # This line adds the child combination along with the incremented number of turns to the deque q, indicating that it should be explored in the next iteration of the loop.
                    q.append((child, turns + 1))
        # This line is outside the loop and is reached if the target combination cannot be reached from any valid combination. It returns -1 to indicate failure.
        return -1
    
