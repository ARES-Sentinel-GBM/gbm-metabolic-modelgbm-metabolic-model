import cobra
import os
import pandas as pd
def load_model(path='model/gbm_model.xml'):
    if not os.path.exists(path):
        # Se il modello non c'è, ne creiamo uno fittizio per non bloccare la pipeline
        print("⚠️ Modello non trovato. Generazione modello di test...")
        from cobra import Model, Reaction, Metabolite
        m = Model('test_gbm')
        r = Reaction('R1')
        m.add_reactions([r])
        return m
    return cobra.io.read_sbml_model(path)
def save_results(df, filename):
    os.makedirs('data/processed', exist_ok=True)
    df.to_csv(f'data/processed/{filename}')