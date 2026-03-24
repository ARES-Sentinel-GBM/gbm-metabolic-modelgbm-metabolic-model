
import numpy as np

class AresEngine:
    def __init__(self, threshold=0.4):
        self.threshold = threshold

    def classify(self, vqe_score):
        if vqe_score < self.threshold:
            return 'SANO'
        elif vqe_score > 1.5 or vqe_score <= 0:
            return 'CORROTTO'
        else:
            return 'GBM'

    def calculate_survival(self, row):
        if row['Stato_Tessuto'] == 'SANO':
            return 0.98
        if row['Stato_Tessuto'] == 'CORROTTO':
            return 0.0
        
        base = 0.15
        if row['Genetica'] == 'IDH1-Mut':
            base += 0.72
        if row['Condizione'] == 'MOF':
            base += np.random.uniform(0.1, 0.3)
        return min(base, 1.0)
