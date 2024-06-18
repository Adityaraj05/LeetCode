class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Pair difficulty with profit and sort by difficulty, If the items are tuples, it sorts primarily by the first element, difficulty = difficulty = [2,4,6,8,10], profit = [10,20,30,40,50]
        jobs = sorted(zip(difficulty, profit)) #[(2, 10), (4, 20), (6, 30), (8, 40), (10, 50)]
        
        # Sort the workers by their capability
        worker.sort()  #  [4,5,6,7]
        
        profitSum = 0
        maxProfit = 0
        j = 0
        
        for ability in worker:
            # Update maxProfit for the current worker based on their ability
            while j < len(jobs) and jobs[j][0] <= ability:
                maxProfit = max(maxProfit, jobs[j][1])
                j += 1
            # Add the best profit for this worker to the total profit
            profitSum += maxProfit
        
        return profitSum
       
