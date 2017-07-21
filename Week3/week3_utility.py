from utilities import *

AMINO_ACID_MASSES = [57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]

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
    amino_acid_mass_table = _get_amino_acid_mass_table()
    return _cyclospectrum(amino_acid_mass_table, peptide)


def _cyclospectrum(amino_acid_mass_table, peptide):
    sub_peptides = [['',0]]
    for l in range(len(peptide))[1:]:
        for pos in range(len(peptide)):
            sub_peptide = peptide[pos:pos+l] if pos+l<=len(peptide) else peptide[pos:]+peptide[:pos+l-len(peptide)]
            sub_peptides.append([sub_peptide,0])
    if (peptide):
        sub_peptides.append([peptide,0])

    for entry in sub_peptides:
        entry[1] = _get_peptide_mass(amino_acid_mass_table, entry[0])
    return sorted(sub_peptides, key=lambda entry: entry[1])


def linearspectrum(peptide):
    amino_acid_mass_table = _get_amino_acid_mass_table()
    sub_peptides = [['',0]]
    for l in range(len(peptide))[1:]:
        for pos in range(len(peptide)):
            if pos + l <= len(peptide):
                sub_peptide = peptide[pos:pos+l]
                sub_peptides.append([sub_peptide,0])
    if (peptide):
        sub_peptides.append([peptide,0])

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
    masses = [0] * (m+1)
    masses[0] = 1
    for i in range(m+1):
        for j in range(len(AMINO_ACID_MASSES)):
            if i >= AMINO_ACID_MASSES[j]:
                masses[i] += masses[i-AMINO_ACID_MASSES[j]]
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


"""
    CyclopeptideSequencing(Spectrum)
        Peptides ← a set containing only the empty peptide
        while Peptides is nonempty
            Peptides ← Expand(Peptides)
            for each peptide Peptide in Peptides
                if Mass(Peptide) = ParentMass(Spectrum)
                    if Cyclospectrum(Peptide) = Spectrum
                        output Peptide
                    remove Peptide from Peptides
                else if Peptide is not consistent with Spectrum
                    remove Peptide from Peptides
    - Cyclospectrum(Peptide): https://stepik.org/lesson/Sequencing-Antibiotics-by-Shattering-Them-into-Pieces-98/step/4?course=Stepic-Interactive-Text-for-Week-3&unit=8263
    - Mass(Peptide): the total mass of an amino acid string Peptide
    - ParentMass(Spectrum): equal to the largest mass in Spectrum
"""
def cyclopeptide_sequencing_v1(spectrum):
    spectrum = [int(amino) for amino in spectrum.split(' ')]
    sequences = []
    candidates = ['']
    amino_acid_mass_table = _get_amino_acid_mass_table()
    spectrum_set = set(spectrum)
    while candidates:
        peptides = _expand(candidates, amino_acid_mass_table)
        candidates = list(peptides)
        for peptide in peptides:
            mass = _get_peptide_mass(amino_acid_mass_table, peptide)
            parent_mass = spectrum[-1]
            cs = [entry[1] for entry in cyclospectrum(peptide)]
            if mass == parent_mass:
                if cs == spectrum:
                    sequences.append([amino_acid_mass_table[amino_acid] for amino_acid in peptide])
                candidates.remove(peptide)
            elif cs[-1] > spectrum[-1] or not set(cs).issubset(spectrum_set):
                candidates.remove(peptide)
    return sequences


def _expand(peptides, amino_acid_mass_table):
    return [peptide + amino_acid for amino_acid in amino_acid_mass_table.keys() for peptide in peptides]


"""
Version 2 of cyclopeptide_sequencing which iterates amino acid mass list instead of amino acid list
"""
def cyclopeptide_sequencing(spectrum):
    spectrum = [int(amino) for amino in spectrum.split(' ')]
    sequences = []
    candidate_peptides = [[]]
    spectrum_set = set(spectrum)
    while candidate_peptides:
        #peptides = [peptide.append(aa_mass) for aa_mass in AMINO_ACID_MASSES for peptide in candidate_peptides]
        peptides = []
        for peptide in candidate_peptides:
            for aa_mass in AMINO_ACID_MASSES:
                if aa_mass not in spectrum_set:
                    continue
                candidate = list(peptide)
                candidate.append(aa_mass)
                peptides.append(candidate)
        candidate_peptides = list(peptides)
        for peptide in peptides:
            if not peptide:
                candidate_peptides.remove(peptide)
            mass = sum(peptide)
            parent_mass = spectrum[-1]
            if mass == parent_mass:
                cs = _cyclospectrum_mass(peptide)
                if cs == spectrum:
                    sequences.append(peptide)
                candidate_peptides.remove(peptide)
            else:
                #TODO: should use linearspectrum() here
                cs = _cyclospectrum_mass(peptide)
                if cs[-1] > spectrum[-1]:
                    candidate_peptides.remove(peptide)
                else:
                    cs_set = set(cs)
                    if (not cs_set.issubset(spectrum_set)):
                        candidate_peptides.remove(peptide)
    return sequences

def _cyclospectrum_mass(peptide):
    spectrum = [0]
    for l in range(len(peptide))[1:]: #exclude length 0
        for pos in range(len(peptide)):
            sub_peptide = peptide[pos:pos+l] if pos+l<=len(peptide) else peptide[pos:]+peptide[:pos+l-len(peptide)]
            spectrum.append(sum(sub_peptide))
            #if pos + l <= len(peptide):
            #    sub_peptide = peptide[pos:pos + l]
            #    spectrum.append(sum(sub_peptide))
    if (peptide):
        spectrum.append(sum(peptide))
    return sorted(spectrum)
