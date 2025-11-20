def read_fasta(filepath):
    """
    Reads a fasta file and creates a dictionary containing key-value pairs of the protein IDs and their sequences.

    Parameters
    -------
    filepath: str
        Input the path of the fasta file to be read.
    Returns
    -------
    protein_map: dict
        Dictionary containing the protein ID/sequence pairs.
    """
    protein_map = {}
    current_id = None
    current_sequence = []
    with open(filepath, 'r', encoding='utf-8') as fasta_handle:
        for line in fasta_handle:
            stripped = line.strip()
            if not stripped:
                continue
            if stripped.startswith('>'):
                if current_id is not None:
                    protein_map[current_id] = ''.join(current_sequence)
                    current_sequence = []
                current_id = stripped.split('|')[1]
            else:
                current_sequence.append(stripped)
    if current_id is not None:
        protein_map[current_id] = ''.join(current_sequence)
    return protein_map