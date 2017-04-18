import itertools


"""
    EulerianCycle(Graph)
        form a cycle Cycle by randomly walking in Graph (don't visit the same edge twice!)
        while there are unexplored edges in Graph
            select a node newStart in Cycle with still unexplored edges
            form Cycle’ by traversing Cycle (starting at newStart) and then randomly walking
            Cycle ← Cycle’
        return Cycle
"""
def eulerian_cycle(graph):
    unvisited_edges = {}

    # build initial unvisited edges, which has all edges from graph
    for edge_map in graph:
        unvisited_edges[edge_map[0]] = list(edge_map[1])

    return _find_eulerian_cycle(graph[0][0], unvisited_edges)

def eulerian_path(graph):
    unvisited_edges = {}
    path = []

    # build initial unvisited edges, which has all edges from graph
    for edge_map in graph:
        unvisited_edges[edge_map[0]] = list(edge_map[1])

    in_nodes = list(itertools.chain.from_iterable([edge_map[1] for edge_map in graph]))
    in_counts = {node:in_nodes.count(node) for node in set(in_nodes)}
    start = None
    end = None
    for out_s, out_ts in unvisited_edges.items():
        if not in_counts.__contains__(out_s):
            start = out_s
            break
        out_count = len(out_ts)
        in_count = in_counts[out_s]
        if out_count > in_count:
            start = out_s
            break
        if out_count < in_count:
            end = out_s
    if not end:
        for in_node in in_counts:
            if not unvisited_edges.__contains__(in_node):
                end = in_node
                break

    if unvisited_edges.__contains__(end):
        unvisited_edges[end].append(start)
    else:
        unvisited_edges[end] = [start]

    cycle = _find_eulerian_cycle(start, unvisited_edges)
    positions = [index for index in range(len(cycle)-1) if (cycle[index] == end and cycle[index+1] == start)]
    position = positions[0]
    path = cycle[position+1:] + cycle[1:position+1]
    return path


def _find_eulerian_cycle(start, unvisited_edges):
    cycle = [start]
    while unvisited_edges:
        found_match = False
        for s, targets in unvisited_edges.items():
            if s != start:
                continue
            t = targets[0]
            targets.remove(t)
            if not targets:
                unvisited_edges.__delitem__(start)
            cycle.append(t)
            found_match = True
            start = t
            break
        if not found_match:
            cycle = cycle[1:]
            cycle.append(cycle[0])
            start = cycle[-1]
    return cycle


