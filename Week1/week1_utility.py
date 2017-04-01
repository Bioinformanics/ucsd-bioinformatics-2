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