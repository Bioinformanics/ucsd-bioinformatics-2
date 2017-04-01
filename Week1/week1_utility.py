def string_composition(k, text):
    """
    String Composition Problem: Generate the k-mer composition of a string.
     Input: An integer k and a string Text.
     Output: Compositionk(Text), where the k-mers are arranged in lexicographic order.
    """
    return [text[i:i+k] for i in range(len(text)-k+1)]