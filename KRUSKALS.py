class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_u] = root_v
                self.rank[root_v] += 1

def kruskals_algorithm(edges, num_vertices):
    edges.sort(key=lambda x: x[2])  
    minimum_spanning_tree = []

    disjoint_set = DisjointSet(num_vertices)

    for edge in edges:
        u, v, weight = edge
        if disjoint_set.find(u) != disjoint_set.find(v):
            minimum_spanning_tree.append(edge)
            disjoint_set.union(u, v)

    return minimum_spanning_tree

edges = [(0, 1, 2), (0, 2, 4), (1, 2, 1), (1, 3, 7), (2, 3, 3)]
num_vertices = 4

result = kruskals_algorithm(edges, num_vertices)
print("Minimum Spanning Tree:")
print("Edge \tWeight")
for edge in result:
    print(f"{edge[0]} - {edge[1]}\t{edge[2]}")