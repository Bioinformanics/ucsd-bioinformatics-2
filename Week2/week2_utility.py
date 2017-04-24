import itertools
from Week1.week1_utility import string_spelled_by_a_genome_path


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


def string_reconstruction(k, kmers):
    graph_dict = {}
    for kmer in kmers:
        source = kmer[:-1]
        target = kmer[1:]
        if source in graph_dict:
            graph_dict[source].append(target)
        else:
            graph_dict[source] = [target]
    graph = [[source, targets] for source,targets in graph_dict.items()]
    path = eulerian_path(graph)
    return string_spelled_by_a_genome_path(path)


def k_universal_string(k):
    sources = [format(val, "0"+str(k)+"b") for val in range(2**k)]
    graph_dict = {}
    for kmer in sources:
        source = kmer[:-1]
        target = kmer[1:]
        if source in graph_dict:
            graph_dict[source].append(target)
        else:
            graph_dict[source] = [target]
    graph = [[source, targets] for source,targets in graph_dict.items()]
    cycle = eulerian_cycle(graph)
    return ''.join(c[0] for c in cycle[:-1])


def string_reconstruction_from_string_pairs(k, d, pairs):
    edges = {}
    # build initial unvisited edges, which has all edges from graph
    for pair in pairs:
        prefix = _get_pair_prefix(pair, k)
        suffix = _get_pair_suffix(pair, k)
        if prefix in edges:
            edges[prefix].append(suffix)
        else:
            edges[prefix] = [suffix]
    graph = [[source, targets] for source, targets in edges.items()]

    path = eulerian_path(graph)
    first = string_spelled_by_a_genome_path([s[0:k-1] for s in path])
    second = string_spelled_by_a_genome_path([s[k:k+k-1] for s in path])
    return first + second[-k-d:]


def _get_pair_prefix(pair, k):
    return pair[:k-1] + pair[k:k+k-1]


def _get_pair_suffix(pair, k):
    return pair[1:k] + pair[k+1:k+k]

"""
    StringSpelledByGappedPatterns(GappedPatterns, k, d)
        FirstPatterns ← the sequence of initial k-mers from GappedPatterns
        SecondPatterns ← the sequence of terminal k-mers from GappedPatterns
        PrefixString ← StringSpelledByGappedPatterns(FirstPatterns, k)
        SuffixString ← StringSpelledByGappedPatterns(SecondPatterns, k)
        for i = k + d + 1 to |PrefixString|
            if the i-th symbol in PrefixString does not equal the (i - k - d)-th symbol in SuffixString
                return "there is no string spelled by the gapped patterns"
        return PrefixString concatenated with the last k + d symbols of SuffixString
"""
def string_spelled_by_gapped_pattern(k, d, pairs):
    pass
