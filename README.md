# Proteosim Course Package

## 0. Description
The goal of this package is to enable an easy simulation of key steps in proteomic analysis. This includes extraction of peptide sequences from FASTA files, peptide digestion, and LC-MS/MS.

The repository is **under active development**.

## 1. Dependencies
In order to use this package you need to download the dependencies contained in the ```requirements.txt``` file. To do that, simply write the following code in your terminal:

```
pip install -r requirements.txt
```
## 2. Package Description
The package contains 4 modules which are based on the main steps in proteomic analysis.
### A. ```file_handling.py```
This module contains the ```read_fasta``` function which takes a FASTA file with proteins and extracts their IDs as well as their sequences in a dictionary.

### B. ```protein_digestion.py```
This module can be used to digest proteins. 


```digest_protein_sequence``` takes a protein sequence string and digests it based on a specified cleavage pattern. The output is a list of peptides within a specific length window.

```digest_protein_collection``` also digests protein sequences, however it uses a dictionary of ID/sequence pairs. It then generates another dictionary containig the selected peptides of each protein.

```compute_sequence_coverage``` calculates the percentage of the reference sequence (str) covered by the generated peptides. The output is a float. 

### C. ```liquid_chromatography.py```
This part can be used to simulate liquid chromatography.

```predict_lc_retention_times``` predicts the retention times of peptides within a dictionary relatively to each other, with the output also being a dictionary. Therefore, values can also be negative.

```plot_retention_time``` plots the predicted values in a histogram. 

```select_retention_time_window``` selects the retention times from a dictionary within a given window. The output is also a dictionary.

### D. ```mass_spectra_simulation.py```
The final module covers the simulation of mass spectra - both MS1 and MS2.

```calculate_mol_mass``` calculates the molecular mass of a sequence (str) based on a dictionary containing amino acid/mass-pairs. The output is a dictionary. 
```calculate_mol_mass_collection```also calculates the molecular mass of sequences, but the input is a dictionary conatining multiple peptides.
```calculate_mz_collection``` calculates the m/z ratio.
```...``` ...

## 3. Example notebook
To see all the functions in action, you can check out the notebook ```ms_experiment_final.ipynb```. 

### Have fun using the package!