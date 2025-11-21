from proteosim.mass_spectra_simulation import calculate_mol_mass, calculate_mol_mass_collection, calculate_mz_collection

def test_calculate_mol_mass():
    aa_mass_dict = {
        'A': 5, 'B': 10, 'C': 1
    }
    test_peptide = 'ABBB'
    expected_mass = 35
    calculated_mass = calculate_mol_mass(test_peptide, amino_acid_mass_dict=aa_mass_dict)['ABBB']
    assert calculated_mass == expected_mass

test_calculate_mol_mass()

def test_calculate_mol_mass_collection():
    aa_mass_dict = {
        'A': 5, 'B': 10, 'C': 1
    }
    peptides = ['ABBB', 'CBBB']
    expected = {
        'ABBB': 35, 'CBBB': 31
    }
    actual = calculate_mol_mass_collection(peptides,aa_mass_dict)

    assert actual == expected

test_calculate_mol_mass_collection()

def test_calculate_mz_collection():
    peptide_mass_map = {
        'A': 17.986, 'B': 12.986
        }
    actual = calculate_mz_collection(peptide_mass_map, charge=2)
    expected = {
        'A': 10.0, 'B': 7.5
    }

    assert actual == expected

test_calculate_mz_collection()