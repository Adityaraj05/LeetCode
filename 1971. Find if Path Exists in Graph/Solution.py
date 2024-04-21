class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #  initializes an empty defaultdict named adjacency_list, which will be used to store the adjacency list representation of the graph. defaultdict is a dictionary-like object that provides a default value for keys that haven't been seen before. In this case, the default value is an empty list.
        adjacency_list = collections.defaultdict(list)
        # This loop iterates over each edge (u, v) in the edges list. For each edge, it adds v to the list of neighbors of u and adds u to the list of neighbors of v. This builds an undirected graph representation in the adjacency_list dictionary.
        for u, v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)
        # This line initializes an empty set named visited, which will be used to keep track of the nodes that have been visited during the DFS traversal.
        visited = set()
        # This line defines a recursive function named dfs that performs a depth-first search (DFS) traversal of the graph starting from the given node.
        def dfs(node):
            #  checks if the current node is equal to the destination. If they are the same, it means that we have found a path from the source to the destination, so the function returns True to indicate that.
            if node == destination:
                return True
            # This line adds the current node to the set of visited nodes to mark it as visited.
            visited.add(node)
            # This loop iterates over each neighbor v of the current node in the adjacency list. 
            for v in adjacency_list[node]:
                # If v has not been visited yet (v not in visited), the dfs function is called recursively with v as the argument. If the recursive call returns True, it means that a path to the destination has been found, so the function returns True immediately.
                if v not in visited and dfs(v):
                    return True
            # If none of the neighbors of the current node leads to the destination, the function returns False to indicate that no path from the source to the destination was found.
            return False
            # dfs function with the source node as the argument. This initiates the DFS traversal from the source node and returns True if a path to the destination is found, otherwise False.
        return dfs(source)
        
