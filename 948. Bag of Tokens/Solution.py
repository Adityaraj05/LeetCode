class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # firstly we are initializing the variable resutl and score 
        result, score = 0, 0
        # sorting the token
        tokens.sort()
        # two pointer left and right 
        left, right = 0, len(tokens)-1
        # traversing through while loop
        while left <= right:
            # Face-up: If your current power is at least tokens[i], you may play tokeni, losing tokens[i] power and gaining 1 score.
            if power >= tokens[left]:
                power -= tokens[left]
                left +=1
                score +=1
                result = max(result, score)
            #  Face-down: If your current score is at least 1, you may play tokeni, gaining tokens[i] power and losing 1 score.  
            elif score > 0:
                power += tokens[right]
                right -=1
                score -=1
                # if we don't have enough power or score then we break the loop
            else:
                break
        return result

        
