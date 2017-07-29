
"""
Code Challenge: Implement ConvolutionCyclopeptideSequencing.
     Input: An integer M, an integer N, and a collection of (possibly repeated) integers Spectrum.
     Output: A cyclic peptide LeaderPeptide with amino acids taken only from the top M elements (and ties) of the convolution of
     Spectrum that fall between 57 and 200, and where the size of Leaderboard is restricted to the top N (and ties).
"""

def _get_spectral_convolution_dict(spectrum):
    spectrum = sorted(spectrum)
    convolution_dict = {}
    for i in range(len(spectrum)-1):
        for j in range(i, len(spectrum)):
            mass = spectrum[j] - spectrum[i]
            if mass < 57 or mass > 200: continue
            if mass in convolution_dict:
                convolution_dict[mass] += 1
            else:
                convolution_dict[mass] = 1
    return convolution_dict


def _get_top_m_elements(convolution_dict, m):
    convolution = [(key, val) for key, val in convolution_dict.items()]
    sorted_convolution = sorted(convolution, key=lambda entry: entry[1], reverse=True)
    trim_pos = m-1
    for trim_pos in range(m-1, len(sorted_convolution)-1):
        if sorted_convolution[trim_pos][1] > sorted_convolution[trim_pos+1][1]:
            break
    return [entry[0] for entry in sorted_convolution[:trim_pos+1]]


def _expand(peptides, amino_acid_mass_list):
    #return [peptide.copy().append(mass) for mass in amino_acid_mass_list for peptide in peptides]
    new_peptides = []
    for peptide in peptides:
        for mass in amino_acid_mass_list:
            new_peptide = list(peptide)
            new_peptide.append(mass)
            new_peptides.append(new_peptide)
    return new_peptides


def _get_parent_mass(spectrum):
    return spectrum[-1]


def _score(peptide, spectrum):
    ls = _cyclospectrum(peptide)
    cs = spectrum.copy()
    score = 0
    for c in ls:
        if c in cs:
            score += 1
            cs.remove(c)
    return score


def _cyclospectrum(peptide):
    prefix_mass = [0]
    for i in range(len(peptide)):
        prefix_mass.append(prefix_mass[i]+peptide[i])

    theoretical_spectrum = [0]
    for i in range(len(prefix_mass)-1):
        for j in range(i+1, len(prefix_mass)):
            theoretical_spectrum.append(prefix_mass[j]-prefix_mass[i])
            if i > 0 and j < len(prefix_mass)-1:
                theoretical_spectrum.append(prefix_mass[-1] - (prefix_mass[j] - prefix_mass[i]))
    return sorted(theoretical_spectrum)


def _linear_spectrum(peptide):
    prefix_mass = [0]
    for i in range(len(peptide)):
        prefix_mass.append(prefix_mass[i]+peptide[i])

    theoretical_spectrum = [0]
    for i in range(len(prefix_mass)-1):
        for j in range(i+1, len(prefix_mass)):
            theoretical_spectrum.append(prefix_mass[j]-prefix_mass[i])
    return sorted(theoretical_spectrum)


def trim(leaderboard, spectrum, n):
    if len(leaderboard) <= n:
        return leaderboard
    sorted_leaderboard = [(peptide, _score(peptide, spectrum)) for peptide in leaderboard]
    sorted_leaderboard = sorted(sorted_leaderboard, key=lambda entry: entry[1], reverse=True)
    trim_pos = n-1
    for trim_pos in range(n-1, len(leaderboard)-1):
        if sorted_leaderboard[trim_pos][1] > sorted_leaderboard[trim_pos+1][1]:
            break
    return [entry[0] for entry in sorted_leaderboard[:trim_pos+1]]


# peptides are represented as list of amino acid masses rather than amino acid string
def _leaderboard_cyclopeptide_sequencing(spectrum, n, amino_acid_mass_list):
    leaderboard = [[]]
    leader_peptide = ''
    leader_peptide_score = 0
    while leaderboard:
        leaderboard = _expand(leaderboard, amino_acid_mass_list)
        loop = list(leaderboard)
        for peptide in loop:
            mass = sum(peptide)
            parent_mass = _get_parent_mass(spectrum)
            if mass == parent_mass:
                score = _score(peptide, spectrum)
                if score > leader_peptide_score:
                    leader_peptide = peptide
                    leader_peptide_score = score
            elif mass > parent_mass:
                leaderboard.remove(peptide)
        leaderboard = trim(leaderboard, spectrum, n)
    return leader_peptide


def convolution_cyclopeptide_sequencing(m, n, spectrum):
    spectrum = sorted(spectrum)
    convolution_dict = _get_spectral_convolution_dict(spectrum)
    top_m_amino_acid_mass = _get_top_m_elements(convolution_dict, m)
    return _leaderboard_cyclopeptide_sequencing(spectrum, n, top_m_amino_acid_mass)


def quiz():
    with open('DataSets\ConvolutionCyclopeptideSequencing\quiz.txt', 'r') as datafile:
        lines = [line.strip() for line in datafile.readlines()]
        m = int(lines[0])
        n = int(lines[1])
        spectrum = [int(mass) for mass in lines[2].split(' ')]
    print('-'.join([str(mass) for mass in convolution_cyclopeptide_sequencing(m, n, spectrum)]))


#quiz()