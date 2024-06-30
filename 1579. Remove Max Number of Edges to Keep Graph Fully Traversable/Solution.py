# __init__(self, n): Initializes the Union-Find data structure for n nodes
class UnionFind:
    def __init__(self, n): #self.n stores the number of nodes.
        self.n = n
        # self.parent is a list where each node is its own parent initially.
        self.parent = [i for i in range(n+1)]
        # to keep track of component, size of each component 
        self.ranks = [1] * (n + 1)
    # method to find root parent of the component
    def find(self, node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node
    # it's a method to union of two components it will return 1 if we successful union or 0 if its already connected, It finds the root parents of both nodes.
    def union(self, node1, node2):
        par1, par2 = self.find(node1), self.find(node2)
        # If both nodes have the same root parent, they are already connected, so it returns 0
        if par1 == par2:
            return 0
        # Otherwise, it merges the sets based on rank to keep the tree shallow
        if self.ranks[par1] > self.ranks[par2]:
            self.parent[par2] = par1
            self.ranks[par1] += self.ranks[par2]
        else:
            self.parent[par1] = par2
            self.ranks[par2] += self.ranks[par1]
            # The number of disjoint sets (self.n) is decremented.
        self.n -= 1
        # It returns 1 to indicate a successful union.
        return 1
        # Checks if there is only one set (i.e., all nodes are connected).Returns True if self.n is less than or equal to 1.
    def isConnected(self):
        return self.n <= 1



class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice, bob = UnionFind(n), UnionFind(n)
        total = 0 # number of edges we have to keep

        for color, src, dst in edges: # here color represent Types of edges
            if color == 3: # both can traverse
                a = alice.union(src, dst)
                b = bob.union(src, dst)
                # If at least one of the unions is successful, it increments total.
                total += 1 if (a or b) else 0

        for color, src, dst in edges:
            if color == 1: # only alice can traverse
                total += alice.union(src, dst)
            elif color == 2: ## only bob can traverse
                total += bob.union(src, dst)
  
        if bob.isConnected() and alice.isConnected():
            # If both are connected, it returns the number of edges that can be removed (len(edges) - total).
            return len(edges) - total
            # it returns -1 indicating it's not possible to connect the graph for both Alice and Bob.
        return -1
        
