import sys
from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        def floyd_warshall(n: int, shortest_path_matrix: List[List[int]]) -> None:
            # Floyd-Warshall algorithm to compute shortest paths
            for via in range(n):
                for i in range(n):
                    for j in range(n):
                        if shortest_path_matrix[i][via] + shortest_path_matrix[via][j] < shortest_path_matrix[i][j]:
                            shortest_path_matrix[i][j] = shortest_path_matrix[i][via] + shortest_path_matrix[via][j]

        def get_city_with_fewest_reachable(n: int, shortest_path_matrix: List[List[int]], distance_threshold: int) -> int:
            city_with_fewest_reachable = -1
            fewest_reachable_count = float('inf')

            for i in range(n):
                reachable_count = 0
                for j in range(n):
                    if i != j and shortest_path_matrix[i][j] <= distance_threshold:
                        reachable_count += 1

                if reachable_count <= fewest_reachable_count:
                    fewest_reachable_count = reachable_count
                    city_with_fewest_reachable = i

            return city_with_fewest_reachable

        # Initialize the shortest path matrix with large values
        inf = float('inf')
        shortest_path_matrix = [[inf] * n for _ in range(n)]

        for i in range(n):
            shortest_path_matrix[i][i] = 0  # Distance to itself is zero

        for u, v, wt in edges:
            shortest_path_matrix[u][v] = wt
            shortest_path_matrix[v][u] = wt

        # Compute shortest paths using Floyd-Warshall algorithm
        floyd_warshall(n, shortest_path_matrix)

        # Find the city with the fewest reachable cities
        return get_city_with_fewest_reachable(n, shortest_path_matrix, distanceThreshold)
