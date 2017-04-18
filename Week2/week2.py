from Week2.week2_utility import *

def eulerian_cycle_problem():
    graph = []
    with open('Datasets/EulerianCycle/quiz.txt', 'r') as datafile:
        for line in datafile.readlines():
            edge_map = line.strip().split(" -> ")
            source = edge_map[0]
            targets = edge_map[1].split(",")
            graph.append([source, targets])
    cycle = eulerian_cycle(graph)
    print("->".join(cycle))


def eulerian_path_problem():
    graph = []
    with open('Datasets/EulerianPath/quiz.txt', 'r') as datafile:
        for line in datafile.readlines():
            edge_map = line.strip().split(" -> ")
            source = edge_map[0]
            targets = edge_map[1].split(",")
            graph.append([source, targets])
    path = eulerian_path(graph)
    print("->".join(path))


#eulerian_cycle_problem()
eulerian_path_problem()
