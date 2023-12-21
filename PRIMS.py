class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight 

    def find_min_key(self, key, in_mst):
        min_key = float('inf')
        min_index = -1

        for v in range(self.vertices):
            if key[v] < min_key and not in_mst[v]:
                min_key = key[v]
                min_index = v

        return min_index

    def prim(self):
        key = [float('inf')] * self.vertices
        parent = [None] * self.vertices
        in_mst = [False] * self.vertices

        key[0] = 0
        parent[0] = -1

        for _ in range(self.vertices - 1):
            current_vertex = self.find_min_key(key, in_mst)

            in_mst[current_vertex] = True

            for v in range(self.vertices):
                if 0 < self.graph[current_vertex][v] < key[v] and not in_mst[v]:
                    key[v] = self.graph[current_vertex][v]
                    parent[v] = current_vertex

        print("Edge \tWeight")
        for i in range(1, self.vertices):
            print(f"{parent[i]} - {i}\t{self.graph[i][parent[i]]}")

num_vertices = 5
g = Graph(num_vertices)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)

print("Minimum Spanning Tree (Prim's Algorithm):")
g.prim()
