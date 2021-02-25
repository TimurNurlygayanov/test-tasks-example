# The graph was taken from simple example
# https://youtu.be/-cuoV89nRGo?t=367

# Representation of the graph
graph = {'1': [('2', 10), ('5', 100), ('4', 30)],
         '2': [('3', 50)],
         '3': [('5', 10)],
         '4': [('3', 20), ('5', 60)],
         '5': [],
         '6': []}


def dijkstra_alg(start_node: str, end_node: str) -> dict:
    """ This function applies Dijkstra algorithm to
        find the shortest path between nodes in the graph.
    """

    current_node = start_node
    all_paths = {node_id: float('inf') for node_id in graph}
    all_paths[start_node] = 0
    visited_nodes = []

    while current_node != end_node:
        for node_id, path_cost in graph[current_node]:
            new_path_cost = all_paths[current_node] + path_cost
            if all_paths[node_id] > new_path_cost:
                all_paths[node_id] = new_path_cost

        visited_nodes.append(current_node)

        available_paths = {p: v for p, v in all_paths.items()
                           if p not in visited_nodes}

        current_node, path_cost = min(available_paths.items(),
                                      key=lambda x: x[1])

    return all_paths[end_node]


res = dijkstra_alg('1', '5')
print('The length of the shortest path', res)
