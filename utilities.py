def AreStringListsEqual(expected, result):
    if len(expected) != len(result):
        _print_list_difference(expected, result)
        return False
    for val in expected:
        if (val not in result) or expected.count(val) != result.count(val):
            _print_list_difference(expected, result)
            return False
    return True


def _print_list_difference(expected, result):
    print("Expected: " + str(len(expected)) + ", " + ' '.join(expected) + "\n")
    print("Result:   " + str(len(result)) + ", " + ' '.join(result) + "\n")


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


def get_reverse_complement(dna):
    dna = str.upper(dna)
    complement = ''
    for base in dna:
        if base == 'A':
            complement += 'T'
        elif base == 'T':
            complement += 'A'
        elif base == 'C':
            complement += 'G'
        elif base == 'G':
            complement += 'C'
        else:
            raise Exception('Invalid DNA base.')
    return complement[::-1]


def transcribe_dna(dna):
    return dna.replace('T', 'U')

def reverse_transcribe_rna(rna):
    return rna.replace('U', 'T')