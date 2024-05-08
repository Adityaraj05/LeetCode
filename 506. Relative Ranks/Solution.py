class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
      # sorted in descending order.
        list = sorted(score, reverse=True)
        count = {}
        for i in range(len(list)):
            if i == 0:
                count[list[i]] = 'Gold Medal'
            elif i == 1:
                count[list[i]] = 'Silver Medal'
            elif i == 2:
                count[list[i]] = 'Bronze Medal'
            else:
                count[list[i]] = str(i+1)
        answer = []
        for i in score:
            answer.append(count[i])
        return answer
