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


def string_reconstruction_problem():
    with open('Datasets/StringReconstruction/quiz.txt', 'r') as datafile:
        lines = datafile.readlines()
        k = int(lines[0].strip())
        kmers = [line.strip() for line in lines[1:]]
    result = string_reconstruction(k, kmers)
    print(result)


def k_universal_string_problem():
    print(k_universal_string(9))


def string_reconstruction_from_string_pairs_problem():
    with open('Datasets/StringReconstructionFromStringPairs/quiz.txt') as datafile:
        lines = datafile.readlines()
        args = lines[0].strip().split(" ")
        k = int(args[0])
        d = int(args[1])
        pairs = [pair[0:k] + pair[k + 1:k + k + 1] for pair in lines[1:]]
    result = string_reconstruction_from_string_pairs(k, d, pairs)
    print(result)


def contig_generation_problem():
    with open ('Datasets/ContigGeneration/quiz.txt') as datafile:
        kmers = [line.strip() for line in datafile.readlines()]
    contigs = generate_contigs(kmers)
    print(' '.join([str(len(contig)) for contig in contigs]))
    print('\n'.join(contigs))
    print(len(contigs))

# eulerian_cycle_problem()
# eulerian_path_problem()
# string_reconstruction_problem()
# k_universal_string_problem()
# string_reconstruction_from_string_pairs_problem()
# contig_generation_problem()


def quiz1():
    with open('Datasets/quiz1.txt', 'r') as datafile:
        lines = [line.strip() for line in datafile.readlines() if line.strip()]
    print("Quiz 1: " + string_reconstruction(len(lines[0]), lines))


def quiz3():
    with open('Datasets/quiz3.txt', 'r') as datafile:
        edges = [line.strip()[1:-1].split("|") for line in datafile.readlines() if line.strip()]
    graph = [edge[0] + edge[1] for edge in edges]

    print("Quiz 3: " + string_reconstruction_from_string_pairs(3, 1, graph))


quiz1()
quiz3()
