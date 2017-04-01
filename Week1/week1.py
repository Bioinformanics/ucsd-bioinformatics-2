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


#string_composition_problem()
string_spelled_by_a_genome_path_problem()
