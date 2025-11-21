def calculate_mol_mass(peptide_seq, amino_acid_mass_dict):
    """
    Calculates the molecular mass of a peptide.

    Parameters
    ----------
    peptide_seq: str
        Peptide sequence whose mass is to be calculated.
    amino_acid_mass_dict: dict
        Dictionary containing amino acid-mass pairs.
        
    Returns
    -------
    peptide_mass: dict
        Dictionary containing the peptide sequence and its corresponding mass.

    """
    mass = 0
    peptide_mass = {}

    for key, value in amino_acid_mass_dict.items():
            mass = mass + value * peptide_seq.count(key)
            peptide_mass[peptide_seq] = mass
    
    return peptide_mass

def calculate_mol_mass_collection(peptides, amino_acid_mass_dict):
    """
    Calculate the molecular masses of peptides from a list.
    
    Parameters
    ----------
    peptides: list
        List containing multiple peptides.
        
    amino_acid_mass_dict: dict
        Dictionary containing amino acids and their corresponding molecular masses.

    Returns
    -------
    peptides_mass: dict
        Dictionary containing peptide-mass pairs.

    """
    peptides_mass = {}
    for pep in peptides:
        mass = 0
        for aa, m in amino_acid_mass_dict.items():
            if aa in pep:
                mass = mass + m * pep.count(aa)
            peptides_mass[pep] = mass

    return peptides_mass

def calculate_mz_collection(peptide_mass_map, charge=2, proton_mass=1.007):
    """
    Takes peptide-mass pairs and maps the peptides to m/z values.

    Parameters
    ----------
    peptide_mass_map: dict
        Dictionary containing peptide-mass pairs.

    charge: int
        Charge given to the peptides after passing electrospray ionization (default=2).
    
    proton_mass: float
        Mass of a proton (default=1.007)
    
    Returns
    -------

    """
    peptide_mz_map = {}

    for pep, mass in peptide_mass_map.items():
        mz = (mass + charge * proton_mass) / charge
        peptide_mz_map[pep] = mz
    
    return peptide_mz_map

import numpy as np
import matplotlib.pyplot as plt

def plot_spectrum(mz_values, random_count_range=(0, 30000), seed=42, title='MS Spectrum'):
    """
    Visualizes randomly generated intensities to m/z values. 

    Parameters
    ----------
    mz_values: list
        List containing m/z values.
    
    random_count_range: tuple
        Range within a random value for the intensity should be drawn.
    
    seed: int
        Seed used for reproducibility of the random value drawn.
    
    title: str 
        Title of the barplot. (Default='MS Spectrum')

    Returns
    -------

    """
    int_list = []
    
    np.random.seed(seed)
    for x in mz_values:
        int_value = np.random.randint(random_count_range[0], random_count_range[1])
        int_list.append(int_value)

    plt.bar(mz_values, int_list, width=1)
    plt.title(title)
    plt.xlabel('m/z')
    plt.ylabel('Intensity')
    plt.show()