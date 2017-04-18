
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
    unvisited_edges = []
    cycle = []

    # build initial unvisited edges, which has all edges from graph
    for edge_map in graph:
        for targets in edge_map[1]:
            for target in targets:
                unvisited_edges.append([edge_map[0], target])

    source = unvisited_edges[0][0]
    cycle.append(source)
    while unvisited_edges:
        found_match = False
        for edge in unvisited_edges:
            if edge[0] != source:
                continue
            unvisited_edges.remove(edge)
            cycle.append(edge[1])
            found_match = True
        if not found_match:
            cycle = cycle[1:]
            cycle.append(cycle[0])

    return cycle

