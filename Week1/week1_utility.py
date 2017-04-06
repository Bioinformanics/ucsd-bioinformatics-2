from utilities import Node

def string_composition(k, text):
    """
    String Composition Problem: Generate the k-mer composition of a string.
     Input: An integer k and a string Text.
     Output: Compositionk(Text), where the k-mers are arranged in lexicographic order.
    """
    return [text[i:i+k] for i in range(len(text)-k+1)]


def string_spelled_by_a_genome_path(patterns):
    """
    String Spelled by a Genome Path Problem. Reconstruct a string from its genome path.
     Input: A sequence of k-mers Pattern1, … ,Patternn such that the last k - 1 symbols
            of Patterni are equal to the first k-1 symbols of Patterni+1 for 1 ≤ i ≤ n-1.
     Output: A string Text of length k+n-1 such that the i-th k-mer in Text is equal to Patterni  (for 1 ≤ i ≤ n).
    """
    return ''.join([pattern[0] for pattern in patterns]) + patterns[-1][1:]


def construct_overlap_graph(patterns):
    """
    Overlap Graph Problem: Construct the overlap graph of a collection of k-mers.
     Input: A collection Patterns of k-mers.
     Output: The overlap graph Overlap(Patterns), in the form of an adjacency list. (You may return the edges in any order.)
    """
    matches = ([pattern1, pattern2] for i,pattern1 in enumerate(patterns) for j,pattern2 in enumerate(patterns)
             if ((i != j) and pattern2.startswith(pattern1[1:])))
    outputs = [match[0]+" -> "+match[1] for match in matches]
    return outputs


def construct_de_Bruijn_graph(k, text):
    """
    De Bruijn Graph from a String Problem: Construct the de Bruijn graph of a string.
     Input: An integer k and a string Text.
     Output: DeBruijnk(Text).
    """
    edges = [text[i:i+k] for i in range(len(text)-k+1)]
    return construct_de_Bruijn_graph_from_kmers(edges)

def construct_de_Bruijn_graph_from_kmers(kmers):
    matches = {}
    for kmer in kmers:
        parent = kmer[:-1]
        child = kmer[1:]
        if matches.__contains__(parent):
            matches[parent].insert(0, child)
        else:
            matches[parent] = [child]

    outputs = [key+" -> "+','.join(matches[key]) for key in list(matches.keys())]
    return outputs
