
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
    cycle = []

    # build initial unvisited edges, which has all edges from graph
    for edge_map in graph:
        unvisited_edges[edge_map[0]] = list(edge_map[1])

    source = graph[0][0]
    cycle.append(source)
    while unvisited_edges:
        found_match = False
        for s, targets in unvisited_edges.items():
            if s != source:
                continue
            t = targets[0]
            targets.remove(t)
            if not targets:
                unvisited_edges.__delitem__(source)
            cycle.append(t)
            found_match = True
            source = t
            break
        if not found_match:
            cycle = cycle[1:]
            cycle.append(cycle[0])
            source = cycle[-1]

    return cycle

