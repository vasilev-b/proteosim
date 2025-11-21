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
This script includes functions that simulate liquid chromatography.

```predict_lc_retention_times``` predicts the retention times of peptides within a dictionary relatively to each other, with the output also being a dictionary. Therefore, values can also be negative.

```plot_retention_time``` plots the predicted values in a histogram. 

```select_retention_time_window``` selects the retention times from a dictionary within a given window. The output is also a dictionary.

### C. ```liquid_chromatography.py```
In this part ...

### D. ```mass_spectra_simulation.py```
...

## 3. Example notebook
To see all the functions in action, you can check out the notebook ```ms_experiment_final.ipynb```. 

Have fun using the package!