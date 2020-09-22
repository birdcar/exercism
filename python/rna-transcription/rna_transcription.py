def to_rna(dna_strand: str):
    """
    Given a DNA strand, return it's RNA complement (per RNA transcription).
    """
    for char in dna_strand:
        if char not in 'GCTA':
            raise ValueError("Your DNA strand contains invalid nucleotides.")

    return dna_strand.translate(str.maketrans('GCTA', 'CGAU'))
