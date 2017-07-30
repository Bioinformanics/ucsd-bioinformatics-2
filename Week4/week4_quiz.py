from Week4.CyclopeptideScoringProblem import score
from Week4.LeaderboardCyclopeptideSequencing import _linear_score
from Week4.SpectralConvolutionProblem import spectral_convolution

def quiz3():
    print("------ Quiz 3 ------")
    print(score("MAMA", [int(mass) for mass in "0 71 98 99 131 202 202 202 202 202 299 333 333 333 503".split(' ')]))


def quiz4():
    print("------ Quiz 4 ------")
    print(_linear_score("PEEP", [int(mass) for mass in "0 97 97 129 129 194 203 226 226 258 323 323 323 355 403 452".split(' ')]))


def quiz5():
    print("------ Quiz 5 ------")
    print(spectral_convolution([int(mass) for mass in "0 57 118 179 236 240 301".split(' ')]))


quiz3()
quiz4()
quiz5()