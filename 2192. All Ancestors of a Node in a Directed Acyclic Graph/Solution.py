class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def dfs(curr, parent, visited):
            # The nonlocal res statement allows the function to modify the res variable outside its scope.it must be declared with nonlocal inside dfs. Without nonlocal, any assignment to res would create a new local variable res within the dfs function's scope, leaving the original res in the enclosing scope unchanged.
            nonlocal res

            # mark current node as visited
            visited.add(curr)
            
            # check the neighbours
            for neigh in adj[curr]:
                # pass; seen before
                if neigh in visited:
                    continue
                
                # add the parent of current to the neigh list of parent
                res[neigh] += [parent]

                # recur on neigh
                dfs(neigh, parent, visited)


        # directed lookup mapping source to destination Create an adjacency list to represent the graph.
        adj = defaultdict(list)
        for src, des in edges:
            adj[src] += [des]  # adj[0] = []; adj[1] = []; adj[] = []; adj=[0, 1]...

        res = [[] for _ in range(n)]  # [[], [], [], [], [], [], [], []]
        
        # run dfs staring at each node, Initialize a list of empty lists to store ancestors for each node.
        for i in range(n):
            dfs(i, i, set())

        return res
