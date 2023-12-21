def dynamic_programming(graph, destination):

    num_vertices = len(graph)
    dist = [float('infinity')] * num_vertices
    dist[destination] = 0
    unvisited_vertices = list(range(num_vertices))

    while unvisited_vertices:

        current_vertex = min(unvisited_vertices, key=lambda vertex: dist[vertex])

        for neighbour, weight in enumerate(graph[current_vertex]):
            if weight > 0:  
                distance = dist[current_vertex] + weight
                if distance < dist[neighbour]:
                    dist[neighbour] = distance

        unvisited_vertices.remove(current_vertex)

    return dist

example_graph = [
    [0, 7, 4, 0],
    [7, 0, 6, 5],
    [4, 6, 0, 7],
    [0, 5, 7, 0]
]

destination_vertex = 0
shortest_distances = dynamic_programming(example_graph, destination_vertex)

for vertex, distance in enumerate(shortest_distances):
    print(f"Shortest distance from {vertex} to {destination_vertex}: {distance}")
