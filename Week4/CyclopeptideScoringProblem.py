"""
Cyclopeptide Scoring Problem: Compute the score of a cyclic peptide against a spectrum.
     Input: An amino acid string Peptide and a collection of integers Spectrum.
     Output: The score of Peptide against Spectrum, Score(Peptide, Spectrum).
"""

amino_acid_mass_table = {'G':57,'A':71,'S':87,'P':97,'V':99,'T':101,'C':103,'I':113,'L':113,'N':114,'D':115,'K':128,'Q':128,'E':129,'M':131,'H':137,'F':147,'R':156,'Y':163,'W':186}


def cyclospectrum(peptide):
    prefix_mass = [0]
    for i in range(len(peptide)):
        prefix_mass.append(prefix_mass[i]+amino_acid_mass_table[peptide[i]])

    theoretical_spectrum = [0]
    for i in range(len(prefix_mass)-1):
        for j in range(i+1, len(prefix_mass)):
            theoretical_spectrum.append(prefix_mass[j]-prefix_mass[i])
            if i > 0 and j < len(prefix_mass)-1:
                theoretical_spectrum.append(prefix_mass[-1] - (prefix_mass[j] - prefix_mass[i]))
    return sorted(theoretical_spectrum)


def score(cyclic_peptide, spectrum):
    theoretical_spectrum = cyclospectrum(cyclic_peptide)
    all = set(theoretical_spectrum).union(set(spectrum))
    return sum([min(theoretical_spectrum.count(mass), spectrum.count(mass)) for mass in all])


def print_score(peptide, spectrum_string):
    print(score(peptide, [int(mass) for mass in spectrum_string.split(' ')]))


def quiz():
    with open('DataSets\CyclopeptideScoring\quiz.txt', 'r') as datafile:
        lines = [line.strip() for line in datafile.readlines()]
        peptide = lines[0]
        spectrum = [int(mass) for mass in lines[1].split(' ')]
    print(score(peptide, spectrum))


#quiz()