from proteosim.liquid_chromatography import predict_lc_retention_times, select_retention_time_window

import numpy as np

def test_predict_lc_retention_times():
    peptides = ['AAAAAK', 'AAAAA', 'CCCCCR', 'CCCCC', 'DDDDDRPDDDDD', 'FFFFFKPFFFFF']
    expected = {'AAAAAK': np.float64(10.8),
                'AAAAA': np.float64(11.0),
                'CCCCCR': np.float64(13.9),
                'CCCCC': np.float64(13.0),
                'DDDDDRPDDDDD': np.float64(-22.9),
                'FFFFFKPFFFFF': np.float64(92.0)}

    actual = predict_lc_retention_times(peptides)
    assert actual == expected

test_predict_lc_retention_times()

def test_select_retention_time_window():
    peptide_rt_map = {'A': -5, 'B': 3.4, 'C': 15.2}
    selected = select_retention_time_window(peptide_rt_map, lower_ret_time=0, upper_ret_time=10)

    assert selected == {'B': 3.4}

test_select_retention_time_window()