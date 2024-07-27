import sys
import math

class Solution:
    def FloydWarshall(self, adjMatrix, original, changed, cost):
        n = 26  # Number of letters in the alphabet
        
        # Initialize the adjacency matrix
        for i in range(n):
            for j in range(n):
                if i != j:
                    adjMatrix[i][j] = math.inf
        
        # Apply given costs
        for i in range(len(original)):
            s = ord(original[i]) - ord('a')
            t = ord(changed[i]) - ord('a')
            adjMatrix[s][t] = min(adjMatrix[s][t], cost[i])
        
        # Apply Floyd-Warshall algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    adjMatrix[i][j] = min(adjMatrix[i][j], adjMatrix[i][k] + adjMatrix[k][j])
    
    def minimumCost(self, source, target, original, changed, cost):
        n = 26  # Number of letters in the alphabet
        adjMatrix = [[math.inf] * n for _ in range(n)]
        
        self.FloydWarshall(adjMatrix, original, changed, cost)
        
        total_cost = 0
        
        for i in range(len(source)):
            if source[i] == target[i]:
                continue
            
            s = ord(source[i]) - ord('a')
            t = ord(target[i]) - ord('a')
            
            if adjMatrix[s][t] == math.inf:
                return -1
            
            total_cost += adjMatrix[s][t]
        
        return total_cost
