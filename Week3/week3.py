from itertools import permutations

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


def cyclopeptide_sequencing_problem():
    #spectrum = "0 71 97 99 103 113 113 114 115 131 137 196 200 202 208 214 226 227 228 240 245 299 311 311 316 327 337 339 340 341 358 408 414 424 429 436 440 442 453 455 471 507 527 537 539 542 551 554 556 566 586 622 638 640 651 653 657 664 669 679 685 735 752 753 754 756 766 777 782 782 794 848 853 865 866 867 879 885 891 893 897 956 962 978 979 980 980 990 994 996 1022 1093"
    spectrum = "0 101 103 113 113 113 114 114 114 131 186 204 215 217 227 227 227 244 245 299 299 318 318 328 330 341 358 358 412 413 430 431 431 432 444 471 472 514 526 543 544 545 545 545 575 585 617 627 657 657 657 658 659 676 688 730 731 758 770 771 771 772 789 790 844 844 861 872 874 884 884 903 903 957 958 975 975 975 985 987 998 1016 1071 1088 1088 1088 1089 1089 1089 1099 1101 1202"
    sequences = cyclopeptide_sequencing_v1(spectrum)
    sequence_strings = ['-'.join(map(str, sequence)) for sequence in sequences]
    print(' '.join(sequence_strings))

# protein_translation_problem()
# peptide_encoding_problem()
# theoretical_spectrum_problem()
# count_peptide_with_given_mass_problem()
#cyclopeptide_sequencing_problem()


def quiz2():
    print("----- Quiz 2 -----")
    rnas = ["CCAAGUACAGAGAUUAAC", "CCGAGGACCGAAAUCAAC", "CCAAGAACAGAUAUCAAU", "CCUCGUACAGAAAUCAAC"]
    for rna in rnas:
        if translate_protein(rna) == "PRTEIN":
            print(str(rnas.index(rna)+1))


def quiz3():
    print("----- Quiz 3 -----")
    #rnas = permutations(['A','C','G','U'], 5)
    #print(len([rna for rna in rnas if translate_protein(rna) == 'LEADER']))

    #print(6*2*4*2*2*6)  # LEADER
    print(1*4*6*6)  # MASS


def quiz4():
    print("----- Quiz 4 -----")
    #table = _get_amino_acid_mass_table()
    #print(sum([table[amino_acid] for amino_acid in "GLY"]))


def quiz5():
    print("----- Quiz 5 -----")
    peptides = ["MTAI", "MLAT", "TAIM", "ALTM", "MAIT", "TMLA"]
    for peptide in peptides:
        spectrum = [str(item[1]) for item in cyclospectrum(peptide)]
        if ' '.join(spectrum) == "0 71 101 113 131 184 202 214 232 285 303 315 345 416":
            print(str(peptides.index(peptide)+1))


def quiz6():
    print("----- Quiz 6 -----")
    #peptides = ["TCE", "AQV", "VAQ", "ETC", "CTV", "CET"]
    peptides = ["ETC", "TCE", "CTV", "QCV", "AQV", "CTQ"]
    spectrum_set = set("0 71 99 101 103 128 129 199 200 204 227 230 231 298 303 328 330 332 333".split(' '))
    for peptide in peptides:
        sub_spectrum = [str(item[1]) for item in linearspectrum(peptide)]
        if set(sub_spectrum).issubset(spectrum_set):
            print(str(peptides.index(peptide)+1))


quiz2()
quiz3()
quiz4()
quiz5()
quiz6()