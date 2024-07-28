from collections import defaultdict, deque
from typing import List
import math


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # Create the graph using an adjacency list
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # Initialize distance arrays with infinity
        min_distance = [math.inf] * (n + 1)
        second_min_distance = [math.inf] * (n + 1)

        # Queue for BFS, starting with the source node (1)
        queue = deque([(0, 1)])  # (current_time, node)
        min_distance[1] = 0

        while queue:
            current_time, node = queue.popleft()
            for neighbor in graph[node]:
                # Calculate the new cost considering the traffic light changes
                red_light_cycles = current_time // change
                new_time = current_time + time
                if red_light_cycles % 2:  # If we are in a red light period
                    new_time = (change * (1 + red_light_cycles)) + time

                # Update the minimum and second minimum distances
                if min_distance[neighbor] > new_time:
                    second_min_distance[neighbor] = min_distance[neighbor]
                    min_distance[neighbor] = new_time
                    queue.append((new_time, neighbor))
                elif min_distance[neighbor] < new_time < second_min_distance[neighbor]:
                    second_min_distance[neighbor] = new_time
                    queue.append((new_time, neighbor))

        return second_min_distance[n]
