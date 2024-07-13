class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        Hashmap = {position : index for index, position in enumerate(positions)} # {5: 0, 4: 1, 3: 2, 2: 3, 1: 4}
        stack = [] # index we will using 
        for p in sorted(positions): #{1->4 , 2 -> 3 , 3 - > 2, 4 -> 1, 5 - > 0} preserving the index
            current_index = Hashmap[p]
            if directions[current_index] == "R":
                stack.append(current_index)
            else: # current robot moving to the left 
                while stack and directions[stack[-1]] == "R" and healths[current_index]:
                    prev_index = stack.pop()
                    if healths[current_index] > healths[prev_index]: # current and previous robot heatlth compaing
                        healths[prev_index] = 0 #destroy
                        healths[current_index] -=1
                    elif healths[current_index] < healths[prev_index]:
                        healths[current_index] = 0 #destroy
                        healths[prev_index] -=1
                        stack.append(prev_index)
                    else:
                        healths[current_index] = healths[prev_index] = 0 #both destroy
                # After exiting the loop, if the current robot's health is still greater than zero, its index is pushed onto the stack.
                if healths[current_index]:
                    stack.append(current_index)
        return [h for h in healths if h > 0 ] # if health is greater than 0

