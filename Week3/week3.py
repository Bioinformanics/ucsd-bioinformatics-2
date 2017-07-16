from Week3.week3_utility import *
from Week3.week3_utility import _get_amino_acid_mass_table


def protein_translation_problem():
    with open('DataSets\ProteinTranslation\quiz.txt', 'r') as datafile:
        rna = datafile.readline().strip()
    print(translate_protein(rna))


def peptide_encoding_problem():
    with open('DataSets\PeptideEncoding\quiz.txt', 'r') as datafile:
        dna = datafile.readline().strip()
        peptide = datafile.readline().strip()
    print('\n'.join(find_peptide_encoding(dna, peptide)))


def theoretical_spectrum_problem():
    with open('DataSets\TheoreticalSpectrum\quiz.txt', 'r') as datafile:
        peptide = datafile.readline().strip()
    print(' '.join([str(entry[1]) for entry in cyclospectrum(peptide)]))


def count_peptide_with_given_mass_problem():
    print(count_peptide_with_given_mass(1360))

# protein_translation_problem()
# peptide_encoding_problem()
# theoretical_spectrum_problem()
count_peptide_with_given_mass_problem()