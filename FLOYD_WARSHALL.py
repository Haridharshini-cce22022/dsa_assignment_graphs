def floyd_warshall(graph):
    num_vertices = len(graph)
    
    dist = [[float('infinity') for _ in range(num_vertices)] for _ in range(num_vertices)]

    for i in range(num_vertices):
        dist[i][i] = 0
        for j in range(num_vertices):
            if graph[i][j] != 0:
                dist[i][j] = graph[i][j]

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

example_graph = [
    [0, 1, 9, 0],
    [14, 0, 2, 5],
    [4, 6, 0, 10],
    [0, 5, 1, 0]
]

shortest_distances = floyd_warshall(example_graph)

for i in range(len(shortest_distances)):
    for j in range(len(shortest_distances[i])):
        print(f"Shortest distance from {i} to {j}: {shortest_distances[i][j]}")

