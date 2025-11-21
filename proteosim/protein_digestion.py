import re

# Here is an example dictionary containing cleavage patterns of proteases.
enzyme_cleavage_patterns = {
    'LysC': r'(?<=K)',
    'LysN': r'(?=K)',
    'ArgC': r'(?<=R)',
    'Trypsin': r'(?<=[KR])(?!P)'
    }


def digest_protein_sequence(protein_seq, cleave_pattern, min_pep_len=5, max_pep_len=30):
    """
    Cleaves a given amino acid sequence based on the cleave pattern of a specific protease and filters them within a specific length window.
    Parameters
    ----------
    protein_seq: str
        Protein sequence to be cleaved by the function.
    cleave_pattern: str
        Cleave pattern that corresponds to a specific protease.
    min_pep_len: int, default=5
        Minimal length of peptides to be selected.
    max_pep_len: int, default=30
        Maximal length of peptides to be selected.

    Returns
    -------
    selected_peptides: list
        Digested peptides within the specified length interval.
    """
    # peptides = re.split(cleave_pattern, protein_seq)
    selected_peptides = []
    peptides = re.split(cleave_pattern, protein_seq)
    for i in peptides:
        if min_pep_len <= len(i) <= max_pep_len:
            selected_peptides.append(i)
        else: 
            continue
    print(f'Nr. of digested peptides: {len(peptides)}')
    print(f'Nr. of digested peptides selected: {len(selected_peptides)}')
    return selected_peptides

def digest_protein_collection(protein_map, cleave_pattern, min_pep_len=5, max_pep_len=30):
    """
    Cleaves the proteins within a dictionary and selects the digested peptides within a specific length window for each protein.
    
    Parameters
    ----------
    protein_map: dict
        Dictionary containing protein ID/sequence pairs.
    cleave_pattern: str
        Cleave pattern that corresponds to a specific protease.
    min_pep_len: int
        Minimal length of peptides to be selected.
    max_pep_len: int
        Maximal length of peptides to be selected.
    
    Returns
    -------
    selected_peptides_dict: dict
        Dictionary containing the protein IDs as keys and lists with the digested peptides selected as a corresponding value.
    """
    selected_peptides_dict = {}
    for i in protein_map.keys():
        selected_peptides = []
        peptides = re.split(cleave_pattern, protein_map[i])
        for j in peptides:
            if min_pep_len <= len(j) <= max_pep_len:
                selected_peptides.append(j)
            else: 
                continue
            selected_peptides_dict[i] = selected_peptides
   
    return selected_peptides_dict

# Sequence coverage
def compute_sequence_coverage(protein_seq, peptides):
    """
    Computes the coverage percentage for any protein/peptide combination.

    Parameters
    ----------
    protein_seq: str
        Reference sequence of the intact protein.
    peptides: list
        List of selected peptides generated after digestion.
    Returns
    -------
    seq_coverage: float
        Percentage of the reference sequence covered by the selected peptides.
    """
    covered = ''
    for i in peptides:
        if i in protein_seq:
            # print("in if")
            covered = covered + i * protein_seq.count(i)
        else: 
            continue
    seq_coverage = len(covered)/len(protein_seq) * 100
    print(f'Sequence coverage: {seq_coverage} %')
    return seq_coverage




