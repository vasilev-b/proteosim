from proteosim.protein_digestion import digest_protein_sequence, digest_protein_collection, compute_sequence_coverage

def test_digest_protein_sequence():
    dummy_sequence = "AAAAAKAAAAA"
    cleave_pattern = r'(?=K)'
    assert digest_protein_sequence(dummy_sequence, cleave_pattern=cleave_pattern) == [
        'AAAAA', 'KAAAAA'
    ]

def test_digest_protein_collection():
    dummy_proteins = {
        'alpha': 'AAAAAKAAAAA',
        'beta': 'BBBBBKBBBBB'
    }
    cleave_pattern = r'(?=K)'
    assert digest_protein_collection(dummy_proteins, cleave_pattern=cleave_pattern) == {
        'alpha': ['AAAAA','KAAAAA'],
        'beta': ['BBBBB','KBBBBB']
        }

test_digest_protein_collection()

def test_compute_sequence_coverage():
    dummy_prot_seq = 'AAAAKAAAAA'
    dummy_peps = ['KAAAAA']
    coverage = compute_sequence_coverage(dummy_prot_seq, dummy_peps)
    assert coverage == 60.0

test_compute_sequence_coverage()