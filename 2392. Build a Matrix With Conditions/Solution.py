from collections import defaultdict, deque
from typing import List

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row_order = self.topological_sort(k, rowConditions)
        col_order = self.topological_sort(k, colConditions)

        if not row_order or not col_order:
            return []

        row_pos = {row_order[i]: i for i in range(k)}
        col_pos = {col_order[i]: i for i in range(k)}

        matrix = [[0] * k for _ in range(k)]

        for i in range(k):
            matrix[row_pos[i]][col_pos[i]] = i + 1

        return matrix
        
    def topological_sort(self, n, conditions):
        graph = defaultdict(list)
        in_degree = [0] * n

        for u, v in conditions:
            graph[u - 1].append(v - 1)
            in_degree[v - 1] += 1

        queue = deque([i for i in range(n) if in_degree[i] == 0])
        topo_order = []

        while queue:
            node = queue.popleft()
            topo_order.append(node)

            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(topo_order) == n:
            return topo_order
        else:
            return []
