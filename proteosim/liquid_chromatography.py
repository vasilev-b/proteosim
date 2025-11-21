from pyteomics import achrom
def predict_lc_retention_times(peptides):
    """
    Predicts the retention times of peptides within a list.

    Parameters
    ----------
    peptides: list
        List of peptides whose lc-retention time is to be predicted.
   
    Returns
    -------
    peptides_retention_dict: dict
        Dictionary containing peptide/retention time pairs, with the retention time being rounded to two decimals.
    """
    peptides_retention_dict = {}

    for pep in peptides:
        retention = achrom.calculate_RT(pep, achrom.RCs_guo_ph7_0)
        peptides_retention_dict[pep] = round(retention, 2)
        
    return peptides_retention_dict

import matplotlib.pyplot as plt
def plot_retention_time(retention_times, resolution=30):
    """
    Creates a histogram out of the values of a dictionary.

    Parameters
    ----------
    retention_times: dict
        Dictionary containing peptide/retention time pairs.
    resolution: int
        Number of histogram bins (default=30).
    
    Returns
    -------
    
    """
    plt.hist(retention_times.values(), resolution, edgecolor='black')
    plt.title(f'Distribution of Peptide Retention Times')
    plt.xlabel('Retention time (relative)')
    plt.ylabel('# of fragments')
    plt.show()

def select_retention_time_window(peptide_rt_map, lower_ret_time, upper_ret_time):
    """
    Selects peptides from a given dictionary that have a retention time within a specific time window.

    Parameters
    ----------
    peptide_rt_map: dict
        Dictionary containing peptides and their corresponding retention times.

    lower_ret_time: {float, int}
        Minimal retention time.

    upper_ret_time: {float, int}
        Maximal retention time.
        
    Returns
    -------
    selected_retention_times: dict
        Dictionary containing only the selected peptides and their retention times.
    """
    selected_retention_times = {}
    for key, value in peptide_rt_map.items():
        if lower_ret_time <= value <= upper_ret_time:
            selected_retention_times[key] = value
    
    return selected_retention_times