from utilities import *

"""
Protein Translation Problem: Translate an RNA string into an amino acid string.
     Input: An RNA string Pattern and the array GeneticCode.
     Output: The translation of Pattern into an amino acid string Peptide.
"""
def translate_protein(rna):
    codon_table = _construct_RNA_codon_table()
    protein = ''
    for i in range(int(len(rna)/3)):
        pos = i*3
        protein += codon_table[rna[pos:pos+3]]
    return protein


def _construct_RNA_codon_table():
    codon_table = {}
    with open('RNA_codon_table_1.txt', 'r') as datafile:
        entries = [line.strip().split(' ') for line in datafile.readlines()]
    for entry in entries:
        codon = entry[0]
        amino_acid = entry[1] if len(entry) == 2 else ''
        codon_table[codon] = amino_acid
    return codon_table


"""
    Peptide Encoding Problem: Find substrings of a genome encoding a given amino acid sequence.
     Input: A DNA string Text, an amino acid string Peptide, and the array GeneticCode.
     Output: All substrings of Text encoding Peptide (if any such substrings exist).
     https://stepik.org/lesson/How-Do-Bacteria-Make-Antibiotics-96/step/7?unit=8261
"""
def find_peptide_encoding(dna, peptide):
    dna_rc = get_reverse_complement(dna)
    rna = transcribe_dna(dna)
    rna_rc = transcribe_dna(dna_rc)
    rna_length = len(peptide) * 3
    results = []
    for i in range(len(rna) - rna_length + 1):
        rna_snip = rna[i:i+rna_length]
        if translate_protein(rna_snip) == peptide:
            results.append(reverse_transcribe_rna(rna_snip))
    for i in range(len(rna_rc) - rna_length + 1):
        rna_snip = rna_rc[i:i + rna_length]
        if translate_protein(rna_snip) == peptide:
            results.append(get_reverse_complement(reverse_transcribe_rna(rna_snip)))

    return results


"""
    Generating Theoretical Spectrum Problem: Generate the theoretical spectrum of a cyclic peptide.
     Input: An amino acid string Peptide.
     Output: Cyclospectrum(Peptide).
"""
def cyclospectrum(peptide):
    sub_peptides = [['',0]]
    for l in range(len(peptide))[1:]:
        for pos in range(len(peptide)):
            sub_peptide = peptide[pos:pos+l] if pos+l<=len(peptide) else peptide[pos:]+peptide[:pos+l-len(peptide)]
            sub_peptides.append([sub_peptide,0])
    if (peptide):
        sub_peptides.append([peptide,0])

    amino_acid_mass_table = _get_amino_acid_mass_table()
    for entry in sub_peptides:
        entry[1] = _get_peptide_mass(amino_acid_mass_table, entry[0])
    return sorted(sub_peptides, key=lambda entry: entry[1])


def _get_peptide_mass(amino_acid_mass_table, peptide):
    mass = 0
    for pos in range(len(peptide)):
        mass += amino_acid_mass_table[peptide[pos]]
    return mass


def _get_amino_acid_mass_table():
    with open('amino_acid_mass_table.txt') as datafile:
        lines = [line.strip().split(' ') for line in datafile.readlines()]
    aas, masses = zip(*lines)
    masses = [int(mass) for mass in masses]
    return dict(zip(aas, masses))


"""
    Counting Peptides with Given Mass Problem: Compute the number of peptides of given mass. 
    (weight combinations rather than amino acid combinations)
     Input: An integer m.
     Output: The number of linear peptides having integer mass m.
"""
def count_peptide_with_given_mass(mass):
    amino_acid_mass_table = _get_amino_acid_mass_table()
    return _count_sub_peptide_with_given_mass(amino_acid_mass_table, mass)


def _count_sub_peptide_with_given_mass(amino_acid_mass_table, m):
    """
    sum = 0
    for amino_acid in amino_acid_mass_table.keys():
        amino_acid_mass = amino_acid_mass_table[amino_acid]
        if mass == amino_acid_mass:
            sum += 1
        elif mass > amino_acid_mass:
            sum += _count_sub_peptide_with_given_mass(amino_acid_mass_table, mass - amino_acid_mass)
    return sum
    """
    peptide_masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
    masses = [0] * (m+1)
    masses[0] = 1
    for i in range(m+1):
        for j in range(len(peptide_masses)):
            if i >= peptide_masses[j]:
                masses[i] += masses[i-peptide_masses[j]]
    return masses[m]


def _count_sequence_of_sub_peptide_with_given_mass_by_brutal_force(amino_acid_mass_table, m):
    sum = 0
    for amino_acid in amino_acid_mass_table.keys():
        amino_acid_mass = amino_acid_mass_table[amino_acid]
        if m == amino_acid_mass:
            sum += 1
        elif m > amino_acid_mass:
            sum += _count_sub_peptide_with_given_mass(amino_acid_mass_table, mass - amino_acid_mass)
    return sum
