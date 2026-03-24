import pandas as pd
import numpy as np

def verify_dataset(df):
    results = {}
    passed = True
    
    # Test Anti-Bias
    idh1_surv = df[df['Genetica'] == 'IDH1-Mut']['Sopravvivenza'].mean()
    wt_surv = df[df['Genetica'] == 'Wild-Type']['Sopravvivenza'].mean()
    results['bias_check'] = "PASS" if idh1_surv > wt_surv else "FAIL"
    if idh1_surv <= wt_surv: passed = False

    # Test Anti-Falsificazione
    illegal = df[(df['Sopravvivenza'] < 0) | (df['Sopravvivenza'] > 1.0)].shape[0]
    results['falsification_check'] = "PASS" if illegal == 0 else "FAIL"
    if illegal > 0: passed = False

    # Test Diagnostico
    h_err = df[(df['Stato_Tessuto'] == 'SANO') & (df['Sopravvivenza'] < 0.90)].shape[0]
    results['diagnostic_integrity'] = "PASS" if h_err == 0 else "FAIL"
    if h_err > 0: passed = False

    return passed, results