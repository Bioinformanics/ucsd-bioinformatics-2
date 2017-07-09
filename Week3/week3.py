from Week3.week3_utility import *


def protein_translation_problem():
    with open('DataSets\ProteinTranslation\quiz.txt', 'r') as datafile:
        rna = datafile.readline().strip()
    print(translate_protein(rna))


def peptide_encoding_problem():
    with open('DataSets\PeptideEncoding\quiz.txt', 'r') as datafile:
        dna = datafile.readline().strip()
        peptide = datafile.readline().strip()
    print('\n'.join(find_peptide_encoding(dna, peptide)))


"""
    Exercise Break: Solve the Peptide Encoding Problem for Bacillus brevis and Tyrocidine B1 
    (Val-Lys-Leu-Phe-Pro-Trp-Phe-Asn-Gln-Tyr). 
    How many starting positions in Bacillus brevis encode this peptide?
"""
def Tyrocidine_B1_encoding_in_Bacillus_brevis():

# protein_translation_problem()
# peptide_encoding_problem()