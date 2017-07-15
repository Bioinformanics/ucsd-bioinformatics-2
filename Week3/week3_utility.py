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
        mass = 0
        sub_peptide = entry[0]
        for pos in range(len(sub_peptide)):
            mass += amino_acid_mass_table[sub_peptide[pos]]
        entry[1] = mass
    return sorted(sub_peptides, key=lambda entry: entry[1])


def _get_amino_acid_mass_table():
    with open('amino_acid_mass_table.txt') as datafile:
        lines = [line.strip().split(' ') for line in datafile.readlines()]
    aas, masses = zip(*lines)
    masses = [int(mass) for mass in masses]
    return dict(zip(aas, masses))

