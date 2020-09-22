def distance(strand_a: str, strand_b: str) -> int:
    """
    Calculate the Hamming difference between two DNA strands.
    """
    if len(strand_a) == len(strand_b):
        return sum(1 for a, b in zip(strand_a, strand_b) if a != b)
    
    raise ValueError("The DNA strands are not homologous.")
