from Week1.week1_utility import *

def string_composition_problem():
    with open('Datasets/StringComposition/quiz.txt', 'r') as datafile:
        lines = datafile.readlines()
        k = int(lines[0].strip())
        text = lines[1].strip()

    print('\n'.join(string_composition(k, text)))


def string_spelled_by_a_genome_path_problem():
    with open('Datasets/GnomePath/quiz.txt', 'r') as datafile:
        lines = datafile.readlines()
        patterns = [line.strip() for line in lines]

    print(string_spelled_by_a_genome_path(patterns))


def overlap_graph_problem():
    with open('Datasets/OverlapGraph/quiz.txt', 'r') as datafile:
        patterns = [line.strip() for line in datafile.readlines()]
    outputs = construct_overlap_graph(patterns)

    print('\n'.join(outputs))


def de_Bruijn_graph_problem():
    with open('Datasets/deBruijnGraph/quiz.txt', 'r') as datafile:
        lines = datafile.readlines()
        k = int(lines[0].strip())
        text = lines[1].strip()
    outputs = construct_de_Bruijn_graph(k, text)

    print('\n'.join(outputs))


def de_Bruijn_graph_from_kmer_problem():
    with open('Datasets/deBruijnGraphFromKMer/quiz.txt', 'r') as datafile:
        kmers = [line.strip() for line in datafile.readlines()]
    outputs = construct_de_Bruijn_graph_from_kmers(kmers)

    print('\n'.join(outputs))


# string_composition_problem()
# string_spelled_by_a_genome_path_problem()
# overlap_graph_problem()
# de_Bruijn_graph_problem()
# de_Bruijn_graph_from_kmer_problem()
