from collections import deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u) 

    def bfs(self, start_vertex):
        visited = [False] * self.vertices
        queue = deque([start_vertex])

        while queue:
            current_vertex = queue.popleft()
            if not visited[current_vertex]:
                print(current_vertex, end=" ")
                visited[current_vertex] = True

                for neighbour in self.graph[current_vertex]:
                    if not visited[neighbour]:
                        queue.append(neighbour)

num_vertices = 4
g = Graph(num_vertices)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

start_vertex = 3
print("BFS starting from vertex", start_vertex)
g.bfs(start_vertex)
