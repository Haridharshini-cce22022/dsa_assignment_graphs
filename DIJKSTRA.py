def dijkstra(graph, source):

    num_vertices = len(graph)
    dist = [float('infinity')] * num_vertices
    dist[source] = 0
    visited = []

    while len(visited) < num_vertices:
        current_vertex = min(
            set(range(num_vertices)) - set(visited),
            key=lambda vertex: dist[vertex]
        )

        for neighbour, weight in enumerate(graph[current_vertex]):
            if weight > 0: 
                distance = dist[current_vertex] + weight
                if distance < dist[neighbour]:
                    dist[neighbour] = distance

        visited.append(current_vertex)

    return dist

example_graph = [
    [0, 7, 4, 0],
    [7, 0, 1, 5],
    [4, 1, 0, 7],
    [0, 5, 7, 0]
]

source_vertex = 0
shortest_distances = dijkstra(example_graph, source_vertex)

for vertex, distance in enumerate(shortest_distances):
    print(f"Shortest distance from {source_vertex} to {vertex}: {distance}")
