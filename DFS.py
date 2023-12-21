class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Assuming an undirected graph

    def dfs_recursive(self, current_vertex, visited):
        visited[current_vertex] = True
        print(current_vertex, end=" ")

        for neighbor in self.graph[current_vertex]:
            if not visited[neighbor]:
                self.dfs_recursive(neighbor, visited)

    def dfs(self, start_vertex):
        visited = [False] * self.vertices
        self.dfs_recursive(start_vertex, visited)

# Example usage:
num_vertices = 4
g = Graph(num_vertices)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

start_vertex = 1
print("DFS starting from vertex", start_vertex)
g.dfs(start_vertex)
