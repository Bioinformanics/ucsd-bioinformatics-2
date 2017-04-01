from Week1.week1_utility import *

def string_composition_problem():
    with open('Datasets/StringComposition/quiz.txt', 'r') as datafile:
        lines = datafile.readlines()
        k = int(lines[0].strip())
        text = lines[1].strip()

    print('\n'.join(string_composition(k, text)))

string_composition_problem()
